Feature: Do things using the thing doer

    Scenario: The user does a thing
        Given a request in the correct format
        When we do a thing
        Then the status code returned is 200

    Scenario: The user does a thing with the wrong input
        Given a request in the incorrect format
        When we do a thing
        Then the status code returned is 422
    
    Scenario: The user does a specific thing
        Given a request where the input is: this string
        When we do a thing
        Then the status code returned is 200
        And the response has successfully counted our first letter 2 times
        And the database has 1 document in it

    Scenario: The user does a thing which has already been done
        Given a request where the input is: this string
        And a database entry which has character t with a count of 100 for that request
        When we do a thing
        Then the status code returned is 200
        And the response has successfully counted our first letter 100 times
        And the database has 1 document in it