# 📘 Python - More Classes and Objects

Welcome to the **More Classes and Objects** project from the `holbertonschool-higher_level_programming` repository.  
This directory focuses on deepening understanding of Python's object-oriented programming concepts 🧠🐍.

---

## 📂 Project Structure

| 📄 File              | 📋 Description |
|----------------------|----------------|
| `0-rectangle.py`     | 🧱 Defines an **empty** Rectangle class. |
| `1-rectangle.py`     | ➕ Adds `width` and `height` with **property getters and setters**, including **validation**. |
| `3-rectangle.py`     | 🖼️ Adds `__str__()` to **visually represent** the rectangle using `#`. |
| `5-rectangle.py`     | 🧹 Adds `__del__()` to print **"Bye rectangle..."** when an instance is deleted. |
| `7-rectangle.py`     | 🧩 Adds class attribute `print_symbol` to customize the symbol used in the printed rectangle. |
| `9-rectangle.py`     | 🟪 Adds `@classmethod` `square()` to create a **square** (width == height). |

---

## 🧠 Key Concepts Covered

- Encapsulation using **private attributes** and `@property`
- Class vs instance attributes
- Magic methods like `__str__`, `__repr__`, and `__del__`
- Instance counting with class attribute `number_of_instances`
- Custom print behavior with `print_symbol`
- Static and class methods (`@staticmethod`, `@classmethod`)

---

## ✅ Requirements

- **Python 3**
- No external modules used
- Code follows **PEP8** style guide

---

## 🛠 Usage

Each file defines a `Rectangle` class with increasing functionality.  
You can test them using the provided `main.py` files or by importing and creating rectangle objects yourself.

---

## 🚀 Example

```python
from 9_rectangle import Rectangle

sq = Rectangle.square(5)
print(sq)
# Output:
#####
#####
#####
#####
#####

