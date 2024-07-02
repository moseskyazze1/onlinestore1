from flask import Flask, request
import json
from config import db

app= Flask(__name__)

@app.get("/")
def home():
    return"hello from flask"

@app.get("/test")
def test():
    return"here is the test page"

@app.get("/api/about")
def about():
    me={"name":"Moses"}
    return json.dumps(me)

products=[]

def fix_id(obj):
    obj["_id"]=str(obj["_id"])
    return obj

@app.post("/api/products")
def saveProducts():
    newItem=request.get_json()
    print(newItem)
    db.products.insert_one(newItem)
    #products.append(newItem)
    return json.dumps(fix_id(newItem))

@app.get("/api/products")
def getProduct():
    return json.dumps(products)

app.run(debug=True)

