# Django-school-project

 ### Interductions
Simple school api build by django, this project have four model's students, instrucator, course, classess 
to help sign students to there class 

 ### Website Link
 [https://school-project-t.herokuapp.com/api/students/](https://school-project-t.herokuapp.com/api/students/)
 
 /instructors
 /courses
 /classes
 
 ### Installing Dependencies
 
 1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/Django-school-project
` directory and running:
```bash
pip3 install -r requirements.txt
```
This will install all of the required packages selected within the `requirements.txt` file.

4. **Key Dependencies**
 - [Django](https://www.djangoproject.com/)  Django is an advanced Web framework written in Python that makes use of the model view controller (MVC).

 - [PostgreSql](https://www.postgresql.org/) is Open Source Relational Database
 
### Database 
This project is connected with PostgreSql DB before running the project 
locate to `school_project/settings.py`

Scroll down to DATABASES and change it to you'r DB information 


### Running the Project

From within the `Django-school-project/` directory.

Ececute migration to detect any changes to your models.
```bash
python manage.py makemigration
python manage.py migrate
```
To run the server, execute:
```bash
python manage.py runserver
```

## API

[API Documents](https://documenter.getpostman.com/view/16467666/UVXjJvhj)  
Replace {{DJANG}} with https://school-project-t.herokuapp.com/

