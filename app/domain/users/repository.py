from advanced_alchemy.extensions.litestar import repository

from app.db.models import User


class UserRepository(repository.SQLAlchemyAsyncRepository[User]):
    model_type = User
