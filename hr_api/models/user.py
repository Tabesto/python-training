from dataclasses import dataclass

@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    company_id: int
    role_id: int | None = None
    active: bool = True
    email: str | None = None