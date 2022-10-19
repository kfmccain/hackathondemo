Feature: Getting Application ID

	@TEST_HD-5
	Scenario: Getting Application ID
		Given I am a Logging user
		And I have an application name
		When I request an application ID
		Then I should get an application ID
