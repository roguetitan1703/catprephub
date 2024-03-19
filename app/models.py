from django.db import models
from django.contrib.auth.models import User

import json

# Create your models here.
class TestSection(models.Model):
    """
    Model representing a test section within a CAT exam.
    """
    test_name = models.CharField(max_length=255)  # Renamed for clarity
    description = models.TextField(blank=True)
    time_limit = models.PositiveIntegerField(help_text="Time limit in minutes")

    def __str__(self):
        return self.test_name  # Use test_name for display

class Question(models.Model):
    """
    Model representing a question within a test section (all MCQ).
    """
    text = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=255)
    section = models.ForeignKey(TestSection, on_delete=models.CASCADE)

    def __str__(self):
        """Returns a JSON string representation of the question object."""
        data = {
            'text': self.text,
            'option1': self.option1,
            'option2': self.option2,
            'option3': self.option3,
            'option4': self.option4,
            'correct_option': self.correct_option,
        }

        return json.dumps(data, indent=4)

class TestResult(models.Model):
    """
    Model representing a user's test result for a specific section.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_section = models.ForeignKey(TestSection, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True, blank=True)
    displayed_questions = models.ManyToManyField(Question, related_name='displayed_in_tests', blank=True)
    
    end_time = models.DateTimeField(null=True, blank=True)
    attempted_questions = models.ManyToManyField(Question, related_name='attempted_in_tests', blank=True)
    correct_answers = models.ManyToManyField(Question, related_name='correct_answers', blank=True)
    wrong_answers = models.ManyToManyField(Question, related_name='wrong_answers', blank=True)
    score = models.IntegerField(default=0)
    time_taken = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.test_section.test_name} Result"
