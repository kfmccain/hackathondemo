Feature: Sample Scenario
    An API to handle all of your logging needs

    Scenario: Getting Application ID
        Given I am a Logging user
        And I have an application name
        When I request an application ID
        Then I should get an application ID

    Scenario: Post Info Log Message
        Given I am a Logging user
        Then I have information I want to log
        When I try to log this info
        Then This information should insert into the database

    Scenario: Post Error Log Message
        Given I am a Logging user
        Then I have an error message I want to log
        When I try to log this error
        Then This error should insert into the database

    Scenario: Post Debug Log Message
        Given I am a Logging user
        Then I have a debug message I want to log
        When I try to log this message
        Then This message should insert into the database

    Scenario: Getting Application User Name
        Given I am a Logging user
        Then I have a debug message I want to log
        When I try to log this message
        Then This message should insert into the database