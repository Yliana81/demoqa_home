from pages.swag_labs import SwagLabs

def test_check_swag(browser): #

    # перейти на страницу https: // www.saucedemo.com /
    # проверить наличие иконки
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    swag_labs_page.exist_icon()
    assert swag_labs_page.exist_icon()

    # перейти на страницу https: // www.saucedemo.com /
    # проверить наличие поля имени
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    swag_labs_page.find_element('#user-name')

    # перейти на страницу https: // www.saucedemo.com /
    # проверить наличие поля пароля
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    swag_labs_page.find_element('#password')




