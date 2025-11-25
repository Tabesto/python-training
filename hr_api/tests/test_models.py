from models.company import Company
from models.employee import Employee
from models.user import User

### Tests for Company model
def test_company_creation():
    company = Company(
        id=1, 
        name="Tabesto", 
        address="Quai Jemmapes, 75010 Paris"
    )

    assert company.id == 1
    assert company.name == "Tabesto"
    assert company.address == "Quai Jemmapes, 75010 Paris"


def test_company_update_fields():
    company = Company(
        id=1,
        name="Tabesto",
        address="Quai Jemmapes, 75010 Paris"
    )

    # Update
    company.address = "174 Quai Jemmapes, 75010 Paris"

    assert company.address == "174 Quai Jemmapes, 75010 Paris"

#### Tests for Employee module
def test_employee_creation():
    emp = Employee(
        id=1,
        first_name="Oliver",
        last_name="Fouquoire",
        company_id=1,
        role="devops",
        active=True,
    )

    assert emp.id == 1
    assert emp.first_name == "Oliver"
    assert emp.last_name == "Fouquoire"
    assert emp.company_id == 1
    assert emp.role == "devops"
    assert emp.active is True

#### Tests for User module
def test_user_creation_with_role():
    usr = User(
        id=2,
        first_name="Charlotte",
        last_name="Guignard",
        company_id=1,
        role="human resources",
        active=False,
    )

    assert usr.id == 2
    assert usr.first_name == "Charlotte"
    assert usr.last_name == "Guignard"
    assert usr.company_id == 1
    assert usr.role == "human resources"
    assert usr.active is False
