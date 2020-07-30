># Test dacodes - Matrixes and course API
## Requirements
### download and install Python 3 in your computer
[Download Python 3](https://www.python.org/downloads/)

### Install Django framework
```bash
pip install Django
```

### Install Django rest-framework
```bash
pip install djangorestframework
```

### Install numpy library
```bash
pip install numpy
```
# Matrixes
### open a terminal and going to folder matrixes and execute the command
```bash
python snake.py
```


# Courses API

### for to run the API, open a terminal and going to folder courses and execute the command

```bash
python manage.py runserver
```
### open a browser and enter the url 
http://127.0.0.1:8000/adminpanel/

### in this section you can create, edit and delete courses, lesson, questions and responses, users and assign courses to the students
---
> get information from the API

## Get List of users
http://127.0.0.1:8000/api/users/

```bash
GET /api/users/

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "name": "cesar alberto equihua zepeda",
        "type": "student",
        "username": "cequihua"
    },
    {
        "name": "Marta Nicio De la Cruz",
        "type": "professor",
        "username": "mnicio"
    }
]
```
## Get the user by username
```bash
POST /api/users/

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "username":"theusername"
}
```

## Get List of Courses
http://127.0.0.1:8000/api/courses/

```bash
GET /api/courses/

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "course_id": {
            "name": "Java desde Cero",
            "number": "",
            "score": 300.0
        }
    },
    {
        "course_id": {
            "name": "Python desde 0",
            "number": "",
            "score": 200.0
        }
    }
]
```
## Get the Curses by username
```bash
POST /api/courses/

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "username":"theusername"
}
```

## Get List of Lessons
http://127.0.0.1:8000/api/lessons/
```bash
GET /api/lessons/

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "name": "Intrduccion",
        "number": "",
        "score": 12.0,
        "course_id": {
            "name": "Python desde 0",
            "number": "",
            "score": 200.0
        },
        "details": "KKSDKSDKLSDKLSDKL"
    },
    {
        "name": "Variables",
        "number": "",
        "score": 20.0,
        "course_id": {
            "name": "Python desde 0",
            "number": "",
            "score": 200.0
        },
        "details": "KDDFKSDF"
    },
    {
        "name": "Condicionales",
        "number": "",
        "score": 30.0,
        "course_id": {
            "name": "Java desde Cero",
            "number": "",
            "score": 300.0
        },
        "details": "False"
    }
]
```
## Get the Lessons by username
```bash
POST /api/lessons/

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "username":"theusername"
}
```

## Get List of Questions
http://127.0.0.1:8000/api/questions/

```bash
GET /api/questions/

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "name": "Quien Invento Python ?",
        "score": 10.0,
        "lesson_id": {
            "name": "Intrduccion",
            "number": "",
            "score": 12.0,
            "course_id": {
                "name": "Python desde 0",
                "number": "",
                "score": 200.0
            },
            "details": "KKSDKSDKLSDKLSDKL"
        }
    }
]
```
## Get the Questions by username
```bash
POST /api/questions/

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "username":"theusername"
}
```





