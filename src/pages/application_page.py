class ApplicationPage:
    def __init__(self, page):
        self.page = page

    def fill_personal_information(
        self,
        personal_number,
        first_name,
        last_name,
        email,
        phone,
        address,
        postal_code,
        city
    ):
        self.page.get_by_label("Personnummer").fill(personal_number)
        self.page.get_by_label("Förnamn").fill(first_name)
        self.page.get_by_label("Efternamn").fill(last_name)
        self.page.get_by_label("E-post").fill(email)
        self.page.get_by_label("Telefonnummer").fill(phone)
        self.page.get_by_label("Adress").fill(address)
        self.page.get_by_label("Postnummer").fill(postal_code)
        self.page.get_by_label("Stad").fill(city)

    def click_next(self):
        self.page.get_by_role("button", name="Nästa").click()
