from behave import given


@given("a request in the correct format")
def add_data_to_request(context):
    request = {
        "command": "this is a command"
    }

    context.request = request
