from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_validator,
    computed_field,
)# type:ignore
from typing import List, Optional, Dict


# ==========================================
# Basic User Model
# ==========================================

class User(BaseModel):
    id: int
    name: str
    is_active: bool


input_data = {
    "id": 101,
    "name": "John Doe",
    "is_active": True,
}

result = User(**input_data)

print("User Data:")
print(result)
print()


# ==========================================
# Stock Prediction Model
# ==========================================

class StockPrediction(BaseModel):
    id: int
    name: str
    price: float
    is_stock: bool = True


stock = StockPrediction(
    id=1,
    name="Apple",
    price=189.56,
)

print("Stock Prediction:")
print(stock)
print()


# ==========================================
# Cart Model
# ==========================================

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantity: Dict[str, int]


cart = Cart(
    user_id=101,
    items=["Laptop", "Mouse"],
    quantity={
        "Laptop": 1,
        "Mouse": 2,
    },
)

print("Cart:")
print(cart)
print()


# ==========================================
# Optional Fields
# ==========================================

class Optionals(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None


post = Optionals(
    title="Pydantic Tutorial",
    content="Learning Optional Fields"
)

print("Optional Field Example:")
print(post)
print()


# ==========================================
# Employee Model with Field()
# ==========================================

class Employee(BaseModel):
    id: int

    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples=["Vishal"]
    )

    department: Optional[str] = "General"

    salary: float = Field(
        ...,
        gt=10000,
        description="Employee Salary"
    )


employee = Employee(
    id=1,
    name="Vishal",
    salary=50000
)

print("Employee:")
print(employee)
print()


# ==========================================
# Field Validator Example
# ==========================================

class UserValidation(BaseModel):
    username: str

    @field_validator("username")
    @classmethod
    def username_length(cls, value):
        if len(value) < 4:
            raise ValueError("Username must be at least 4 characters long.")
        return value


user = UserValidation(username="vishal")

print("Validated User:")
print(user)
print()


# ==========================================
# Model Validator Example
# ==========================================

class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def password_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match.")
        return self


signup = SignupData(
    password="12345678",
    confirm_password="12345678",
)

print("Signup Data:")
print(signup)
print()


# ==========================================
# Computed Field Example
# ==========================================

class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity


product = Product(
    price=499.99,
    quantity=3,
)

print("Product:")
print(product)

print("Total Price:", product.total_price)