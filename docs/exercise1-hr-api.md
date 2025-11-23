# Exercise 1 - Mini HR Manager

## Objective

Build a Flask backend API to manage companies, roles, users, and employees.

## Features

- **Companies**: Full CRUD operations
- **Roles**: Create, list, and view operations
- **Users**: CRUD operations with role/company association
- **Employees**: CRUD operations with filtering capabilities
- **Presets**: Save and apply JSON-based filters

## Tech Stack

The exercise focuses on the following technologies and concepts (with approximate weight):

- Flask (15%)
- Pydantic (25%)
- JSON/simplejson (35%)
- Cerberus (10%)
- CRUD logic (5%)
- Caching (5%)
- UV/Uvicorn (3%)
- Clean Code (2%)

## Structure

The project should follow this directory structure:

```
hr_api/
├── app.py
├── models/
├── repositories/
├── routes/
├── validation/
└── utils/
```

## Deliverables

- Source code
- Report
- Demo

## Grading

The evaluation will be based on the following criteria:

- **Features**: 40%
- **Validation**: 20%
- **Code quality**: 15%
- **Constraints handling**: 10%
- **Presets**: 10%
- **Demo**: 5%

---

> **Trainer note**: Cache is an objects list in RAM.