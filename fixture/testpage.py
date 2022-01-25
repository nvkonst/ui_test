from random import randrange


class TestPage:
    def __init__(self, app):
        self.app = app
        self.url = self.app.base_url

    def open_test_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith('qa.digift.ru'):
            wd.get(self.url)

    def update_value_in_form_by_name(self, name, value):
        wd = self.app.wd
        wd.find_element_by_name(name).click()
        wd.find_element_by_name(name).clear()
        wd.find_element_by_name(name).send_keys(value)

    def activate_checkbox_by_for_attribute(self, attr_value):
        wd = self.app.wd
        wd.find_element_by_css_selector(f'label.checkbox-label[for="{attr_value}"]').click()

    def set_delivery_date(self):
        # нужно доработать - реализовать выбор случайной даты
        wd = self.app.wd
        self.update_value_in_form_by_name("delivery_date", "31.01.2022")
        # действие для закрытия календаря
        wd.find_elements_by_css_selector('.send-form')[1].click()

    def set_delivery_time(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.sendFrom-deliveryTimeField').click()
        intervals = wd.find_elements_by_css_selector('.jq-selectbox__dropdown ul li:not(.disabled)')
        intervals[randrange(len(intervals))].click()

    def fill_in_sender_data(self, sender):
        self.update_value_in_form_by_name("sender_name", sender.name)
        self.update_value_in_form_by_name("sender_lastname", sender.lastname)
        self.update_value_in_form_by_name("sender_email", sender.email)
        self.update_value_in_form_by_name("sender_mobile", sender.mobile)
        self.activate_checkbox_by_for_attribute("sms")
        self.activate_checkbox_by_for_attribute("for_me")

    def fill_in_receiver_data(self, receiver):
        self.update_value_in_form_by_name("receiver_name", receiver.name)
        self.update_value_in_form_by_name("receiver_lastname", receiver.lastname)
        self.update_value_in_form_by_name("receiver_email", receiver.email)
        self.update_value_in_form_by_name("receiver_mobile", receiver.mobile)
        self.set_delivery_date()
        self.set_delivery_time()

    def click_checkout_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('button[name="to_checkout"]').click()
