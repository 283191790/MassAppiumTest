import random
import time

from selenium.common.exceptions import NoSuchElementException

from scripts.case_builder import TestInterfaceCase


class CalculatorTest(TestInterfaceCase):

    def setUp(self):
        super(CalculatorTest, self).setUp()

    def tearDown(self):
        super(CalculatorTest, self).tearDown()

    # def test_find_elements(self):
    #
    #     permission_check = self.driver.find_element_by_id('amigo:id/amigo_button1')
    #     if permission_check is not None:
    #         permission_check.click()
    #
    #     time.sleep(3)
    #
    #     basic_key = self.driver.find_element_by_id('com.android.calculator2:id/menu_basic_key')
    #     self.assertIsNotNone(basic_key)

    def test_simple_actions(self):

        permission_check = self.driver.find_element_by_id('amigo:id/amigo_button1')
        if permission_check is not None:
            permission_check.click()

        time.sleep(3)

        equal = self.driver.find_element_by_id('com.android.calculator2:id/basic_key_equal')
        for i in range(100):
            print('Round %s' % str(i+1))

            random_num1 = random.randint(0, 9)
            random_num1_el = self.driver.find_element_by_id(
                'com.android.calculator2:id/basic_key_digit_num%s' % str(random_num1))

            random_num2 = random.randint(0, 9)
            random_nun2_el = self.driver.find_element_by_id(
                'com.android.calculator2:id/basic_key_digit_num%s' % str(random_num2))

            operators = ['add', 'minus', 'multiply']
            # , 'devide']
            operator = random.choice(operators)

            operator_el = self.driver.find_element_by_id('com.android.calculator2:id/basic_key_%s' % operator)

            random_num1_el.click()
            time.sleep(0.5)
            operator_el.click()
            time.sleep(0.5)
            random_nun2_el.click()
            time.sleep(0.5)
            equal.click()
            time.sleep(1)

            if operator == 'add':
                check = random_num1 + random_num2
                print('%s+%s=%s' % (str(random_num1), str(random_num2), str(check)))
            elif operator == 'minus':
                check = random_num1 - random_num2
                if check < 0:
                    check = '−%s' % str(-check)
                print('%s-%s=%s' % (str(random_num1), str(random_num2), str(check)))

            elif operator == 'multiply':
                check = random_num1 * random_num2
                print('%s*%s=%s' % (str(random_num1), str(random_num2), str(check)))
            elif operator == 'devide':
                check = random_num1 / random_num2
                if type(check) == float:
                    check = float('%10f' % check)
                print('%s/%s=%s' % (str(random_num1), str(random_num2), str(check)))

            check_result = self.driver.find_element_by_android_uiautomator('new UiSelector().text("=%s")' % str(check))

            try:
                self.assertIsNotNone(check_result)

            except NoSuchElementException:
                i += 1
                self.driver.get_screenshot_as_file('Error%s.png' % i)
                print('error! Element not found.')


    #
    # def SimpleTests(self):
    #     self.test_find_elements()
    #     self.test_simple_actions()
