from repo.auto_ex.methods.page_base import PageBase
import repo.auto_ex.pages.casino_page as casino_locators
import repo.auto_ex.data.calculator as data_calc
import decimal

pb = PageBase(10)


def test_enter_btc_negative_value():
    pb.navigate_to_page(casino_locators.page_url)  # Precondition 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['btc']  # Precondition 2
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['usd']  # Precondition 3
    pb.fill_input(pb.types['xpath'], casino_locators.inputs['btc'], data_calc.test_values['negative_btc'])  # Step 1
    assert float(pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber')) \
           == (float(data_calc.test_values['negative_btc']))*(float(data_calc.btc_usd_rate))  # Assertion 1


def test_enter_btc_value_0():
    pb.navigate_to_page(casino_locators.page_url)  # Precondition 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['btc']  # Precondition 2
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['usd']  # Precondition 3
    pb.fill_input(pb.types['xpath'], casino_locators.inputs['btc'], data_calc.test_values['zero'])  # Step 1
    assert float(pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber')) \
           == (float(0))  # Assertion 1


def test_enter_btc_value_letters():
    pb.navigate_to_page(casino_locators.page_url)  # Precondition 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['btc']  # Precondition 2
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['usd']  # Precondition 3
    pb.fill_input(pb.types['xpath'], casino_locators.inputs['btc'], data_calc.test_values['letters'])  # Step 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           'NaN'  # Assertion 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['usd']  # Assertion 2


def test_enter_btc_value_space_bar():
    pb.navigate_to_page(casino_locators.page_url)  # Precondition 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['btc']  # Precondition 2
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['usd']  # Precondition 3
    pb.fill_input(pb.types['xpath'], casino_locators.inputs['btc'], data_calc.test_values['space_bar'])  # Step 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           'NaN'  # Assertion 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['usd']  # Assertion 2


def test_enter_btc_value_empty():
    pb.navigate_to_page(casino_locators.page_url)  # Precondition 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['btc']  # Precondition 2
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['usd']  # Precondition 3
    pb.fill_input(pb.types['xpath'], casino_locators.inputs['btc'], data_calc.test_values['empty'])  # Step 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           'NaN'  # Assertion 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['usd']  # Assertion 2


def test_enter_btc_positive_value_7_decimal_places():
    pb.navigate_to_page(casino_locators.page_url)  # Precondition 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['btc']  # Precondition 2
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['usd']  # Precondition 3
    pb.fill_input(pb.types['xpath'], casino_locators.inputs['btc'],
                  str(data_calc.test_values['positive_7_dec']).replace('.', ','))  # Step 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') \
           == str(round(data_calc.test_values['positive_7_dec']*(float(data_calc.btc_usd_rate)), 2))  # Assertion 1


def test_enter_btc_positive_value_8_decimal_places():
    pb.navigate_to_page(casino_locators.page_url)  # Precondition 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['btc']  # Precondition 2
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['usd']  # Precondition 3
    pb.fill_input(pb.types['xpath'], casino_locators.inputs['btc'],
                  str(data_calc.test_values['positive_8_dec']).replace('.', ','))  # Step 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') \
           == str(round(data_calc.test_values['positive_8_dec']*(float(data_calc.btc_usd_rate)), 2))  # Assertion 1


def test_enter_btc_positive_value_9_decimal_places():
    pb.navigate_to_page(casino_locators.page_url)  # Precondition 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['btc']  # Precondition 2
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['usd']  # Precondition 3
    pb.fill_input(pb.types['xpath'], casino_locators.inputs['btc'],
                  str(data_calc.test_values['positive_9_dec']).replace('.', ','))  # Step 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') \
           == str(round(data_calc.test_values['positive_9_dec']*(float(data_calc.btc_usd_rate)), 2))  # Assertion 1


def test_enter_usd_negative_value():
    pb.navigate_to_page(casino_locators.page_url)  # Precondition 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['btc']  # Precondition 2
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['usd']  # Precondition 3
    pb.fill_input(pb.types['xpath'], casino_locators.inputs['usd'], data_calc.test_values['negative_usd'])  # Step 1
    assert float(pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber')) \
           == (float(data_calc.test_values['negative_usd']))/(float(data_calc.btc_usd_rate))  # Assertion 1


def test_enter_usd_value_0():
    pb.navigate_to_page(casino_locators.page_url)  # Precondition 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['btc']  # Precondition 2
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['usd']  # Precondition 3
    pb.fill_input(pb.types['xpath'], casino_locators.inputs['usd'], data_calc.test_values['zero'])  # Step 1
    assert float(pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber')) \
           == (float(0))  # Assertion 1


def test_enter_usd_value_letters():
    pb.navigate_to_page(casino_locators.page_url)  # Precondition 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['btc']  # Precondition 2
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['usd']  # Precondition 3
    pb.fill_input(pb.types['xpath'], casino_locators.inputs['usd'], data_calc.test_values['letters'])  # Step 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           'NaN'  # Assertion 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['btc']  # Assertion 2


def test_enter_usd_value_space_bar():
    pb.navigate_to_page(casino_locators.page_url)  # Precondition 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['btc']  # Precondition 2
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['usd']  # Precondition 3
    pb.fill_input(pb.types['xpath'], casino_locators.inputs['usd'], data_calc.test_values['space_bar'])  # Step 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           'NaN'  # Assertion 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['btc']  # Assertion 2


def test_enter_usd_value_empty():
    pb.navigate_to_page(casino_locators.page_url)  # Precondition 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['btc']  # Precondition 2
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['usd']  # Precondition 3
    pb.fill_input(pb.types['xpath'], casino_locators.inputs['usd'], data_calc.test_values['empty'])  # Step 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           'NaN'  # Assertion 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['btc']  # Assertion 2


def test_enter_usd_positive_value_1_decimal_place():
    pb.navigate_to_page(casino_locators.page_url)  # Precondition 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['btc']  # Precondition 2
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['usd']  # Precondition 3
    pb.fill_input(pb.types['xpath'], casino_locators.inputs['usd'],
                  str(data_calc.test_values['positive_1_dec']).replace('.', ','))  # Step 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') \
           == str(round(decimal.Decimal((data_calc.test_values['positive_1_dec'])/(float(data_calc.btc_usd_rate))), 8))
    # Assertion 1


def test_enter_usd_positive_value_2_decimal_places():
    pb.navigate_to_page(casino_locators.page_url)  # Precondition 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['btc']  # Precondition 2
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['usd']  # Precondition 3
    pb.fill_input(pb.types['xpath'], casino_locators.inputs['usd'],
                  str(data_calc.test_values['positive_2_dec']).replace('.', ','))  # Step 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') \
           == str(round(decimal.Decimal((data_calc.test_values['positive_2_dec'])/(float(data_calc.btc_usd_rate))), 8))
    # Assertion 1


def test_enter_usd_positive_value_3_decimal_places():
    pb.navigate_to_page(casino_locators.page_url)  # Precondition 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['btc']  # Precondition 2
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['usd']).get_attribute('valueAsNumber') == \
           data_calc.page_default_values['usd']  # Precondition 3
    pb.fill_input(pb.types['xpath'], casino_locators.inputs['usd'],
                  str(data_calc.test_values['positive_3_dec']).replace('.', ','))  # Step 1
    assert pb.wd.find_element(pb.types['xpath'], casino_locators.inputs['btc']).get_attribute('valueAsNumber') \
           == str(round(decimal.Decimal((data_calc.test_values['positive_3_dec'])/(float(data_calc.btc_usd_rate))), 8))
    # Assertion 1
    pb.wd.quit()
