from behave import *


@when('menu_tab: I click on {tab_name}')
def step_impl(context, tab_name):
    context.home_page.click_on_menu_tab(tab_name)


@then('{page_name}: I verify that the url is "https://www.emag.ro/{url_path}"')
def step_impl(context, url_path, page_name):
    assert context.browser.driver.current_url == "https://www.emag.ro/" + url_path
