import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action")
    def measure():
        @print_timing("selenium_app_custom_action:view_sheet")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/projects/AANES?selectedItem=app.jxl:sheets")
            page.wait_until_available_to_switch((By.ID, "itsfine-sconnect-iframe"))
            page.wait_until_visible((By.CLASS_NAME, "jxl-table-header-cell"))
            page.return_to_parent_frame()
        sub_measure()
    measure()