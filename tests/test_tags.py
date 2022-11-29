import pytest
from assertpy import assert_that, soft_assertions


@pytest.fixture()
def api_result(app_api):
    # Getting response from request that return all tags for dashboard
    return app_api.get_all_tags()


def test_default_tags_displaying(app, api_result):
    # this is example of UI test case
    app.dashboard.goto('/')
    all_tags_on_ui = app.dashboard.get_all_tags_names()
    all_tags_api = api_result['data']['tags']
    with soft_assertions():
        # verifying that result from api matches what is displaying on ui
        assert_that(len(all_tags_on_ui), 'Expected number of tags displayed').is_equal_to(len(all_tags_api))
        assert_that(all_tags_on_ui).is_equal_to(all_tags_api)


def test_get_all_tags_api(api_result):
    assert_that(api_result['status_code']).is_equal_to(200)
    assert_that(api_result['data']['tags']).is_length(10)
