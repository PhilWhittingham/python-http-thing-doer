from behave import fixture, use_fixture
from fastapi.testclient import TestClient

from app.routes import app


@fixture
def app_client(context):
    client = TestClient(app, raise_server_exceptions=False)

    context.client = client
    yield context.client


def before_feature(context, feature):
    use_fixture(app_client, context)
