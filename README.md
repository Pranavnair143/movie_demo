# Movie Demo

## Requirements:
1) Python 3.11 or higher
2) Postgres DB required (Array[Json] is not supported in SQlite)

## Steps:
1) Create a virtualenv and install all dependencies from requirements.txt
     ```markdown
    virtualenv venv
    pip install -r requirements.txt 
    ```
2) Place the required credentials in .env file.
3) Migrate the table schema in your local DB and Run the Django app
   ```markdown
    python manage.py migrate
   python manage.py runserver
    ```

## Postman collection link --> [Link](https://drive.google.com/file/d/1px2rL2RjacamRUrhAUFT2w9Mnz-fvqwU/view?usp=sharing)
