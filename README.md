# 🐍 Pydantic Demo

<div align="center">

```python
# Animated Logo
import time
frames = [
    "  ▄▄▄▄▄▄▄   ",
    " ▐   ▄   ▌  ",
    "  █▄▀  ▀▄█  ",
    "   ▀▀▀▀▀▀   ",
    "  ▄▄▄▄▄▄▄   ",
    " ▐   ▄   ▌  ",
    "  █▄▀  ▀▄█  ",
    "   ▀▀▀▀▀▀   ",
]
for frame in frames:
    print(frame)
    time.sleep(0.1)
```

**A comprehensive demonstration of Pydantic's data validation capabilities**

[![Python](https://img.shields.io/badge/Python-3.14%2B-blue.svg)](https://www.python.org/downloads/)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.13%2B-green.svg)](https://pydantic-docs.helpmanual.io/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.139%2B-red.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 📖 About

This project serves as a comprehensive learning resource for **Pydantic** - a powerful data validation library that uses Python type annotations. Pydantic provides data validation, settings management, and seamless integration with modern Python frameworks.

### What is Pydantic?

Pydantic is a data validation library that allows developers to define data models with type hints. It automatically validates data against those models, ensuring that input data conforms to expected types and constraints. Commonly used in:
- Web development (API design)
- Configuration management
- Data processing pipelines
- Type-safe applications

---

## 🚀 Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.14+ | Core runtime environment |
| **Pydantic** | 2.13.4+ | Data validation & settings management |
| **FastAPI** | 0.139.0+ | Modern web framework for APIs |
| **Pydantic Settings** | 2.14.2+ | Environment-based configuration |
| **Python-dotenv** | 1.2.2+ | Environment variable management |
| **Uvicorn** | 0.51.0+ | ASGI server for FastAPI |

---

## ✨ Features

- **📦 Basic Models**: Learn to create and use Pydantic BaseModel classes
- **🔍 Field Validation**: Use Field() for advanced constraints and descriptions
- **✅ Custom Validators**: Implement field_validator and model_validator
- **🧮 Computed Fields**: Create dynamic properties with @computed_field
- **🔧 Type Safety**: Leverage Python type hints for robust data handling
- **🌐 FastAPI Integration**: Seamless API development with automatic validation
- **⚙️ Settings Management**: Environment-based configuration with pydantic-settings

---

## 📁 Project Structure

```
pydantic-demo/
├── Basic_pydantic/
│   ├── example/           # Example implementations
│   │   └── first_model.py # Comprehensive Pydantic examples
│   ├── assisgment/        # Practice assignments
│   └── solutions/         # Assignment solutions
├── main.py                # Entry point
├── pyproject.toml         # Project dependencies
├── README.md             # This file
└── .venv/                # Virtual environment
```

---

## 🛠️ Installation

### Prerequisites
- Python 3.14 or higher
- UV package manager (recommended)

### Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd pydantic-demo
```

2. **Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
uv sync
# or with pip
pip install -r requirements.txt
```

---

## 💻 Usage

### Running the Main Example

```bash
python main.py
```

### Running Pydantic Examples

```bash
python Basic_pydantic/example/first_model.py
```

### Example Output

```
User Data:
id=101 name='John Doe' is_active=True

Stock Prediction:
id=1 name='Apple' price=189.56 is_stock=True

Cart:
user_id=101 items=['Laptop', 'Mouse'] quantity={'Laptop': 1, 'Mouse': 2}
```

---

## 📚 Learning Path

### 1. Basic Models
Start with simple BaseModel classes to understand the fundamentals.

### 2. Field Validation
Learn to use Field() for constraints like min_length, max_length, gt, etc.

### 3. Validators
Implement custom validation logic with @field_validator and @model_validator.

### 4. Computed Fields
Create dynamic properties that are calculated from other fields.

### 5. Advanced Features
Explore nested models, settings management, and FastAPI integration.

---

## 🎯 Key Concepts Covered

- **BaseModel**: The foundation of Pydantic models
- **Field()**: Advanced field configuration
- **Optional Fields**: Handling nullable data
- **Type Hints**: Leveraging Python's type system
- **Validators**: Custom validation logic
- **Computed Fields**: Dynamic property calculation
- **Settings**: Environment-based configuration

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🔗 Resources

- [Pydantic Documentation](https://docs.pydantic.dev/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

---

<div align="center">

**Built with ❤️ using Pydantic**

</div>
