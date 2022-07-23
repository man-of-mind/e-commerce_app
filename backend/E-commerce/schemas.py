from pydantic import BaseModel

class AllCatgoriesBase(BaseModel):
    id: int
    name: str
    
class AllCategories(AllCatgoriesBase):
    class Config:
        orm_mode = True
        

class Categories(BaseModel):
    name: str
    class Config:
        orm_mode = True
                
class SubCatgoriesBase(BaseModel):
    id: int
    name: str
    category_type: str

class SubCategories(SubCatgoriesBase):
    class Config:
        orm_mode = True
        
        
class TypeBase(BaseModel):
    id: int
    name: str
    sub_category_type: str
    sub_catgory_id: int
    

class Type(TypeBase):
    class Config:
        orm_mode = True
        

class ProductBase(BaseModel):
    id: int
    product_name: str
    type_id: int
    price: int
    

class Product(ProductBase):
    class config:
        orm_mode = True 
           