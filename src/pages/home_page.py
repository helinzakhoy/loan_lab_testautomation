class HomePage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://souderbroder-loan-lab.lovable.app")

    def choose_car_loan(self):
        self.page.locator("text=Bil").first.click(force=True)








