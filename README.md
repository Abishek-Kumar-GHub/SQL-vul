# SQL Injection Vulnerability Lab (Django)

This repository contains a simple Django-based web application designed to demonstrate a **SQL Injection** vulnerability. The application has a login page that allows users to submit their credentials, and the credentials are used directly in a SQL query without proper sanitization. This exposes the application to SQL Injection attacks.

## Overview

The application contains a vulnerable login feature where an attacker can inject arbitrary SQL code into the login form's inputs. The vulnerability arises from the direct inclusion of user inputs in a SQL query, which can result in unauthorized access to the application.

### Vulnerability Demonstrated:

- **SQL Injection**: The vulnerability allows an attacker to manipulate the SQL query by injecting malicious SQL code through user input fields. This can bypass authentication, retrieve sensitive data, or modify the database.

### Example:
If an attacker submits the following string in the username field:

```sql
' OR 1=1 -- 
```
And any value in the password field, the application will log in without checking the credentials, due to the injected OR 1=1 condition, which always evaluates to true. This is the essence of SQL Injection.

### Features:
- **Login Form**: Allows users to enter their username and password.
- **Vulnerable to SQL Injection**: The application uses user input directly in SQL queries without proper sanitization, making it susceptible to SQL Injection.
  
## Running the Application
Follow these steps to run the application locally:

### Prerequisites:
- Python 3 and pip installed on your system.
- Django installed (pip install django).
- SQLite database used for storage.

### Steps:
1. Clone the repository:
```bash
git clone https://github.com/Abishek_Kumar_GHub/SQL-XSS-vul.git
cd sql-injection-lab
```
2. Create a virtual environment (optional but recommended):
```bash
 python3 -m venv venv
 source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3. Install dependencies(Django):
```bash
pip install django
```
5. Run the Django application:
```bash
python manage.py runserver
```
The application should be running at http://127.0.0.1:8000/

### Access the Application:
Open your browser and navigate to http://127.0.0.1:8000/. You can now attempt the SQL Injection attack using the login form.

## How to Demonstrate the Vulnerability:
1. Navigate to the login page at http://127.0.0.1:8000/login/.
2. Enter the following in the Username field:
```sql
' OR 1=1 --
```
3. Enter any value in the Password field (e.g., anypassword).
4. Click "Login".
5. You will be logged in without proper credentials, demonstrating the SQL Injection vulnerability.
   
## Fixing the Vulnerability (Solution)
The vulnerability can be fixed by using parameterized queries or Django's built-in ORM methods, which automatically escape user input to prevent SQL Injection attacks.

### Example of Fix:
In the vulnerable view, replace the raw SQL query with Django's built-in authenticate() method that uses the ORM to safely query the database.

#### Before Fix (Vulnerable Code):

```python
query = f"SELECT * FROM auth_user WHERE username='{username}' AND password='{password}'"
with connection.cursor() as cursor:
    cursor.execute(query)
    user = cursor.fetchone()
```
#### After Fix (Safe Code):

```python
from django.contrib.auth import authenticate

user = authenticate(request, username=username, password=password)
if user is not None:
    # Proceed with login
    login(request, user)
Using the authenticate() method ensures that user input is properly escaped and prevents SQL Injection attacks.
```
**safecode.py** have the safe method to do the application without sql injection vulnerability. Copy that file and paste in views.py to domonstrate the mitigation

## Contributing
Feel free to open issues or submit pull requests for improvements. If you want to help fix the vulnerability or add additional features, your contributions are welcome!

