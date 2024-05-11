from repo.auto_ex.methods.page_base import PageBase
import repo.auto_ex.pages.home_page as homepage_locators
import repo.auto_ex.pages.casino_page as casino_locators
import repo.auto_ex.pages.header as header

pb = PageBase(10)


def test_switch_between_homepage_to_casino_page():
    pb.navigate_to_page(homepage_locators.page_url)  # Precondition 1
    pb.click_element('xpath', header.buttons['casino_tab'])  # Step 1
    pb.wait_for_text_to_be_present(pb.types['xpath'], '//h1[text()="New games"]', 'New games')
    assert pb.wd.current_url == casino_locators.page_url  # Assertion 1
    assert pb.wd.find_element(pb.types['xpath'], '//h1[text()="New games"]').is_displayed()  # Assertion 2


def test_switch_between_casino_page_to_homepage():
    pb.navigate_to_page(casino_locators.page_url)  # Precondition 1
    pb.click_element('xpath', header.buttons['home_tab'])  # Step 1
    pb.wait_for_text_to_be_present(pb.types['xpath'], '//main[text()="Something..."]', 'Something...')
    assert pb.wd.current_url == homepage_locators.page_url  # Assertion 1
    assert pb.wd.find_element(pb.types['xpath'], '//main[text()="Something..."]').is_displayed()  # Assertion 2
    pb.wd.quit()
