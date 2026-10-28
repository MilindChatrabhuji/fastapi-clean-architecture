import uuid
from datetime import datetime
from app.domain.entities.user import User
from app.application.dtos.user_dto import UserCreateDTO, UserResponseDTO

class CreateUserUseCase:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    async def execute(self, dto: UserCreateDTO) -> UserResponseDTO:
        user = User(
            id=str(uuid.uuid4()),
            email=dto.email,
            full_name=dto.full_name,
            is_active=True,
            created_at=datetime.utcnow()
        )
        saved = await self.user_repo.save(user)
        return UserResponseDTO(
            id=saved.id,
            email=saved.email,
            full_name=saved.full_name,
            is_active=saved.is_active,
            created_at=saved.created_at
        )
