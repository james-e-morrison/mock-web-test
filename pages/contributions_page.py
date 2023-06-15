from playwright.sync_api import sync_playwright


class ContributionsPage:
    def __init__(self, page):
        self.page = page

    def change_contribution_value(self, value):
        self.page.fill('input[name="contribution_percentage"]', value)
        self.page.click('button[name="change-contribution"]')

    def change_contribution_percentage(self, value):
        self.page.fill('input[name="contribution"]', value)
        self.page.click('button[name="change-contribution"]')

    def get_contribution_value(self):
        return self.page.get_attribute('input[name="contribution"]', 'value')
    
    def get_contribution_percentage(self):
        return self.page.get_attribute('input[name="contribution_percentage"]', 'value')
