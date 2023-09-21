# Generic Thing-Doer in Python

A tongue-in-cheek demonstration of a handful of technologies working together to achieve something completely arbitrary.

## Description

An elaborate, over-engineered backend solution for doing a single generic "thing" using an HTTP endpoint.

This project utilises tools and architectures that I have become comfortable with during my time as an engineer. It can be used as a minimal-example for the packages and concepts used. It can be used as a template to build projects that _actually_ do things.


## Pre-requisites

`Python 3.10` and `Pipenv` are required to build, run and test.

## Running Instructions

Build the environment using

```pipenv install```<br />
or<br />
```pipenv install --dev```<br />
if running the tests.

Run the tests by running one of<br />
```pipenv run test-static```<br />
```pipenv run test-unit```<br />
```pipenv run test-behave```<br />
for running the static (`ruff`, `black`, `mypy` for styles and types), unit and behave tests respectively.


## Built With

* [Python 3.10](https://www.python.org/)
* [Pipenv](https://pipenv.pypa.io/en/latest/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Pydantic](https://docs.pydantic.dev/latest/)
* [Dependency Injector](https://python-dependency-injector.ets-labs.org/)
* [Pytest](https://docs.pytest.org/en/7.4.x/)
* [Behave](https://github.com/behave/behave)
* [Ruff](https://github.com/astral-sh/ruff)
* [Black](https://github.com/psf/black)
* [mypy](https://mypy-lang.org/)

## Inspired By
[Enterprise Fizzbuzz](https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition) for its humour, but imagine less silliness and more learning.
# Code Walkthrough

Here, I'll explain the code in order to describe the concepts demonstrated. Each section will contain a header, a link to any file I'm refering to and an explanation including links to any external references (these links are available in a section at the bottom too). Often, there will be points of uncertainty or discussion as this design is not intended to be a series of dogmatic rules, but rather choices between many valid options.

## Entry point

[app/main.py](https://github.com/PhilWhittingham/python-http-thing-doer/blob/main/app/main.py)

This entry point of the code includes a pattern called an Application Factory (which is a concept I've borrowed from my use of it in [Flask](https://flask.palletsprojects.com/en/2.3.x/patterns/appfactories/)). 

In the `create_app` function we _could_ define a bunch of app-level settings, but this is mostly used for its synergy with the Dependency Injector pattern (inspiration from the [Python Dependency Injector pattern itself](https://python-dependency-injector.ets-labs.org/examples/fastapi.html)). Simply, we define our `app` and our `container` (containing our depedencies). The initialisation of the `container` '_wires_' itself through config inside the `Container` class (although, arguably this could be moved to here to keep the config in one place).

Finally, we make the `app` globally available which allows us to run the program using some ASGI service ([uvicorn](https://www.uvicorn.org/), etc).

[app/containers.py](https://github.com/PhilWhittingham/python-http-thing-doer/blob/main/app/containers.py)

This file is purely there to define our dependencies using Dependency Injector. They include default instantiations which are the ones which will be used in the live service. Everything defined in this file can be overriden in tests, as will be seen later.

The following sections focus on the conventional [layers](https://en.wikipedia.org/wiki/Multitier_architecture) which I've used here to support appropriate separation of concerns and testibility. 

## API

[app/routes.py](https://github.com/PhilWhittingham/python-http-thing-doer/blob/main/app/routes.py)

In a more expansive project, this file (like most of the files here) could become it's own folder. I've intentionally chosen to not clog the project structure here with superfluous files/folders (keeping [the YAGNI principle](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) in mind while still demonstrating complexity).

Routes is intended to be a few things:
- Functionaly, this is where our FastAPI routes are defined.
- Logically, this is Domain Driven Design "Service" (Services come in many shapes, some good articles on this [here](http://gorodinski.com/blog/2012/04/14/services-in-domain-driven-design-ddd/) and [here](https://enterprisecraftsmanship.com/posts/domain-vs-application-services/)).

While I call this a Service, it's only because there is _some_ conditionality controlling the flow of behaviour (we either compute the result or not based on the data in the database). You could split this logic out into a dedicated "Domain Service" and have this file exist simply to define routes.

We use dependency injection here to allow a dependency to be defined dynamically, and not _inside_ the running code. Leveraging dependency injection allows us to write highly testable code (there's a good article on it [here](https://safjan.com/python-dependency-injection-for-the-testability/)). By defining our dependencies in this way, they are easily overrideable (more on this later).

Ideally, this route function would do as little as possible, but there's a few things I always deem acceptable in moderation:
- Logging: logging here usually allows for clear and simple logging which is directly related to the flow of behaviour in the system. Digging through logs is one thing, but digging for where a log message is defined is another.
- Safe exception handling: here we handle a missing entry in a database. Having this handled here ensures that the flow of the route's logic is in 1 place, not spread between multiple places.

Whenever possible, I try to keep the route functions as simple as possible. Really, all we're doing here is:
1. (Optionally) retrieve some data from a repository.
2. (Optionally) perform some business logic by using domain level functions.
3. (Optionally) save some data to a repository.
4. Return data in an agreed format.

Note three of those are optional, they can be ommitted but rarely should they be rearranged. Ideally they shouldn't be chained either (avoid doing `this` then `that` then `the other` - the function would be definitely doing too much ([Clean Code](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)) and become a maintenance nightmare).


## Domain (Business logic)

[app/domain.py](https://github.com/PhilWhittingham/python-http-thing-doer/blob/main/app/domain.py)

This is where the business logic for our application lives. Ours counts characters present in a string - we define two classes, one to perform the behaviour and one as a return type. We use some nice [Pydantic validation](https://docs.pydantic.dev/latest/usage/validators/) on `CharCount` to ensure that we always create valid objects.


## Repository (Interfacing with an external dependency)

[app/repository.py](https://github.com/PhilWhittingham/python-http-thing-doer/blob/main/app/respository.py)

Our repository class is designed as a way for our service to save the things we want to save. The only thing interesting we do here is to allow for the `client` dependency to be set.


## DTOs (The "display" layer)

[app/dto.py](https://github.com/PhilWhittingham/python-http-thing-doer/blob/main/app/dto.py)

The goal here is to define, in one place, all of the models which our are used to bring data in or send data out from the service. I commonly use the suffix DTO (Data Transfer Object) as a way to visually differentiate them from other models.

Having all of the models defined in one place also allows us to have all of our input validation in one place. Pydantic provides type validation upon object instantiation, and combined with FastAPI (like we do in `routes.py` [here](https://github.com/PhilWhittingham/python-http-thing-doer/blob/60eb71c6141619f35ec56e48e8cadc4f2cc76c0d/app/routes.py#L16C14-L16C14) and [here](https://github.com/PhilWhittingham/python-http-thing-doer/blob/main/app/routes.py#L19)) gives us automatic [422 status code](https://www.abstractapi.com/http-status-codes/422) responses when our inputs aren't valid. As we did in `domains.py`, we can extend the validation on these DTO classes to be more complex as the need arrises.

A final thing to note is that FastAPI can use these models and routes to generate an [OpenAPI specification](https://spec.openapis.org/oas/v3.1.0) (example tutorial [here](https://www.doctave.com/blog/python-export-fastapi-openapi-spec)) which can be used by a number of platforms to run, mock, describe etc our service. This could be done even if the DTO-style models weren't in one place, but it's nicer that they are.

## Other

[app/exceptions.py](https://github.com/PhilWhittingham/python-http-thing-doer/blob/main/app/exceptions.py)

It's my personal preference to 1, minimise the use of custom exceptions where [Python built-ins](https://docs.python.org/3/library/exceptions.html) could be used instead, and 2, keep all custom exceptions in one place - usually with a small note about their intended usage.


## Testing

### Unit testing
I use Pytest for unit testing and attmpt to keep the heirarchy as flat as possible by only writing fully isolated function tests (no test classes) with highly descriptive names in the format

```
def test_function_under_test_input_description_expected_behaviour():
    ...
```

There are a bunch of [variations](https://medium.com/@stefanovskyi/unit-test-naming-conventions-dd9208eadbea) on this pattern, but it mostly contains the same information

I avoid test classes to encourage better isolation (also I find that the terminal output is clearer to read).

### BDD testing

The behave testing is incredibly powerful for testing system-wide behaviour _and_ allowing you to make certain assertions about data-at-rest afterwards (through mocking the database)

## Further reading (links to all sources)

TODO