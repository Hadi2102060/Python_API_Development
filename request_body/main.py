from fastapi import FastAPI,status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from Schemas.UserSchema import UserSchema



app = FastAPI()

@app.post("/",tags=["Create User"])
async def store(user:UserSchema)->UserSchema:
    encoded= (jsonable_encoder(user))
    return JSONResponse(status_code=status.HTTP_201_CREATED,content=encoded)
    

@app.get("/",tags=["Create Admin"])

async def index():
    return {"Hello": "World"}