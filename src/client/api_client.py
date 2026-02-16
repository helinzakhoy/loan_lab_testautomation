import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def create_loan(self, payload):
        return requests.post(
            f"{self.base_url}/partner-loan-api",
            json=payload,
            headers=self.headers
        )

    def get_loan_by_reference(self, reference_number):
        return requests.get(
            f"{self.base_url}/partner-loan-api?reference_number={reference_number}",
            headers=self.headers
        )

    def delete_loan(self, reference_number):
        return requests.delete(
            f"{self.base_url}/partner-loan-api?reference_number={reference_number}",
            headers=self.headers
        )
