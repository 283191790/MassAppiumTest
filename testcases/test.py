import time
from scripts.case_builder import TestInterfaceCase


class SimpleAndroidTests(TestInterfaceCase):

    def setUp(self):
        super(SimpleAndroidTests, self).setUp()

    def tearDown(self):
        super(SimpleAndroidTests, self).tearDown()

    def test_find_elements(self):

        permission_check = self.driver.find_element_by_id('amigo:id/amigo_button1')
        if permission_check is not None:
            permission_check.click()

        time.sleep(3)

        plus = self.driver.find_element_by_id('com.android.calculator2:id/basic_key_add')
        self.assertIsNotNone(plus)

    def test_simple_actions(self):

        permission_check = self.driver.find_element_by_id('amigo:id/amigo_button1')
        if permission_check is not None:
            permission_check.click()

        time.sleep(3)

        one = self.driver.find_element_by_id('com.android.calculator2:id/basic_key_digit_num1')

        plus = self.driver.find_element_by_id('com.android.calculator2:id/basic_key_add')

        equal = self.driver.find_element_by_id('com.android.calculator2:id/basic_key_equal')

        for i in range (10):

            one.click()

            plus.click()

            one.click()

            equal.click()

        # TouchAction(self.driver).long_press(equal, 5000).perform()

        check_result = self.driver.find_element_by_android_uiautomator('new UiSelector().text("=2")')

        self.assertIsNotNone(check_result)

    @staticmethod
    def tearDownClass():
        pass

    def SimpleTests(self):
        self.test_find_elements()
        self.test_simple_actions()
