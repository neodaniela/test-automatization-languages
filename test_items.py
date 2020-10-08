def test_guest_should_see_add_button(browser):
    add_button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert add_button, "Add button not found"
