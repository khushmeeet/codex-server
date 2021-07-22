import uuid
from pydantic import BaseModel, HttpUrl, Field
from mongoengine import *


class WebAPIModel(BaseModel):
    id: int = Field(default_factory=uuid.uuid4, alias='_id')
    url: HttpUrl = Field(..., description='url of the webpage')
    content: str = Field(..., description='content of the webpage in HTML')

    class Config:
        all_ppopulation_by_field_name = True
        orm_mode = True
        schema_extra = {
            'example': {
                'id': 'f5e001d8-3682-4447-b20f-3fb105fb5b4e',
                'url': 'https://example.com',
                'content': '<h1>Hello World</h1>'
            }
        }


class WebDBModel(Document):
    url = URLField()
    content = StringField()
    added_on = DateTimeField(required=True)
    meta = {'collection': 'web'}


