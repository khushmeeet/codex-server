from fastapi import APIRouter
from .models import WebSchema

web = APIRouter()


@web.get('/')
def default():
    print(WebSchema.objects)
    return {'Hello': 'World'}
