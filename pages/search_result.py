import allure
from selene import have
from selene.support.shared import browser


class SearchResultsPage:
    def __init__(self):
        self.results = browser.all('.search-block-elenent')

    @allure.step("Get search results count")
    def get_results_count(self):
        self.results.should(have.size_greater_than_or_equal(0))
        return len(self.results)




