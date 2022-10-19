Feature: Getting Application ID - Scenario 1

	#Sample Scenario
	@TEST_DESK-19
	Scenario: Getting Application ID - Scenario 1
		Scenario: Getting Application ID
		        Given I am a Logging user
		        And I have an application name
		        When I request an application ID
		        Then I should get an application ID
