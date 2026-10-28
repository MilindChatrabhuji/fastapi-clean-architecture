from fastapi import APIRouter, status, Depends
from app.application.dtos.user_dto import UserCreateDTO, UserResponseDTO
from app.application.use_cases.create_user import CreateUserUseCase
from app.infrastructure.repositories.in_memory_user_repo import InMemoryUserRepository

router = APIRouter(prefix="/users", tags=["Users"])
_shared_repo = InMemoryUserRepository()

def get_user_use_case():
    return CreateUserUseCase(_shared_repo)

@router.post("/", response_model=UserResponseDTO, status_code=status.HTTP_201_CREATED)
async def create_user(dto: UserCreateDTO, use_case: CreateUserUseCase = Depends(get_user_use_case)):
    return await use_case.execute(dto)
