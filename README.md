# Navigus Assignment

Link to deployed demo: https://navigus-assignment-prateek.herokuapp.com/

### Steps to run the Application locally:

#### Dependencies required:
- Python3.8
- Redis

##### Steps:

Make sure you have the dependencies mentioned above installed before proceeding further.

* **Step 0** - Clone the repository and ```cd ``` into the directory.

```sh
git clone git@github.com:prateekj117/navigus_assignment.git
cd navigus_assignment
```

* **Step 1** - Create virtualenv and Install Python Dependencies.

```sh
virtualenv -p python3.8 venv
. venv/bin/activate
python -m pip install -r requirements.txt
```

* **Step 2** - Run Migrations and Create Super User.

```sh
python manage.py migarte
python manage.py createsuperuser
```

* **Step 3** - Copy environment variables.

```sh
cp navigus_assignment/.env.example navigus_assignment/.env
```

* **Step 3** - Run Server.

```sh
python manage.py runserver
```

* Run Unit Tests:

```sh
python manage.py collectstatic
python manage.py test
```

#### Requirements explained and Methodology:

- Created both the backend and Frontend of the Application.
- Created basic user registration and authentication system.
- Created UI similar to the one shown in the Assignment pdf to show the users viewing that docs.
  For this, I used Django Channels along with Redis and [django-channels-presence](https://github.com/ml-learning/django-channels-presence)
  library. Everything is asynchronously updated. I also used logic for Heartbeats to make sure `last_seen` of users gets updated. To handle cases when
  server restarts and there are old entries in `Presence` Table, I also configured a Celery Task, to make sure that stale
  connections no longer exists. The presence page can only be accessed by Registered Users as was said in the aassignment.
  If unauthenticated users try to visit this page, they are redirected to Home Page.
- When you hover over the avatar, you can see the user info.
- Wrote some basic unit tests. Can be found in `navigus_assignment/tests`
- Also made a Dockerfile for the project for easy setup
- Deployed the app on Heroku. You can register an account, and then register another account in incognito, and keep an eye on UI. 
