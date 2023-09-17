from behave import given


@given("a request in the correct format")
def add_data_to_request(context):
    request = {
        "command": "this is a command"
    }

    context.request = request

@given("a request in the incorrect format")
def add_bad_data_to_request(context):
    request = {
        "not_the_right_format": 100
    }

    context.request = request
