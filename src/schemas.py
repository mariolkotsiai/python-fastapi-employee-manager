from pydantic import BaseModel
from typing import Optional


class EmployeeBase(BaseModel):
    name: str
    email: str
    department: str
    position: str
    salary: float
    is_active: bool = True


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    department: Optional[str] = None
    position: Optional[str] = None
    salary: Optional[float] = None
    is_active: Optional[bool] = None


class EmployeeResponse(EmployeeBase):
    id: int

    class Config:
        from_attributes = True