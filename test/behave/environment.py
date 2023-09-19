from behave import fixture, use_fixture
from fastapi.testclient import TestClient
from app.main import create_app
from test.behave.mocks import MockDatabaseClient


@fixture
def mock_database_client(context):
    client = MockDatabaseClient()

    context.mock_database_client = client
    with context.app.container.database_client.override(client):
        yield client


@fixture
def app_client(context):
    app = create_app()

    # Used to overwrite dependencies
    context.app = app
    use_fixture(mock_database_client, context)

    # Used in tests to execute calls
    context.client = TestClient(app, raise_server_exceptions=False)
    yield context.client
    app.container.unwire()


def before_feature(context, feature):
    use_fixture(app_client, context)
