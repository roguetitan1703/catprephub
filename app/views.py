from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import TestSection, Question, TestResult 
from datetime import datetime
from .utils import calculate_time_taken

# Other imports
from random import shuffle

# Signup View
def signuppage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse('Passwords do not match')

        user = User.objects.create_user(username, email, pass1)
        user.save()

        return redirect('login')

    return render(request, 'registration/signup.html', {})

# Login View
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')

        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('/')

        return HttpResponse('Invalid Credentials')

    return render(request, 'registration/login.html', {})

# Logout View
def logoutpage(request):
    logout(request)
    return redirect('login')

# Protected Views (using @login_required decorator)
@login_required
def index(request):
    return render(request, 'index.html', {})

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def joinus(request):
    return render(request, 'joinus.html')

@login_required
def community(request):
    return render(request, 'community.html')
@login_required
def rankboard(request):
    """
    Displays a leaderboard featuring all users with test scores, time taken, and test section.
    """

    # Fetch all test results, ordered by score in descending order (minus sign signifies descending)
    test_results = TestResult.objects.select_related('test_section').order_by('-score')

    leaderboard_data = []
    for result in test_results:
        user = result.user
        user_data = {
            'username': user.username,
            'name': user.get_full_name(),  # Assuming a `get_full_name` method exists
            'score': result.score,
            'time_taken': result.time_taken,
            'test_section': result.test_section.description,  # Assuming a `name` field in TestSection
        }
        leaderboard_data.append(user_data)

    context = {
        'leaderboard_data': leaderboard_data,
    }

    return render(request, 'rankboard.html', context)


@login_required
def viewtests(request):
    # Add logic to display available test sections
    test_sections = TestSection.objects.all()
    context = {'test_sections': test_sections}
    return render(request, 'viewtests.html', context)

@login_required
def taketest(request):
    if request.method == "GET":
        test_section_id = request.GET.get('test_section')

        # Get the requested test section
        try:
            test_section = TestSection.objects.get(pk=test_section_id)
        except TestSection.DoesNotExist:
            return HttpResponse('Invalid Test Section')

        # Filter questions belonging to the test section
        questions = Question.objects.filter(section=test_section)

        # Handle scenarios with fewer than 15 questions (optional)
        if questions.count() < 15:
            all_questions = questions
        else:
            all_questions = list(questions)
            shuffle(all_questions)
            selected_questions = all_questions[:15]

        # Create a new TestResult
        test_result = TestResult(
            user=request.user,
            test_section=test_section,
            start_time=datetime.now(),
        )
        test_result.save()  # Save the object to generate an ID

        for question in selected_questions:
            test_result.displayed_questions.add(question)

        test_result.save()  

        context = {'test_section': test_section, 'questions': selected_questions, 'test_result_id': test_result.id}

        return render(request, 'taketest.html', context)   
    
    elif request.method == "POST":
        answer_data = request.POST  # Get submitted data
        test_section_id = request.POST.get('test_section_id')
        test_result_id = request.POST.get('test_result_id')

        # Retrieve the TestSection object
        try:
            test_section = TestSection.objects.get(pk=test_section_id)
        except TestSection.DoesNotExist:
            return HttpResponse('Invalid Test Section')

        # Retrieve the TestResult object
        try:
            test_result = TestResult.objects.get(pk=test_result_id)
        except TestResult.DoesNotExist:
            # Handle potential error (e.g., log the error)
            return HttpResponse('Invalid Test Result')

        # Process and evaluate answers
        num_questions_attempted = 0
        num_correct_answers = 0
        num_wrong_answers = 0
        
        # 
        test_result.end_time = datetime.now()
        # test_result.attempted_questions = set()
        # test_result.correct_answers = set()
        # test_result.wrong_answers = set()
        # test_result.score = 0

        # Evaluating Result
        
        for question_id, answer_value in answer_data.items():
            if question_id.startswith('question_'):  # Filter question data
                question_id = int(question_id.split('_')[1])
                
                try:
                    # Going through attempted question
                    question = Question.objects.get(pk=question_id)
                    
                    test_result.attempted_questions.add(question)  # Add to attempted questions set
                    num_questions_attempted += 1

                    # Compare selected answer with correct answer
                    if answer_value == question.correct_option:
                        test_result.correct_answers.add(question)  # Add to correct answers set
                        num_correct_answers += 1
                    
                    else:
                        test_result.wrong_answers.add(question)  # Add to wrong answers set
                        num_wrong_answers += 1
                        
                except Question.DoesNotExist:
                    print(f"Question with ID {question_id} not found. Skipping...")

        # Calculate score based on adjusted logic (4 * right - wrong)
        calculated_score = (num_correct_answers * 4) - num_wrong_answers

        # Update TestResult object
        test_result.score = calculated_score
        test_result.completed = True  
        test_result.time_taken = calculate_time_taken(test_result)
        test_result.save()

        # return HttpResponse(f'Attempted={num_questions_attempted} Correct={num_correct_answers} Wrong={num_wrong_answers} Score={calculated_score}')
        # Rendering the testresult page
        return render(request, 'testresult.html', {'test_result': test_result})

@login_required
def testanalysis(request):
    if request.method == "GET":
        test_result_id = request.GET.get('test_result_id')

        try:
            test_result = TestResult.objects.get(pk=test_result_id)
        except TestResult.DoesNotExist:
            return HttpResponse('Invalid Test Result')

        total_questions = test_result.attempted_questions.count()

        correct_answers = test_result.correct_answers.count()

        wrong_answers = test_result.wrong_answers.count()

        # Calculate accuracy
        if correct_answers == 0:
            accuracy = 0 
        else:
            accuracy = round((correct_answers / total_questions) * 100, 2)

        # This is a placeholder for illustrative purposes
        all_test_results = TestResult.objects.all().order_by('-score')
        user_rank = None
        for index, result in enumerate(all_test_results):
            if result.pk == test_result.pk:
                user_rank = index + 1
                break

        wrong_answer_question_ids = test_result.wrong_answers.values_list('id', flat=True)
        wrong_answer_questions = Question.objects.filter(pk__in=wrong_answer_question_ids).select_related('section')  # Optimize query

        # Context
        context = {
            'test_result': test_result,
            'accuracy': accuracy,
            'total_questions': total_questions,
            'correct_answers': correct_answers,
            'wrong_answers': wrong_answers,
            'wrong_answer_questions': wrong_answer_questions,
            'rank': user_rank,
        }

        return render(request, 'testanalysis.html', context)

    return HttpResponse('Invalid request method')        
            
        
@login_required
def performance(request):
    if request.method == "GET":
        """
        Retrieves all test results, deletes unfinished ones (completed=False),
        and renders the performance.html template with remaining results.

        Handles potential database errors gracefully and provides informative error messages.
        """

        try:
            # Delete unfinished test results (completed=False) using bulk deletion for efficiency
            TestResult.objects.filter(completed=False).delete()

            # Fetch all test results for the authenticated user using related manager
            test_results = TestResult.objects.filter(user=request.user).select_related('user')  # Optimize for performance
            
            if test_results == []:
                return render(request, 'performance.html')
            
            test_section = TestSection.objects.all()  # Retrieve all test sections for the performance page
            
            
            context = {
                'test_results': test_results,
                'test_section': test_section,
            }

            return render(request, 'performance.html', {'test_results': test_results})

        except Exception as e:
            # Handle potential database errors gracefully
            context = {'error_message': e}
            return render(request, 'performance.html', context)
    
    else:
        return HttpResponse("Invalid request method")
        
        
@login_required
def resources(request):
    return render(request, 'resources.html')