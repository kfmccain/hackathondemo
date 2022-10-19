@HD-4
Feature: Ad-hoc execution for HD-3

	@TEST_HD-3
	Scenario: Hackathon Demo Test
		Scenario: Getting Application ID
		        Given I am a Logging user
		        And I have an application name
		        When I request an application ID
		        Then I should get an application ID
