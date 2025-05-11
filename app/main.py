# app/main.py
from litestar import Litestar
from advanced_alchemy.extensions.litestar import SQLAlchemyPlugin
from app.config import get_settings
from app.db.session import sqlalchemy_config
from app.domain.users.controllers import UserController
from app.logging_config import get_logger
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin

settings = get_settings()
logger = get_logger()

app = Litestar(
    route_handlers=[UserController],
    plugins=[SQLAlchemyPlugin(config=sqlalchemy_config)],
    debug=settings.DEBUG,
    openapi_config=OpenAPIConfig(
        title="Litestar Example",
        version="0.0.1",
        render_plugins=[SwaggerRenderPlugin()]
    )
)