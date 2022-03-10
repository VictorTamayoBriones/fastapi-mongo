from fastapi import APIRouter

user = APIRouter()

@user.get('/users')
def find_all_users():
    return "Hello Wordl!"

@user.post('/users')
def create_user():
    return "Hello Wordl!"

@user.get('/users/{id')
def find_user():
    return "Hello Wordl!"

@user.get('/users')
def find_all_users():
    return "Hello Wordl!"

@user.get('/users')
def find_all_users():
    return "Hello Wordl!"