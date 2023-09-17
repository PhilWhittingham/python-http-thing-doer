from behave import then


@then("the status code returned is a 200")
def assert_status_code_is_200(context):
    response = context.response

    assert response.status_code == 200
