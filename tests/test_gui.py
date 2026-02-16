def test_homepage_loads(page):
    page.goto("https://souderbroder-loan-lab.lovable.app")

    page.wait_for_selector("h1")

    assert page.get_by_role("heading", name="Bil").is_visible()
