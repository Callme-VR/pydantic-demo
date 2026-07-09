from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str


class Setting(BaseModel):
    app_name: str = "Vishal App"
    admin_email: str = "vishal@gmail.com"


def get_settings():
    print("get_settings() was called")
    return Setting()


@app.get("/settings")
def get_settings_endpoint(setting: Setting = Depends(get_settings)):
    print("Inside endpoint")
    print(setting)
    return setting
