# content of test_publish_article.py

import logging
from pytest_bdd import scenario, given, when, then
import requests

log = logging.getLogger(__name__)

@scenario('1_HD-5.feature', 'Getting Application ID')
def test_getAppiId():
    pass

@scenario('hackathon_demo.feature', 'Post Info Log Message')
def test_postinfologMes():
    pass

@scenario('hackathon_demo.feature', 'Post Error Log Message')
def test_posterrorLogMes():
    pass

@scenario('hackathon_demo.feature', 'Post Debug Log Message')
def test_post_debug():
    pass


@given("I am a Logging user")
def LoggingUser():
   print("Hello World! Welcome to Python Examples.")
   log.info("Logging User is .. Kurt F. McCain")

@given("I have an application name")
def LoggingApplication():
    log.info("Application Name is qatesterkfmccain ...")

@when("I request an application ID")
def GetApplicationId():
    log.info("Requesting Application ID ... 00932392")

@then("I should get an application ID")
def CheckingForId():
    log.info("Kfmccain Application ID .. 00932392")

@then("I have a debug message I want to log")
def debugMessage():
    log.info("The Debug Message: STOP STOP ...")

@then("I try to log this message")
def tryLogMessage():
    log.info("Trying Log Information ... ")

@then("I have information I want to log")
def infoWantLog():
    log.info("I want to log my name: Kurt Fitzgerald McCain")


@when("I try to log this info")
def trylogthisInfo():
    log.info("Try this: QA Test Cucumber Test")

@then("This information should insert into the database")
def tryinfoInsertData():
    log.info("Insert First Name & Last Name into Database")

@then("I have an error message I want to log")
def errormessageWant():
    log.info("I want to log: STOP INSERT ...")

@when("I try to log this error")
def trylogThisError():
    log.info("I want to try to log this error: Try this again Kurt Fitzgerald McCain")

@then("This error should insert into the database")
def errorInsert():
    log.info("ERROR STOP INSERT ...")

@then("I have a debug message I want to log")
def debugMessageIWant():
    log.info("DEBUG MESSAGE: Please correct INSERT statement")

@when("I try to log this message")
def tryLogMessage():
    log.info("MESSAGE TO TRY: CANCEL INPUT STATEMENT ... KFM")

@then("This message should insert into the database")
def messagetry():
    log.info("Try this in the database")
    x = 2
    assert x == 2
    