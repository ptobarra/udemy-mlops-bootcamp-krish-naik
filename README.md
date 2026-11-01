# Udemy MLOps Bootcamp — Krish Naik

My code and notes from Krish Naik's Udemy course **"Complete MLOps Bootcamp With 10+ End To End ML Projects"**.

The repo follows the course order. It starts with Python fundamentals and data analysis, then moves to the MLOps tooling: Git/GitHub, MLflow experiment tracking, DVC data versioning, Docker, CI/CD with GitHub Actions, and end-to-end ML projects deployed to the cloud.

## Contents

| # | Section | What's inside |
|---|---------|---------------|
| 1 | [Python basics](1-python%20basics/) | Syntax, variables, data types, operators |
| 2 | [Control flow](2-control%20flow/) | Conditional statements, loops |
| 3 | [Data structures](3-Data%20Structures/) | Lists, tuples, sets, dictionaries |
| 4 | [Functions](4-Functions/) | Functions, lambdas, `map`, `filter` |
| 5 | [Modules](5-Modules/) | Imports, the standard library, a sample package with subpackages |
| 6 | [File handling](6-File%20Handling/) | Reading and writing text and binary files, file paths |
| 7 | [Exception handling](7-Exception%20Handling/) | `try` / `except` / `else` / `finally` |
| 8 | [OOP](8-oop/) | Classes, inheritance, polymorphism, encapsulation, abstraction, magic methods, operator overloading, custom exceptions |
| 9 | [Advanced Python](9-AdvancedPythonConcepts/) | Iterators, generators, decorators |
| 10 | [Data analysis](10-Data%20Analysis%20with%20Python/) | NumPy, pandas, data manipulation, reading CSV / Excel / other sources |
| 12 | [Logging](12-Logging%20in%20Python/) | The `logging` module, multiple loggers, logging in an app |
| 13 | [Flask](13-Flask/flask/) | Routing, GET/POST forms, Jinja2 templates, a simple REST API |

More sections will be added as I work through the course.

## Resources

Reference PDFs collected along the way, in [resources/](resources/):

| Date | Document | Topic |
|------|----------|-------|
| 2026-09-17 | [Introduction to MLOps](resources/20260917%20introduction%20to%20mlops.pdf) | What MLOps is and the ML lifecycle |
| 2026-10-24 | [Flask Framework Notes](resources/20261024%20Flask_Framework_Notes.pdf) | Companion notes for section 13 |
| 2026-11-01 | [Git Cheat Sheet](resources/20261101%20git-cheat-sheet-education.pdf) | Common Git commands |

## Setup

The project uses Python 3.10+ and [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
git clone https://github.com/ptobarra/udemy-mlops-bootcamp-krish-naik.git
cd udemy-mlops-bootcamp-krish-naik

# Create .venv and install dependencies (including Jupyter for the notebooks)
uv sync --extra dev
source .venv/bin/activate
```

If you're not using uv, plain `pip` works too:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Usage

**Notebooks:** open any `.ipynb` file in VS Code or Jupyter and select the `.venv` interpreter/kernel:

```bash
jupyter notebook
```

**Flask apps:** run any of the scripts in `13-Flask/flask/` from inside that folder so the templates are found:

```bash
cd 13-Flask/flask
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## License

[MIT](LICENSE)
