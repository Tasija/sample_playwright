from pathlib import Path
from datetime import datetime
from pytest import fixture, hookimpl
from pytest_html_reporter import attach
from playwright.sync_api import sync_playwright
from src.application_instance import WebApplication
from src.utils.app_requests import AppAPI


@fixture(scope='session')
def get_playwright():
    """
    returns single instance of playwright itself
    :return:
    """
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope='function')
def get_browser(get_playwright, request):
    browser = request.config.getoption('--browser')
    headless = request.config.getini('headless')
    if headless == 'True':
        headless = True
    else:
        headless = False

    if browser == 'chromium':
        browser_instance = get_playwright.chromium.launch(headless=headless)
    elif browser == 'firefox':
        browser_instance = get_playwright.firefox.launch(headless=headless)
    elif browser == 'webkit':
        browser_instance = get_playwright.webkit.launch(headless=headless)
    else:
        assert False, 'unsupported browser type'

    yield browser_instance
    browser_instance.close()


@fixture(scope='function')
def app(get_browser, request):
    """
    Fixture of playwright for non authorised tests
    """
    base_url = request.config.getini('base_url')
    app = WebApplication(driver=get_browser, url=base_url)
    yield app


@fixture(scope='function')
def app_api(request):
    api_url = request.config.getini('api_url')
    app_api = AppAPI(api_url)
    yield app_api


@hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    # result.when == "setup" >> "call" >> "teardown"
    setattr(item, f'result_{result.when}', result)


@fixture(scope='function', autouse=True)
def make_screenshots(request, app):
    yield
    if request.node.result_call.failed:
        for arg in request.node.funcargs.values():
            if isinstance(arg, WebApplication):
                screenshot_dir = Path(".playwright-screenshots")
                screenshot_dir.mkdir(exist_ok=True)
                screenshot = take_screenshot(app=app, nodeid=request.node.nodeid, path=str(screenshot_dir))
                attach(data=screenshot)


def take_screenshot(app, nodeid, path):
    file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/", "_").replace("::", "__")
    return app.page.screenshot(path=f"{path}/{file_name}", type='png')


def pytest_addoption(parser):
    parser.addoption('--secure', action='store', default='secure.json')
    parser.addoption('--browser', action='store', default='chromium')
    parser.addini('base_url', help='base url of site under test', default='https://demo.realworld.io')
    parser.addini('api_url', help='base url of site under test', default='https://api.realworld.io/api')
    parser.addini('headless', help='run browser in headless mode', default='False')
