# Try Django Practice
1. Navigate to project directory (do this with every project)
2. Make sure Python version 3 is installed ```% python3 -V```
3. Create a virtual environment ```% python3 -m venv env```
  - Activate virtual environment ```% source env/bin/activate```
  - Download required packages ```% pip install -r requirements.txt```
  - Check modules installed in current environment ```% pip freeze```
  - Deactivate vritual environment ```% deactivate```
4. Activate venv and install django ```% pip3 install django==version``` (==version optional)
  - Run ```% django-admin``` to find list of django commands
5. Create a source directory to store all of the project files and cd into it
  - this will be the root directory for the project (root is wherever manage.py is) 
6. Create a django project ```% django-admin startproject project_name .``` 
7. Sync settings and apps using migrate ```% python manage.py migrate``` 
  - this will activate the django site and enable admin functionality
8. Go to the root folder (where manage.py is) and run server ```% python manage.py runserver```
  - control+c to deactivate server
9. To create an app, go to the root folder and run ```% python manage.py startapp app_name```
  - Go to model.py and create a class for the app (see 'blog' app example)
  - Add the app to the INSTALLED_APPS in project's settings.py
10. run the following whenever we make changes to models.py
  - ```% python manage.py makemigrations```
  - ```% python manage.py migrate```


---
# Django interactive shell
- To activate, run ```% python manage.py shell```
- We can import models; ```>>> from app.models import Model```
- We can create models; ```>>> Model.objects.create(field1='text', field2=20.22, field3=True)```
- To deactivate, run ```>>> quit()```
