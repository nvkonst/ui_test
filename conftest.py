import pytest
from fixture.application import Application


fixture = None


@pytest.fixture
def app():
    global fixture
    browser = "chrome"
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url="http://HR:test@qa.digift.ru")
        # нужно доработать - получать данные из конфига, не задавать хардкодом
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
