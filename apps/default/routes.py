from fastapi import APIRouter

r = APIRouter()

@r.get('/')
def default():
    return {'Hello': 'World'}
