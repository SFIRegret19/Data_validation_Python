from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def get_main_page() -> dict:
    return {"message": "Главная страница"}


@app.get("/username/admin")
async def get_admin_page() -> dict:
    return {"message": "Вы вошли как администратор"}

# Annotated в данном случае не обязателен, так как во всех значениях мы указываем Path, если бы мы где-то его не исопльзовали
# нужно было бы его использовать для избежания ошибок

@app.get("/user/{username}/{age}")
async def get_user_info(username: Annotated[str, Path(min_length = 5, max_length=20, description='Enter username', example='UrbanUser')], age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='20')]) -> dict:
    return {"message": f"Информация о пользователе. Имя:{username}, Возраст:{age}"}

@app.get("/username/{user_id}")
async def get_user_by_id(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}