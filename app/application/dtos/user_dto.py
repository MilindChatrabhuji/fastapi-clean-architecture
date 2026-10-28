from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreateDTO(BaseModel):
    email: EmailStr
    full_name: str

class UserResponseDTO(BaseModel):
    id: str
    email: str
    full_name: str
    is_active: bool
    created_at: Optional[datetime] = None
