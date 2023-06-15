import pytest
import pytest_playwright
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_set_contribution_valid(test_data):
    '''test to check user can set a new valid contribution'''

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # Login
        page.goto("https://cushon.com/login")
        login_page = LoginPage(page)
        login_page.login(test_data['username'], test_data['password'])

        # Navigate to contributions page
        page.goto("https://cushon.com/contributions")
        contributions_page = ContributionsPage(page)

        # Test Setup: Change contribution value and reload page
        contributions_page.change_contribution_value('1')
        page.wait_for_load_state()
        expect(new_contribution_value).to_equal('1')

        # Change contribution value and reload page
        contributions_page.change_contribution_value(test_data['new_contribution'])
        page.wait_for_load_state()

        # Check new contribution value
        new_contribution_value = contributions_page.get_contribution_value()
        expect(new_contribution_percentage).to_equal(test_data['contribution_percentage'])
        expect(new_contribution_value).to_equal(test_data['contribution_value'])

        browser.close()

def test_set_contribution_percentage_valid(test_data):
    '''test to check user can set a new valid contribution'''

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # Login
        page.goto("https://cushon.com/login")
        login_page = LoginPage(page)
        login_page.login(test_data['username'], test_data['password'])

        # Navigate to contributions page
        page.goto("https://cushon.com/contributions")
        contributions_page = ContributionsPage(page)

        # Test Setup: Change contribution value and reload page
        contributions_page.change_contribution_value('1')
        page.wait_for_load_state()
        expect(new_contribution_value).to_equal('1')

        # Change contribution value and reload page
        contributions_page.change_contribution_percentage(test_data['contribution_percentage'])
        page.wait_for_load_state()

        # Check new contribution value
        new_contribution_value = contributions_page.get_contribution_value()
        expect(new_contribution_percentage).to_equal(test_data['contribution_percentage'])
        expect(new_contribution_value).to_equal(test_data['contribution_value'])

        browser.close()