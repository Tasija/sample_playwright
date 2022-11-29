from src.pages.DashboardPage import DashboardPage


class WebApplication:

    def __init__(self, driver, url):
        self.default_url = url
        self._driver = driver
        self.context = self._driver.new_context()
        self.context.set_default_timeout(timeout=10000)
        self.page = self.context.new_page()

    def get_driver(self):
        return self._driver

    def quit(self):
        self._driver.quit()

    def close(self):
        self._driver.close()

    def refresh(self):
        self._driver.refresh()

    @property
    def dashboard(self):
        return DashboardPage(self.page, self.default_url)
