from fastapi import FastAPI


app = FastAPI()


@app.post("/do-thing")
def do_a_thing_url_command():
    ...
