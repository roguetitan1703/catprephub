# 📋 CATPrepHub

## 📝 Description

CATPrepHub is a web platform designed to help you conquer the CAT exam (Common Admission Test) in India. It provides features for simulating mock tests, analyzing your performance, and potentially offering curated learning resources.

## 🌟 Features

- **User Authentication (Login & Signup)**
- **Mock Test Simulations:**
    - Select Test Sections (QA, VA, LR, DI)
    - Answer Engaging Questions
    - Time Limit Enforcement (Optional) ⏰
    - Score Calculation
- **Performance Analysis:**
    - View Detailed Test Results
    - Data Visualizations for Insights
- **Learning Resources (Optional):**
    - Access Curated Articles & Videos

## 💻 Technologies Used

- Backend: Django (Python Web Framework)
- Frontend: HTML, CSS, JavaScript
    - Bootstrap (CSS Framework)
- Chart.js (JavaScript Charting Library)
- jQuery (JavaScript Library) 🪄
- Database: Django- sqlite

## 🛠️ Setup Instructions

**Prerequisites:**

- Python 3 (Download from [https://www.python.org/downloads/](https://www.python.org/downloads/))

1. **Create a Virtual Environment (Recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate.bat  # Windows
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Database:**

   - Follow Django's documentation to set up your database connection.

4. **Run Database Migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser (Optional):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run Development Server:**

   ```bash
   python manage.py runserver
   ```

7. **Access Application:**

   Open http://127.0.0.1:8000/ in your web browser.

## 🚀 Usage

1. **Register or Login:** Create an account to access CATPrepHub's features.
2. **Select a Test:** Choose the test section you want to simulate (QA, VA, LR, DI).
3. **Take the Mock Test:** Answer questions within the time limit (optional).
4. **Review Results:** Analyze your performance and identify areas for improvement.
5. **Explore Resources (Optional):** Access curated learning materials to enhance your preparation.

## 📚 Additional Notes

- Consider using a version control system like Git to track your codebase changes.

## Combined Takeaways and Challenges

Developing CATPrepHub involved various challenges, but also provided valuable insights into creating educational platforms. One of the key takeaways was the importance of user engagement in educational apps. Integrating features like engaging questions and visualized performance analysis not only enhances user experience but also facilitates better learning outcomes. However, managing complex database structures and ensuring seamless interaction between frontend and backend components posed significant challenges. Overcoming these obstacles required meticulous planning, continuous testing, and iterative development processes.

## 📄 License

This project is licensed under the MIT License (refer to LICENSE file for details).
