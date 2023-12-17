from dependency_injector import containers, providers

from database.database import Database
from repositories.ml import MLRepository
from services.ml import MLService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["routers"]
    )

    config = providers.Configuration(yaml_files=["config.yml"])

    db = providers.Singleton(Database, db_url=config.db.url)

    ml_repository = providers.Factory(
        MLRepository,
        session_factory=db.provided.session,
    )

    ml_service = providers.Factory(
        MLService,
        ml_repository=ml_repository,
    )
