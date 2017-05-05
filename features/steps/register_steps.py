from behave import given, when, then, use_step_matcher, Given, When
from hamcrest import assert_that, equal_to
import re
from login_utils import *
import time



@when(u'a user visits the register page')
def visit_register(context):
    context.browser.get(context.server_address + "/register")
    time.sleep(1)


@then(u'she should see the confirm password field')
def see_passwordConfirm_field(context):
    flaskr_found = re.search("Confirm Password:", context.browser.page_source, re.IGNORECASE)
    assert flaskr_found


@then(u'she should see the register button')
def see_register_button(context):
    flaskr_found = re.search("Register", context.browser.page_source, re.IGNORECASE)
    assert flaskr_found


@when(u'she signs up with username "{username}" and email "{email}" and password "{password}" and password1 "{password1}"')
def register(context, username, email, password, password1):
    context.browser.get(context.server_address + "/register")
    uname = context.browser.find_element_by_name('username')
    email1= context.browser.find_element_by_name('email')
    passwd = context.browser.find_element_by_name('password')
    passwd1 = context.browser.find_element_by_name('password1')
    login_button = context.browser.find_element_by_name('signup')
    uname.clear();
    email1.clear();
    passwd.clear();
    passwd1.clear();
    uname.send_keys(username)
    email1.send_keys(email)
    time.sleep(0.6)
    passwd.send_keys(password)
    passwd1.send_keys(password1)
    time.sleep(1)
    login_button.click()


@then(u'she should see a message of Please confirm your password')
def see_register_failure4(context):
    time.sleep(0.4)
    flaskr_found = re.search("Please confirm your password", context.browser.page_source, re.IGNORECASE)
    assert flaskr_found


@then(u'she should see a message of Username or password invalid')
def see_register_failure3(context):
    time.sleep(0.4)
    flaskr_found = re.search("Username or password invalid", context.browser.page_source, re.IGNORECASE)
    assert flaskr_found


@then(u'she should see a message of User name has already existed, please try again')
def see_register_failure1(context):
    time.sleep(0.4)
    flaskr_found = re.search("User name has already existed, please try again", context.browser.page_source, re.IGNORECASE)
    assert flaskr_found


@then(u'she should see a message of Register successfully')
def see_register_success(context):
    time.sleep(0.4)
    flaskr_found = re.search("Register successfully", context.browser.page_source, re.IGNORECASE)
    assert flaskr_found


@When(u'she clicks on the Register link')
def register_page(context):
    register_found = context.browser.find_element_by_link_text("sign up")
    register_found.click()

@then(u'she turns to register page')
def register_page(context):
    pass


