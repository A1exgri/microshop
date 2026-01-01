from typing import Annotated
from fastapi import FastAPI, Path
import uvicorn
from pydantic import EmailStr, BaseModel
from items_views import router as items_router
from users.views import router as users_router

app = FastAPI()

app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def hello():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
