# Generic Thing-Doer in Python

A tounge-in-cheek demonstration of a handful of technologies working together to achieve something completely arbitrary.

## Description

An elaborate, over-engineered backend solution for doing a single generic "thing" using an HTTP endpoint.

This project utilises tools and architectures that I have become comfortable with during my time as an engineer. It can be used as a minimal-example for the packages and concepts used. It can be used as a template to build projects that _actually_ do things.

### Built With

* [Python 3.10](https://www.python.org/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Dependency Injector](https://python-dependency-injector.ets-labs.org/)
* [Pytest](https://docs.pytest.org/en/7.4.x/)
* [Behave](https://github.com/behave/behave)
* [Ruff](https://github.com/astral-sh/ruff)
* [Black](https://github.com/psf/black)
* [mypy](https://mypy-lang.org/)


### Concepts Demonstrated

Take these with a pinch of salt, as the "domainstration" may not be particularly in-depth due to the size of the project, but these are the concepts I leverage and have tried to demonstrate here.

Application

* Hexagonal architecture
* Separation of concerns
* Dependency injection

Testing

* Unit testing
* Higher level testing (using behave with Gherkin definitions)
* Mocking dependencies

Behaviours

* Extreme Programming
* Domain Driven Design
* Clean Code and Clean Architecture
* Test Driven Design (TDD)