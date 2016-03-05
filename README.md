# DRF-TDD-Example

An example Django REST framework project for test driven development.

##API Endpoints

####Users

* **/api/users/** (User registration endpoint)
* **/api/users/login/** (User login endpoint)
* **/api/users/logout/** (User logout endpoint)


####Todos

* **/api/todos/** (Todo create and list endpoint)
* **/api/todos/<todo-id>/** (Todo retrieve, update and destroy endpoint)

##Install 

    pip install -r requirements.txt

##Usage

    python manage.py test

