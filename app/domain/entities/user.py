from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class User:
    id: str
    email: str
    full_name: str
    is_active: bool = True
    created_at: Optional[datetime] = None
