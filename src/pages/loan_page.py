class LoanPage:
    def __init__(self, page):
        self.page = page

    def enter_amount(self, amount):
        self.page.fill("input[name='amount']", str(amount))

    def submit(self):
        self.page.click("button[type='submit']")
