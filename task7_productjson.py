import json
from tabulate import tabulate 

products=[
    {"productname":"Laptop","price":150000,"quantity":10},
    {"productname":"Keyboard","price":1000,"quantity":15},
    {"productname":"Mouse","price":1500,"quantity":20}
]
with open("productdetails.json","w") as file:
    headers = ["productame","price","quantity"]
    table = [[p["productname"], p["price"], p["quantity"]] for p in products]

    json.dump(products,file,indent=4)
    print(tabulate(table,headers,tablefmt=""))