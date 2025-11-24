from dataclasses import dataclass

@dataclass
class Employee:
    id: int
    first_name: str
    last_name: str
    company_id: int
    role_id: int | None = None
    active: bool = True
