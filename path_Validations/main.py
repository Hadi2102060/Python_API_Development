from fastapi import FastAPI,Path,status,Query

from fastapi.responses import JSONResponse
from typing import Annotated


app = FastAPI()


@app.get("/product/{id}",tags=["This is path validation "])
async def getUser(id: Annotated[int,Path(title="User id",ge=0,le=10)],password:Annotated[str | None,Query(alias="Your password",description="Password Section")]):
    result = {
        "id":1
    }

    if id and password:
        result.update({"Path":id,"password":password})
    return JSONResponse(status_code=200,content=result)

@app.get("/")
async def user():

    return {"Hello ": "Hadi"}