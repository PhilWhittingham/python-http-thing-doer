from behave import given


@given("a request in the correct format")
def add_data_to_request(context):
    request = {"command": "this is a command"}

    context.request = request


@given("a request where the input is: {request_input}")
def add_specific_data_to_request(context, request_input: str):
    request = {"command": request_input}

    context.request = request


@given("a request in the incorrect format")
def add_bad_data_to_request(context):
    request = {"not_the_right_format": 100}

    context.request = request
