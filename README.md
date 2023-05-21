# DemandForecasting

> Development python version : 3.10.6

---

## Steps to install ( Django Version - Bracnch `feature-1`)

> Given commands are for Linux based systems


- Clone the repository

- Create virtual environment ( Optional )

- Install requirements
    ```bash
    pip install -r requirements.txt
    ```

- Add `.env` file with below fields to the root of project ( where `manage.py` file is present )
    ```m
    SECRET_KEY='*******'    # Django Secret Key
    DB_NAME='*******'       # Databse Name
    DB_USER='*******'       # Databse User Name
    DB_PASSWORD='*******'   # Database Password
    DB_HOST='*******'       # Host For Database
    ```

- Create django database migrations
    ```bash
    python3 manage.py makemigrations
    ```

- Run migrations
    ```bash
    python3 manage.py migrate
    ```

- Create super user ( Admin User ) to access dashboard
    ```bash
    python3 manage.py createsuperuser
    ```

- Run server
    ```bash
    python3 manage.py runserver
    ```
---
