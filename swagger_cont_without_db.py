### swagger content code with out db configuration ###

from fastapi import FastAPI
from models import Product
from database import session , engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")

def greet():
    return "welcome to the python world - reloaded successfully!"

# we need to write code for get the details of a products

products = [
    Product(id=1, name="Laptop", description="A personal computer", price=999.99, quantity=100),
    Product(id=2, name="Smartphone", description="A mobile device", price=499.99, quantity=25),
    Product(id=3, name="Headphones", description="Audio device", price=199.99, quantity=50),
    Product(id=4, name="Monitor", description="Display screen", price=299.99, quantity=15),]


@app.get("/products")
def get_products():
    return products

# getting product details by  product_id using "GET" method
@app.get("/product/{product_id}")
def get_product_by_id(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"error": "Product not found"}

# creating a new post using "POST" method
@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

# update the existing data with "PUT" Method
@app.put("/product")
def update_products(id:int, product:Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "product details updated"
    return "product details not found"
# delete data in the db using "DELETE" method
@app.delete("/product")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "product deleted"
    return "product not found"


