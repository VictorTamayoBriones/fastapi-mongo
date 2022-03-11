from fastapi import APIRouter
from config.db import conn
from schemas.user import userEntity, usersEntity
from models.user import User

user = APIRouter()

@user.get('/users')
def find_all_users():
    return usersEntity(conn.local.user.find())

@user.post('/users')
def create_user(user: User):
    new_user = dict(new_user)
    print(new_user)
    return "Recibed"

@user.get('/users/{id}')
def find_user():
    return "Hello Wordl!"

@user.put('/users/{id}')
def update_user():
    return "Hello Wordl!"

@user.delete('/users/{id}')
def delete_user():
    return "Hello Wordl!"