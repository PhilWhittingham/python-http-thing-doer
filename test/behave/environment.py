from behave import fixture, use_fixture
from fastapi.testclient import TestClient
from app.main import create_app


@fixture
def app_client(context):
    app = create_app()

    context.client = TestClient(app, raise_server_exceptions=False)
    yield context.client
    app.container.unwire()


def before_feature(context, feature):
    use_fixture(app_client, context)
