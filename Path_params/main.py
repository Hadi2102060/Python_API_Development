from fastapi import FastAPI,status
from  enum import Enum
from fastapi.responses import JSONResponse


app = FastAPI()


class Role(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"


# @app.get("/user/{id}")
# async def user(id):
    
#     print(id)

#     return JSONResponse(status_code=200,content={
#         "user": True
#     })

@app.get("/user/{role}")
async def user(role:Role):
    
    if role is role.ADMIN:
        return JSONResponse(status_code=200,content={
        "message": "You are a Admin"
        })
    else:
         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content={
        "message": "Sorry! You are not a Admin"
        })




    

@app.get("/")
async def health():
    return {
        "message":"Hadi"
    }