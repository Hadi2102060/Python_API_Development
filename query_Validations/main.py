from fastapi import FastAPI,Query

from typing import Annotated


app = FastAPI()


fake_data : dict[str,list[dict[str,str]]]={

    "items":[
        {"item1": "Apple"},
        {"item2":"Banana"}
    ]

}


# @app.get("/items",tags= ["Items"])
# async def getItem(q:str | None = None):
#     print(q)
#     return {"Hello": "World"}



#............................Qurery validation in some advance(part-1)....................


# @app.get("/items",tags= ["Items"])
# async def getItem(query:str | None = None):
#     print(query)

#     if query:
#         fake_data.update({"New Item":query})

#     return fake_data


#............................Qurery validation in some advance(part-2)....................

@app.get("/items",tags= ["Items"])
async def getItem(query:Annotated[str ,Query(title="Hello WelCome",pattern="hadi",alias="Password",description="All get Description",deprecated=False)]):
    print(query)

    if query:
        fake_data.update({"New Item":query})

    return fake_data


@app.get("/",tags = ["health"])
async def health():
    return {"Hello": " World"}