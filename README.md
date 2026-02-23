This project is a Django REST API for managing student assignments. Students can register, login, view, add, update, and delete their assignments.  
1. Clone the repository

git clone https://github.com/Gino2525/Campus-Assignment-Management-API.git
cd Campus-Assignment-Management-API

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

Then open http://127.0.0.1:8080 in your browser.

have a simple front end integrated for better testing


How to Use
1. Registration

Open the frontend page in your browser.
Click Register.
Fill in the Username, Full Name, Email, Password, Department, and Year.
Click Register.

After successful registration, you will see a message prompting you to login.

2. Login(JWT Auth)

Enter your Username and Password on the login form.
Click Login.
After login, you will be redirected to the Assignments Dashboard.

3. Add Assignment

In the Add Assignment section:
Enter Title, Subject, Description.
Select Status (Pending, Submitted, Approved).

Click Add 

The assignment will appear in your assignments list.

4. Update Assignment

Modify the Title, Subject, Description, or Status directly in the assignment card.
Click Update.
The Updated At timestamp will reflect the change.

5. Delete Assignment

Click Delete on any assignment card to remove it.

7. Logout  (Refresh token is stored locally for a better user experience.)

Click Logout to return to the login page. 
_____________________________________________________________________________________
🔗 API Documentation
Base URL: http://127.0.0.1:8000/

👤 Authentication Endpoints
Base URL: http://127.0.0.1:8000/

POST/register/ -Register a new student
POST,/login/  -Login and receive JWT tokens
POST,/token/refresh/ -Refresh access token using refresh token

GET	/departments/	-Get list of all departments (used in registration form select field)

Assignment Endpoints

Method,Endpoint,Description
GET/assignments/-Get all assignments for logged-in student
POST/assignments-Create a new assignment
GET/assignments/<id>/-Retrieve a specific assignment
PUT/assignments/<id>/-Update a specific assignment
DELETE/assignments/<id>/-Delete a specific assignment
