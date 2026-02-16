import pytest

def test_create_and_get_loan(api):
    payload = {
        "reference_number": "TEST123",
        "amount": 10000,
        "applicant_name": "Helin Test"
    }

    create_response = api.create_loan(payload)
    assert create_response.status_code in [200, 201]

    get_response = api.get_loan_by_reference("TEST123")
    assert get_response.status_code == 200


def test_delete_loan(api):
    payload = {
        "reference_number": "DELETE123",
        "amount": 5000,
        "applicant_name": "Delete Test"
    }

    create_response = api.create_loan(payload)
    assert create_response.status_code in [200, 201]

    delete_response = api.delete_loan("DELETE123")
    assert delete_response.status_code == 200

@pytest.mark.parametrize("amount", [1000, 5000, 20000])
def test_create_loan_with_different_amounts(api, amount):
    payload = {
        "reference_number": f"REF{amount}",
        "amount": amount,
        "applicant_name": "Param Test"
    }

    response = api.create_loan(payload)
    assert response.status_code in [200, 201]
