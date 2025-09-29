from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_form_multi_language(browser):
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, "form[id='add_to_basket_form']>button")