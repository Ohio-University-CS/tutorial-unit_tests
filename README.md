# 🧮 Calculator Projects — Python & C++

This repo contains two simple calculator implementations — one in **Python** and one in **C++** — each with their own unit tests and GitHub Actions workflows.

---

## 📁 Project Structure
```
.
├── cpp-unit-test/
│   ├── calculator.cpp
│   ├── calculator.h
│   ├── test_calculator.cpp
│   ├── catch_amalgamated.hpp / .cpp
│   └── main.cpp
└── python-unit-test/
    ├── calculator.py
    ├── test_calculator.py
    └── main.py
```

---

## 🚀 Run the Main Programs

### 🐍 Python
```bash
cd python-unit-test
uv sync
```
```bash
uv run main.py
```
**Usage:**
- Type an operation (`add`, `subtract`, `multiply`, `divide`)
- Enter two numbers
- Type `exit` to quit

**Example:**
```
Enter operation: add
Enter first number: 5
Enter second number: 3
Result: 8.0
```

---

### 🧱 C++
```bash
cd cpp-unit-test
g++ -std=c++17 main.cpp calculator.cpp -o calculator_app
./calculator_app
```
**Usage:**  
Same as Python — type an operation name and numbers interactively.  
Handles divide-by-zero errors gracefully.

---

## 🧪 Run Unit Tests

### Python Tests
```bash
cd python-unit-test
uv sync
source .venv/bin/activate
```
```bash
pytest -v
```
**Options:**
- `-v` → verbose (shows each test)
- `-q` → quiet (only summary)
- `-x` → stop after first failure

---

### C++ Tests
```bash
cd cpp-unit-test
curl -L -o catch_amalgamated.hpp https://github.com/catchorg/Catch2/releases/download/v3.6.0/catch_amalgamated.hpp
curl -L -o catch_amalgamated.cpp  https://github.com/catchorg/Catch2/releases/download/v3.6.0/catch_amalgamated.cpp
```
```bash
g++ -std=c++17 catch_amalgamated.cpp test_calculator.cpp calculator.cpp -o tests
./tests -s -v high
```
**Options:**
- `-s` → show `std::cout` output  
- `-v high` → high verbosity (shows each assertion and section)  
- `--list-reporters` → list available reporters (e.g., `console`, `xml`)  

---

## ⚙️ CI Automation
Both projects include **GitHub Actions** workflows that:
- Automatically build and run tests on every push and pull request  
- Use Python 3.12 and GCC 17 respectively  
- Fail the workflow if any test fails  

---

✅ **Summary**
| Project | Run App | Run Tests | Framework |
|----------|----------|------------|------------|
| Python | `python main.py` | `pytest -v` | pytest |
| C++ | `./calculator_app` | `./tests -s -v high` | Catch2 v3 |
