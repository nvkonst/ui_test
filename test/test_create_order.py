import allure


def test_create_order(app):
    sender = app.person.random_person()
    receiver = app.person.random_person()
    with allure.step('Открыть тестовую страницу'):
        app.testpage.open_test_page()
    with allure.step('Пролистать страницу до футера'):
        app.scroll_to_element('.footer')
    with allure.step('Заполнить поля в блоке "От кого" валидными данными'):
        app.testpage.fill_in_sender_data(sender)
    with allure.step('Заполнить поля в блоке "Кому" валидными данными'):
        app.testpage.fill_in_receiver_data(receiver)
    with allure.step('Нажать кнопку "Перейти к оплате"'):
        app.testpage.click_checkout_button()
    with allure.step('Проверка: Открылась страница с адресом: "/checkout/thanks/?Order_ID="'):
        assert '/checkout/thanks/?Order_ID=' in app.current_url()
    with allure.step('Проверка: На странице отображается секция "Заказ оплачен"'):
        assert app.check_unique_element_presence_by_xpath('//div[@class="order-payed"]/div/span[text()="заказ оплачен!"]')
    with allure.step('Проверка: Секция "Заказ оплачен" содержит текст "Ваш подарок уже в пути!"'):
        assert app.check_unique_element_presence_by_xpath('//div[@class="order-payed"]/h1[text()="Ваш подарок уже в пути!"]')
