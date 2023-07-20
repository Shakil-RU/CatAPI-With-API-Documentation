# Steps of Creating an API With API Documentation

### Before all, python must be installed in system

## Step-1: Creating virtual environment
Create an empty folder "Practice". Inside the folder create virtual environment<br/>
`python -m venv env`

## Step-2: Activation of virtual envvironment
Activate the virtual environment<br/>
`cd env`<br/>
`cd Scripts`<br/>
`activate`

## Step-3: Django and rest framework installtion
Go back to the project folder "Practice" and install Django and rest framework<br/>
`pip install django`<br/>
`pip install djangorestframework`

## Step-4: Creating Project
Create a new Django project "catproject"<br/>
`django-admin startproject catproject`

## Step-5: Run Project
Run the project if it is working properly<br/>
`python manage.py runserver`

## Step-5: Creating app
Create a new app "catapp"<br/>
`python manage.py startapp catapp`

## Step-6: Including app in project
Go to the settings.py file inside catproject and add 'catapp' and 'rest_framework' in INSTALLED_APPS

## Steps-7: Implemienting the app
Go to the "catapp" folder.<br/>
Implement The model inside models.py<br/>
Create serializers.py and implement serializer including all fields of the model.<br/>
In views.py implement CRUD operations for the model<br/>
Create urls.py and define the urls<br/>
Go to the urls.py in "catproject" and include urls.py of the "catapp"

## Steps-8: Documentation
Install the module `pip install drf-yasg`<br/>
Go to settings.py and add this `'drf_yasg',` in INSTALLED_APPS<br/>
Go to urls.py in "catproject" and add the code snippet<br/>

```
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
```
```
schema_view = get_schema_view(
   openapi.Info(
      title="Dog API",
      default_version='v1',
      description="Documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@dogapp.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
```
```
urlpatterns = [
    path('documentation.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```
For more details about documentation go to the website [Link](https://drf-yasg.readthedocs.io/en/stable/readme.html#installationhttps://drf-yasg.readthedocs.io/en/stable/readme.html#installation)

## Step-9: Unit testing
Go to tests.py in "catapp" and implement the testing. <br/>
For running the tests.py write `python manage.py test`
