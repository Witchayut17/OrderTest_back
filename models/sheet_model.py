from pydantic import BaseModel
from typing import Dict

class SheetName(BaseModel):
    name:str

class CsvInput(BaseModel):
    data:list[Dict]
    sheet:SheetName

class OrderReceive(BaseModel):
    customer_name:str
    order_items:str

class OrderPayload(BaseModel):
    data:list[OrderReceive]