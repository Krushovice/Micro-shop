import uvicorn

from fastapi import FastAPI

from items.views import router as items_router
from users.views import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def read_root():
    return {"Hello": "Matherfuckers"}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
