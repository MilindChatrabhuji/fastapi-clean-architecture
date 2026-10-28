from typing import Dict, Optional, List
from app.domain.entities.user import User

class InMemoryUserRepository:
    def __init__(self):
        self._storage: Dict[str, User] = {}

    async def save(self, user: User) -> User:
        self._storage[user.id] = user
        return user

    async def get_by_id(self, user_id: str) -> Optional[User]:
        return self._storage.get(user_id)

    async def list_all(self) -> List[User]:
        return list(self._storage.values())
