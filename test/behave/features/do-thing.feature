Feature: Do things using the thing doer

    Scenario: The user does a thing
        Given a request in the correct format
        When we do a thing
        Then the status code returned is 200

    Scenario: The user does a thing
        Given a request in the incorrect format
        When we do a thing
        Then the status code returned is 422