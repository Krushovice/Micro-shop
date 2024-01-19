import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from items.views import router as items_router
from users.views import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    title = "Мини-магазин Крушовца"
    items = [
        {
            "id": 1,
            "name": "leather coat",
            "price": 30.50,
        },
        {
            "id": 2,
            "name": "red jacket",
            "price": 99.80,
        },
        {
            "id": 3,
            "name": "blue pants",
            "price": 25.13,
        },
    ]
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": title,
            "items": items,
        },
    )


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
