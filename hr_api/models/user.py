from dataclasses import dataclass

@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    company_id: int
    role: str
    active: bool = True