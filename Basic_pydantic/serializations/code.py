from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = Field(default_factory=list)

    model_config = ConfigDict(
        json_encoders={datetime: lambda dt: dt.strftime("%d-%m-%Y %H:%M:%S")}
    )


user = User(
    id=1,
    name="Vishal",
    email="vishal@hc.com",
    createdAt=datetime(2026, 3, 15, 14, 30),
    address=Address(street="Something", city="Jaipur", zip_code="001144"),
    is_active=False,
    tags=["premium", "subscriber"],
)

print(user.model_dump())
print("-" * 40)
print(user.model_dump_json(indent=4))
