from advanced_alchemy.extensions.litestar import (
    filters,
    service,
    providers
)
from litestar import Controller, get, post, patch, delete
from litestar.params import Parameter, Dependency

from app.domain.users.schemas import UserSchema, UserCreateSchema, UserUpdateSchema
from app.domain.users.service import UserService


class UserController(Controller):
    path = "/users"
    tags = ["Users"]

    dependencies = providers.create_service_dependencies(
        UserService,
        "user_service",
        filters={"id_filter": int, "pagination_type": "limit_offset"},
    )

    @get()
    async def list_users(
            self,
            user_service: UserService,
            filters: list[filters.FilterTypes] = Dependency(skip_validation=True),
    ) -> service.OffsetPagination[UserSchema]:
        """Получить список пользователей."""
        results, total = await user_service.list_and_count(*filters)
        return user_service.to_schema(results, total, filters=filters, schema_type=UserSchema)

    @post(description='Создание пользователя')
    async def create_user(
            self,
            user_service: UserService,
            data: UserCreateSchema,
    ) -> UserSchema:
        """Создать нового пользователя."""
        obj = await user_service.create(data)
        return user_service.to_schema(obj, schema_type=UserSchema)

    @get("/{user_id:int}")
    async def get_user(
            self,
            user_service: UserService,
            user_id: int = Parameter(title="User ID", description="Идентификатор пользователя"),
    ) -> UserSchema:
        """Получить пользователя по ID."""
        obj = await user_service.get(user_id)
        return user_service.to_schema(obj, schema_type=UserSchema)

    @patch("/{user_id:int}")
    async def update_user(
            self,
            user_service: UserService,
            data: UserUpdateSchema,
            user_id: int = Parameter(title="User ID", description="Идентификатор пользователя"),
    ) -> UserSchema:
        """Обновить данные пользователя."""
        obj = await user_service.update(data=data, item_id=user_id, auto_commit=True)
        return user_service.to_schema(obj, schema_type=UserSchema)

    @delete("/{user_id:int}")
    async def delete_user(
            self,
            user_service: UserService,
            user_id: int = Parameter(title="User ID", description="Идентификатор пользователя"),
    ) -> None:
        """Удалить пользователя."""
        await user_service.delete(item_id=user_id)
