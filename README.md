# Task-Manager-Project
`Python 3.12.1` `Django 4.2.6` </br>
A Task Manager system User create, update, delete task. Implemented Authentiaction system.

## Features
- **User Authentication:** User can login, Signup, recover user account by reset password.
- **Task Management:** User can Create, Update, delete Task. 
- **Upload Multiple image:** User can Upload Multiple image when creat or update task.
- **Search by Title:** User can search task by title.

## Technologies Used
`Python 3.12.1` `Django 4.2.6` `Django-Rest-Framework` `HTML` `CSS` ` Bootstrap5` </br>

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/AlSaimun/Task-Manager-Project.git
    ```
2. **Create a virtual environment:**

    ```bash
    python -m virtualenv venv
    ```
3. **Activate the virtual environment:**

    - On Windows:

    ```bash
    .\venv\Scripts\activate
    ```

    - On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```
4. **Install requirements.txt:**

    ```bash
    pip install -r requirements.txt
    ```
5. **Create and Set Up `.env` file:**
    ```
    # email credential for reset password
    EMAIL_HOST_USER =  'example@gmail.com'
    EMAIL_HOST_PASSWORD = 'examplepassword'
    
    # Database credentials
    DB_NAME = 'database name'
    DB_USER= 'username'
    DB_PASSWORD= 'password'
    ```
    NB: It's for send email to user.
6. **Run migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. **Start the development server:**

    ```bash
    python manage.py runserver
    ```
    
8. **Open your web browser and go to <a href="http://localhost:8000/" target="_blank">`http://localhost:8000/`</a> to access the application.**

9. **Create a superuser account to access the admin panel:**
    ```bash
    python manage.py createsuperuser
    ```
## API endpoints
1. Get all tasks by certain user.
```
http://127.0.0.1:8000/tasks/api/task/
```
2. Retrive, PUT/Patch and delete task.
```
http://127.0.0.1:8000/tasks/api/task/1/
```
3. Get Acess token using JWT
```
http://127.0.0.1:8000/jwt/login/ 
```
NB. Use jwt login for get acess token else you can't access to see data. Also tasks filter by user
NB. For see details of a task click over the task card

If any confusion feel free to ask me, Thanks for your time.


# My-Task-Manager
