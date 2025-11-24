from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

# --- Company ---
class CompanyCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    address: Optional[str] = Field(None, max_length=200)
    
class CompanyUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    address: Optional[str] = Field(None, max_length=200)
    
class CompanyRead(BaseModel):
    id: int
    name: str
    address: Optional[str]

# --- User ---
class UserCreate(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    company_id: int
    role_id: Optional[int] = None
    email: Optional[str] = Field(None, max_length=100)
    active: bool = True
    
class UserUpdate(BaseModel):
    first_name: Optional[str] = Field(None, min_length=1, max_length=50)
    last_name: Optional[str] = Field(None, min_length=1, max_length=50)
    company_id: Optional[int] = None
    role_id: Optional[int] = None
    email: Optional[str] = Field(None, max_length=100)
    active: Optional[bool] = None
    
class UserRead(BaseModel):
    id: int
    first_name: str
    last_name: str
    company_id: int
    role_id: Optional[int]
    email: Optional[str]
    active: bool
    
# --- Employee ---
class EmployeeCreate(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    company_id: int
    role_id: Optional[int] = None
    active: bool = True

class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = Field(None, min_length=1, max_length=50)
    last_name: Optional[str] = Field(None, min_length=1, max_length=50)
    company_id: Optional[int] = None
    role_id: Optional[int] = None
    active: Optional[bool] = None
    
class EmployeeRead(BaseModel):
    id: int
    first_name: str
    last_name: str
    company_id: int
    role_id: Optional[int]
    active: bool

# --- Preset ---
class PresetCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=255)
    filter_definition: Dict[str, Any]
    
class PresetUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=255)
    filter_definition: Optional[Dict[str, Any]] = None
    
class PresetRead(BaseModel):
    id: int
    name: str
    description: Optional[str]
    filter_definition: Dict[str, Any]
    
