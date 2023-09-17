from behave import when


@when("we do a thing")
def post_do_thing(context):
    response = context.client.post("/do-thing")

    context.response = response
