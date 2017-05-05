from behave import given, when, then, use_step_matcher, Given, When
from hamcrest import assert_that, equal_to
import re
from login_utils import *
import time

@when(u'a user visits the login page')
def visit_login(context):
    context.browser.get(context.server_address + "/login")
    time.sleep(1)


@then(u'she should see the username field')
def see_username_field(context):
    flaskr_found = re.search("Username:", context.browser.page_source, re.IGNORECASE)
    assert flaskr_found

@then(u'she should see the password field')
def see_password_field(context):
    flaskr_found = re.search("Password:", context.browser.page_source, re.IGNORECASE)
    assert flaskr_found


@then(u'she should see the login button')
def see_login_button(context):
    flaskr_found = re.search("Login", context.browser.page_source, re.IGNORECASE)
    time.sleep(0.5)
    assert flaskr_found


@when(u'she logs in with username "{username}" and password "{password}"')
def login(context, username, password):
    context.browser.get(context.server_address + "/login")
    uname = context.browser.find_element_by_name('username')
    passwd = context.browser.find_element_by_name('password')
    login_button = context.browser.find_element_by_name('login')
    uname.clear();
    passwd.clear();
    uname.send_keys(username)
    time.sleep(0.6)
    passwd.send_keys(password)
    time.sleep(1)
    login_button.click()


@then(u'she should see a message of login success')
def see_login_success(context):
    time.sleep(0.4)
    flaskr_found = re.search("login success!", context.browser.page_source, re.IGNORECASE)
    assert flaskr_found



@then(u'she should see a message of login failure')
def see_login_failure(context):
    time.sleep(0.4)
    flaskr_found = re.search("Bad Login", context.browser.page_source, re.IGNORECASE)
    assert flaskr_found

@given(u'a user visits the login page')
def login_page(context):
    context.browser.get(context.server_address + "/login")
    time.sleep(0.4)


@given(u'she sees the Logout link')
def see_logout_link(context):
    flaskr_found = re.search("Log out", context.browser.page_source, re.IGNORECASE)
    assert flaskr_found


@when(u'she clicks on the Logout link')
def click_logout_link(context):
    Logout_found = context.browser.find_element_by_link_text("log out")
    Logout_found.click()


@then(u'she returns to the site')
def visit_site(context):
    pass


@then(u'she sees a message telling her she has logged out')
def see_logout_success(context):
    flaskr_found = re.search("logged out", context.browser.page_source, re.IGNORECASE)
    time.sleep(1)
    assert flaskr_found
