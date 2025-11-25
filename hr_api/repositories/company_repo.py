# repositories/company_repo.py
from .base import InMemoryRepository
from models.company import Company

class CompanyRepository(InMemoryRepository[Company]):
    # pour l'instant rien de plus que le générique
    pass
