from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]
    
    
    class Config:
        orm_mode=True
        schema_extra={
            'example':{
                
                "email":"vamsiabhiramg@gmail.com",
                "is_active":True,
                "is_staff":False,
                "password":"password",
                "username":"vamsi"
            }
        }
        
class Settings(BaseModel):
    authjwt_secret_key:str='a0283e9a538f41f8402672f8fe1276f9817bec12afc1e85b3afd58a896202db1'
    
class LoginModel(BaseModel):
    username:str
    password:str
    
class OrderModel(BaseModel):
    id:Optional[int]
    quantity:int
    order_status:Optional[str]="PENDING"
    pizza_size:Optional[str]='SMALL'
    user_id:Optional[int]
    
    
    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "quantity":2,
                "pizza_size":"LARGE"
            }
        }
        
class OrderStatusModel(BaseModel):
    order_status:Optional[str]="PENDING"
    
    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "order_status":"PENDING"
            }
        }