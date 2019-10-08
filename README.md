# Event Organisation Booking System

This project was a KTH assignment for Modern Methods of Software Engineering. It models the workflow of an imaginary event-planning company "SEP". Specifically, it shows the basic workflows of

1. Customer service officers, taking bookings ("event request applications") from a client
2. Senior customer sevice officers and administration manager that approve the event bookings
3. Financial managers that
   * approves these bookings
   * approves budget requests
4. Staff managers, that
   * creates budget requests
   * create subteam tasks
   * create staff requests
5. HR managers that view staff requests

## Installing Project

1. Install Python 3.7.4
2. Setup virtual environment in folder venv/

    ```bash
    cd path/to/project
    python3 -m venv venv
    ```

3. Start using python distribution of venv

    ```bash
    source bin/activate
    ```

    Check which python/pip is being used by doing

    ```bash
    which pip
    # or
    which python
    ```

4. Install all requirements into venv

    ```bash
    pip install -r requirements.txt
    ```

In case a new database should be used, be sure to initialize it properly:

1. Execute migrations

    ```bash
    python manage.py migrate
    ```

2. Initialize data

    ```bash
    python manage.py shell_plus < sep/create_user_groups.py
    ```

    This could have been done better by writing the file into migrations.
    `shell_plus` is part of django-extensions which executes a Python shell that uses the Django Project as a environment.
    A super user would have to be created manually however. See Django Docs for that.

## Running Project

Running this project will be fairly straightfoward.

1. Start project (using python from /venv)

    ```bash
    python manage.py runserver 0:8001
    ```

2. Visit localhost:8001/sep/home
3. Login with

| Username     | Password |
| ------------ |:--------:|
| sep_superuser | abc123 |
| customer_service_officer_1 | abc123 |
| senior_customer_service_officer_1 | abc123 |
| financial_manager_1 | abc123 |
| production_manager_1 | abc123 |
| service_manager_1 | abc123 |
| administration_manager_1 | abc123 |
| hr_manager_1 | abc123 |
