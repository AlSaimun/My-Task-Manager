# My-Task-Manager
`Python 3.12.1` `Django 4.2.9` </br>
A Task Manager system User create, update, delete task. Implemented Authentiaction system.

## Features
- **User Authentication:** User can login, Signup, recover user account by reset password.
- **Task Management:** User can Create, Update, delete Task. 
- **Upload Multiple image:** User can Upload Multiple image when creat or update task.
- **Search by Title:** User can search task by title.
- **Real Time Notification:** Get real time notification when a task due date is over.

## Technologies Used
`Python 3.12.1` `Django 4.2.9` `Celery` `Django-Channels` `Django-Rest-Framework` `PostgreSQL` `HTML` `CSS` ` Bootstrap5` </br>

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/AlSaimun/My-Task-Manager.git
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
    # Use PostgreSQL 
    DB_NAME = 'database name'
    DB_USER= 'username'
    DB_PASSWORD= 'password'
    ```
    NB: It's for send email to user.
6. **Install Redis:**
    `https://redis.io/download/` </br>
   NB: Also another option is download **Memurai** `https://www.memurai.com/`.
8. **Run migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

9. **Start the development server:**

    ```bash
    python manage.py runserver
    ```
    
10. **Open your web browser and go to <a href="http://localhost:8000/" target="_blank">`http://localhost:8000/`</a> to access the application.**

11. **Create a superuser account to access the admin panel:**
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

