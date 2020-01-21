# TITTLE : 
Neighborhood

## AUTHOR 
Owino Lawrence Odhiambo

## Getting Started
Fork this repository or clone it to your local machine on ubuntu use the following commands.

git clone [https://github.com/owinolawrence/neighborhood.git]

## User Story
As a user of the application you will be able to:
    .register and login.
    .view your profile and see the projects you have uploaded.
    .view different projects by other users.
    .click on a project and view to details and vote.
    .view the project site itself.

## Pre-requisites

1.What you need.
.python version3.6
.postgres database

## Installation
1. Set up a virtual environment using the command.

python3 -m venv  virtual

And activate virtual

    source virtual/bin/activate

2. Install the requirements use the command...

pip install -r requirements.txt

3. create a .env file and add

SECRET_KEY='<random-string>'
DEBUG=True
ALLOWED_HOSTS='*'
DATABASE_URL='postgres://databaseowner:password@localhost/databasename'

4. create a database using postgres

    CREATE DATABASE <your-database-name>

5. create a migration using the following command

    python3 manage.py makemigrations

    and migrate

   python3 manage.py migrate

6. create a super user for admin account

   python 3.6 manage.py createsuperuser

7. To run user :

    python3 manage.py runserver

   1. navigate to admin by adding /admin to your local host url like so :


127.0.0.1:8000/admin


## Running the tests

python3 manage.py tests

## Technologies Used
.Html5 and Css3
.Python
.Bootdstrap 3
.Django - The web framework used
.JQUERY

## Acknowledgments
Moringa School for guidance

## License
This project is licensed under the MIT License - see the [LICENSE]file for details.