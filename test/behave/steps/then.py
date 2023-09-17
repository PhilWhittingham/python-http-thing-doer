from behave import then


@then("the status code returned is {code:d}")
def assert_status_code_is_200(context, code: int):
    response = context.response

    assert response.status_code == code
