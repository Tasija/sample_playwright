import logging
from playwright.sync_api import TimeoutError
from playwright.sync_api import Page
from playwright.sync_api import ConsoleMessage
from playwright.sync_api import Dialog


class BasePage:

    def __init__(self, page: Page, base_url):
        self.page = page
        self.base_url = base_url
        self.timeout = 10000

        def console_handler(message: ConsoleMessage):
            if message.type == 'error':
                logging.error(f'page: {self.page.url}, console error: {message.text}')

        def dialog_handler(dialog: Dialog):
            logging.warning(f'page: {self.page.url}, dialog text: {dialog.message}')
            dialog.accept()

        self.page.on('console', console_handler)
        self.page.on('dialog', dialog_handler)

    loader = '.brand-loader'

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(url=f'{self.base_url}{endpoint}',
                           wait_until="networkidle",
                           timeout=self.timeout)
        else:
            self.page.goto(endpoint)

    def click(self, locator: str):
        self.page.click(locator)

    def fill(self, locator: str, value: str):
        self.page.fill(locator, value)

    def check(self, locator: str):
        self.page.check(locator)

    def uncheck(self, locator: str):
        self.page.check(locator)

    def hover(self, locator: str):
        self.page.hover(locator)

    def type(self, locator: str, text: str):
        self.click(locator)
        self.page.fill(locator, text)

    def select_option(self, locator: str, option: str):
        self.page.select_option(locator, option)

    def is_element_present(self, locator: str) -> bool:
        try:
            self.page.wait_for_selector(locator)
            return True
        except TimeoutError:
            return False

    def find_attribute(self, locator: str, attr_name: str):
        return self.page.locator(locator).get_attribute(attr_name)

    def is_element_hidden(self, locator: str) -> bool:
        try:
            self.page.wait_for_selector(locator, state='hidden')
            return True
        except TimeoutError:
            return False

