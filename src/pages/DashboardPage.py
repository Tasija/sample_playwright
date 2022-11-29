from src.pages.BasePage import BasePage


class DashboardPage(BasePage):
    article_preview = 'article-preview'
    tag_item = '[ng-bind="tagName"]'

    def wait_for_dashboard_to_load(self):
        self.page.wait_for_selector(selector=self.article_preview,
                                    timeout=self.timeout,
                                    state='visible')

    def get_all_tags_names(self):
        all_tags = self.page.query_selector_all(self.tag_item)
        return [tag.text_content() for tag in all_tags]


