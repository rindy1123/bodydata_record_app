# BodyData Record App
You can record what type of exercise you did, what you ate, and your weight. 
## Table of Contents
+ Description
+ Demo
  + Sign up
  + Login and Home and Timeline screen
  + Edit data
+ Environment
+ Import
+ Run server
## Description
You can get healthier by using this app.  

If you sign up and login, you can record what type of exercise you did, what you ate, and your weight.  
This app automatically calculate how much calories you should consume to lose weight or gain weight. 

You can also see other people's data, and learn what you should do to get healthier from these data.

## Demo
### Sign up
![sign-up mov](https://user-images.githubusercontent.com/39889160/63482572-56ce9200-c4d4-11e9-9d52-49852bac2200.gif)

### Login and Home and Timeline screen
![login_home_timeline mp4](https://user-images.githubusercontent.com/39889160/63483249-baf25580-c4d6-11e9-88bc-d38948b77b90.gif)

### Edit data
![edit_data mov](https://user-images.githubusercontent.com/39889160/63483502-93e85380-c4d7-11e9-8617-8a0fe5c6c277.gif)  

## Environment
macOS Mojave ver.10.14.6  
python 3.7.4  
HTML5  
CSS  
SQLite3  
django 2.2.4  

## git clone
```
$ git clone https://github.com/rindy1123/bodydata_record_app.git
```

## Import
django
```
$ pip install django
```
## Migration
```
$ python manage.py makemigrations

$ python manage.py migrate
```
## Create admin account
```
Username: <username>
Email address: <email@example.com>
Password: <password>
```
If errors has emerged like this, you don't have to worry.
```
This password is too short. It must contain at least 6 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```
Then, you can go to administration site.
## Run server
``` 

$ python manage.py runserver

System check identified 3 issues (0 silenced).
August 22, 2019 - 12:43:37
Django version 2.2.4, using settings 'muscleproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```
Then go to http://127.0.0.1:8000/

You can see urls in 'bodydata_record_app/bodydata_record_app/urls.py'.
If you want to go to 'Signup page', add url like this 'http://127.0.0.1:8000/signup/'.

