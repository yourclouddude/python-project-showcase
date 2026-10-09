from decimal import Decimal
from pydantic import BaseModel,ConfigDict,Field
class PracticeBook(BaseModel):
    model_config=ConfigDict(extra='forbid')
    title:str=Field(min_length=1,max_length=120,pattern=r'\S')
    author:str=Field(min_length=1,max_length=120,pattern=r'\S')
    price:Decimal=Field(ge=0,max_digits=10,decimal_places=2)
    available:bool=True
def validate_book(payload):
    book=PracticeBook.model_validate(payload)
    return {'title':book.title.strip(),'author':book.author.strip(),'price':format(book.price,'.2f'),'available':book.available}
