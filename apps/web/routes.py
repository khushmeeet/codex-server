from fastapi import APIRouter, Body
from .models import WebDBModel, WebAPIModel
import datetime
import json

web = APIRouter()


@web.get('/', response_description='List all data in Web Collection')
def list_data():
    data = []
    for obj in WebDBModel.objects:
        data.append({'id': str(obj.id), 'url': obj.url, 'content': obj.content, 'added_on': obj.added_on})
    return data

@web.post('/new', response_description='Add data to Web Collection')
def new_data(web_model: WebAPIModel = Body(...)):
    data = WebDBModel(
        url=web_model.url,
        content=web_model.content,
        added_on=datetime.datetime.now(datetime.timezone.utc)
    ).save()
    return data