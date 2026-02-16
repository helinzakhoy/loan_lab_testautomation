class ResultPage:
    def __init__(self, page):
        self.page = page

    def is_success(self):
        return self.page.locator("text=Success").is_visible()
