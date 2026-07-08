# 📚 Basic Pydantic

<div align="center">

**Learn Pydantic from the ground up**

[![Level](https://img.shields.io/badge/Level-Beginner-green.svg)]()
[![Topic](https://img.shields.io/badge/Topic-Data%20Validation-blue.svg)]()

</div>

---

## 🎯 Overview

This module introduces the fundamental concepts of Pydantic through hands-on examples. Each example demonstrates a specific feature of Pydantic's data validation capabilities.

---

## 📁 Structure

```
Basic_pydantic/
├── example/           # Working examples with explanations
│   └── first_model.py # Comprehensive Pydantic examples
├── assisgment/        # Practice assignments (coming soon)
└── solutions/         # Assignment solutions (coming soon)
```

---

## 🚀 Getting Started

### Run the Examples

```bash
python example/first_model.py
```

---

## 📖 Examples Covered

### 1. Basic User Model
Learn the fundamentals of creating a Pydantic BaseModel with typed fields.

```python
class User(BaseModel):
    id: int
    name: str
    is_active: bool
```

### 2. Stock Prediction Model
Understand default values and optional fields.

```python
class StockPrediction(BaseModel):
    id: int
    name: str
    price: float
    is_stock: bool = True  # Default value
```

### 3. Cart Model
Work with complex types like List and Dict.

```python
class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantity: Dict[str, int]
```

### 4. Optional Fields
Handle nullable data with Optional type hints.

```python
class Optionals(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None
```

### 5. Field Validation
Use Field() for advanced constraints and metadata.

```python
class Employee(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name"
    )
    salary: float = Field(..., gt=10000)
```

### 6. Field Validators
Implement custom validation logic for individual fields.

```python
@field_validator("username")
@classmethod
def username_length(cls, value):
    if len(value) < 4:
        raise ValueError("Username must be at least 4 characters long.")
    return value
```

### 7. Model Validators
Validate relationships between multiple fields.

```python
@model_validator(mode="after")
def password_match(self):
    if self.password != self.confirm_password:
        raise ValueError("Passwords do not match.")
    return self
```

### 8. Computed Fields
Create dynamic properties calculated from other fields.

```python
@computed_field
@property
def total_price(self) -> float:
    return self.price * self.quantity
```

---

## 🎓 Learning Objectives

After completing this module, you will be able to:

- ✅ Create Pydantic models with typed fields
- ✅ Use default values and optional fields
- ✅ Apply field constraints with Field()
- ✅ Implement custom validators
- ✅ Create computed fields
- ✅ Handle complex types (List, Dict, Optional)
- ✅ Understand validation error handling

---

## 💡 Tips

1. **Start Simple**: Begin with basic models before adding validators
2. **Read Error Messages**: Pydantic provides detailed validation errors
3. **Use Type Hints**: Leverage Python's type system for better IDE support
4. **Test Your Models**: Always test with both valid and invalid data

---

## 🔗 Next Steps

- Explore advanced Pydantic features
- Learn about nested models
- Integrate with FastAPI
- Study settings management

---

<div align="center">

**Happy Learning! 🎉**

</div>
