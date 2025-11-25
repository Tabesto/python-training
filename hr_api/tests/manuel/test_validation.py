from pydantic import ValidationError
from validation.schema import CompanyCreate, EmployeeCreate


def try_company(payload: dict) -> None:
    print(f"\n=== Test CompanyCreate avec: {payload}")
    try:
        obj = CompanyCreate(**payload)
        print("✅ OK :", obj)
    except ValidationError as e:
        print("❌ ValidationError")
        for err in e.errors():
            print(" - loc:", err["loc"], "| msg:", err["msg"], "| type:", err["type"])


def try_employee(payload: dict) -> None:
    print(f"\n=== Test EmployeeCreate avec: {payload}")
    try:
        obj = EmployeeCreate(**payload)
        print("✅ OK :", obj)
    except ValidationError as e:
        print("❌ ValidationError")
        for err in e.errors():
            print(" - loc:", err["loc"], "| msg:", err["msg"], "| type:", err["type"])


def main():
    # Cas valide
    try_company({"name": "Tabesto", "address": "Paris"})
    # Cas invalide (name manquant)
    try_company({"address": "Paris"})

    # Cas valide employé
    try_employee({
        "first_name": "Olivier",
        "last_name": "Fouquoire",
        "company_id": 1,
        "role": "devops",
        "active": True,
    })

    # Cas invalide employé (first_name manquant)
    try_employee({
        "last_name": "Fouquoire",
        "company_id": 1,
        "role": "devops",
    })


if __name__ == "__main__":
    main()
