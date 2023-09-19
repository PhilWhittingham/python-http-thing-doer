from dependency_injector import containers, providers

from app.repository import CharacterCountRepository


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["app.routes"])

    database_client = providers.Factory()  # type: ignore

    count_repository = providers.Factory(
        CharacterCountRepository, client=database_client
    )
