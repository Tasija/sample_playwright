from src.utils.helpers import Https


class AppAPI(Https):

    def get_articles_by_tag_name(self, tag_name):
        tags_details = self.get(resource=f'/articles?tag={tag_name}')
        return tags_details

    def get_all_tags(self):
        return self.get(resource='/tags')
