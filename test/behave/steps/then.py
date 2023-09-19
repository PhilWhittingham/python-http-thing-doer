from behave import then


@then("the status code returned is {code:d}")
def assert_status_code_is_200(context, code: int):
    response = context.response

    assert response.status_code == code


@then("the response has successfully counted our first letter {count:d} times")
def assert_character_count(context, count: int):
    response_body = context.response.json()

    assert response_body["count"] == count


@then("the database has {count:d} document in it")
def assert_database_document_count(context, count: int):
    datastore = context.mock_database_client.datastore

    assert len(datastore) == count, len(datastore)
