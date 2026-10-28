from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class UserCreateDTO(BaseModel):
    email: str = Field(..., pattern=r"^[^@]+@[^@]+\.[^@]+$")
    full_name: str

class UserResponseDTO(BaseModel):
    id: str
    email: str
    full_name: str
    is_active: bool
    created_at: Optional[datetime] = None
