# playground_repo_company.py

from models.company import Company
from repositories.company_repo import CompanyRepository

def main():
    repo = CompanyRepository()

    c1 = Company(id=0, name="Tabesto", address="Paris")
    created = repo.create(c1)
    print("Created:", created)

    all_companies = repo.list()
    print("List:", all_companies)

    one = repo.get(created.id)
    print("Get:", one)

    created.address = "New address"
    repo.update(created.id, created)
    print("Updated:", repo.get(created.id))

    repo.delete(created.id)
    print("After delete:", repo.list())

if __name__ == "__main__":
    main()
