SMART MESS - COLLEGE FINAL PROJECT
=================================

PROJECT FLOW
------------
Home -> Choose Login Type -> Admin Login / Student Login

Admin:
  Dashboard -> Students -> Absence -> Food Waste -> Reports -> Suggestions -> Logout

Student:
  Home -> Profile -> Submit Absence -> Feedback -> Logout

DATABASE COMPATIBILITY
----------------------
This project intentionally uses the existing smart_mess tables visible in your college project:

  admin
  students
  meal_absence
  food_waste
  feedback

The students table is used directly for Student Login. No student_accounts table is required.

The expected students columns are:
  id, student_id, name, email, mobile, password, otp_verified, created_at, otp, otp_expiry

The expected meal_absence columns are:
  id, student_id, absence_date, breakfast, lunch, dinner, created_at

The expected food_waste columns used by this project are:
  waste_kg, detected_at

The expected feedback columns used by this project are:
  student_id, meal, rating, comment

SETUP
-----
1. Put app.py, auth.py and database.py in the same college project folder.
2. In database.py change YOUR_MYSQL_PASSWORD to your MySQL root password.
3. Make sure MySQL service MySQL80 is running.
4. Make sure the database is named smart_mess.
5. Run:
      pip install -r requirements.txt
6. For Student Login, the student's password must not be NULL. Use student_password_setup.sql for a test account, or set a password using your existing registration flow.
7. Run:
      python -m streamlit run app.py

LOGIN
-----
Admin Login uses the existing admin.username + admin.password columns.
Student Login uses the existing students.student_id + students.password columns.

IMPORTANT
---------
Do NOT run an old setup.sql that creates a student_accounts table. This final version is written to use your existing students table so it does not mismatch your college database.
