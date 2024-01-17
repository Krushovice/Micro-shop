import uvicorn
from typing import Union
from pydantic import EmailStr, BaseModel

from fastapi import FastAPI

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def read_root():
    return {"Hello": "Matherfuckers"}


@app.get("/items/")
def read_items():
    return [
        {"id": 1,
         "name": "item1",
         },
        {"id": 2,
         "name": "item2",
         },
        {"id": 3,
         "name": "item3",
         },
    ]


@app.get("/items/{item_id}")
def get_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/users/create/")
def create_user(user: CreateUser):
    return {
        "message": "successs",
        "email": user.email,
    }


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
