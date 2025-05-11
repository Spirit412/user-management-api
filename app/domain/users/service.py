from advanced_alchemy.extensions.litestar import service

from app.domain.users.repository import UserRepository


class UserService(service.SQLAlchemyAsyncRepositoryService):
    repository_type = UserRepository
