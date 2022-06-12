from appium import webdriver
from selenium.webdriver.common.by import By
import unittest
class TestCalculator(unittest.TestCase):

    def setUp(self):
        desired_capabilities = {
        "deviceName": "pixel_2",
        "platformName": "android",
        "platformVersion": "11",
        "app": "C:\\Users\\Alex\\PycharmProjects\\PythonCalcTest\\apksource\\app-debug.apk",
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_capabilities)
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.ID, 'android:id/button1').click()

    def test_add(self):
        inputFieldLeft = self.driver.find_element(By.ID, 'com.vbanthia.androidsampleapp:id/inputFieldLeft')
        inputFieldRight = self.driver.find_element(By.ID, 'com.vbanthia.androidsampleapp:id/inputFieldRight')
        additionButton = self.driver.find_element(By.ID, 'com.vbanthia.androidsampleapp:id/additionButton')
        resultTextView = self.driver.find_element(By.ID, 'com.vbanthia.androidsampleapp:id/resultTextView')

        inputFieldLeft.send_keys('1236')
        inputFieldRight.send_keys('4587')
        additionButton.click()

        expectedResult = '1236.00 + 4587.00 = 5823.00'
        actualResult = resultTextView.text

        assert expectedResult == actualResult, 'Result should be 5823'

    def test_add1(self):
        inputFieldLeft = self.driver.find_element(By.ID, 'com.vbanthia.androidsampleapp:id/inputFieldLeft')
        inputFieldRight = self.driver.find_element(By.ID, 'com.vbanthia.androidsampleapp:id/inputFieldRight')
        additionButton = self.driver.find_element(By.ID, 'com.vbanthia.androidsampleapp:id/additionButton')
        resultTextView = self.driver.find_element(By.ID, 'com.vbanthia.androidsampleapp:id/resultTextView')

        inputFieldLeft.send_keys('0')
        inputFieldRight.send_keys('1')
        additionButton.click()

        expectedResult = '0.00 + 1.00 = 1.00'
        actualResult = resultTextView.text

        assert expectedResult == actualResult, 'Result should be 1'

    def test_subtract(self):
        inputFieldLeft = self.driver.find_element(By.ID, 'com.vbanthia.androidsampleapp:id/inputFieldLeft')
        inputFieldRight = self.driver.find_element(By.ID, 'com.vbanthia.androidsampleapp:id/inputFieldRight')
        additionButton = self.driver.find_element(By.ID, 'com.vbanthia.androidsampleapp:id/subtractButton')
        resultTextView = self.driver.find_element(By.ID, 'com.vbanthia.androidsampleapp:id/resultTextView')

        inputFieldLeft.send_keys('10')
        inputFieldRight.send_keys('5')
        additionButton.click()

        expectedResult = '10.00 - 5.00 = 5.00'
        actualResult = resultTextView.text

        assert expectedResult == actualResult, 'Result should be 5'

    def test_divison(self):
        inputFieldLeft = self.driver.find_element(By.ID, 'com.vbanthia.androidsampleapp:id/inputFieldLeft')
        inputFieldRight = self.driver.find_element(By.ID, 'com.vbanthia.androidsampleapp:id/inputFieldRight')
        additionButton = self.driver.find_element(By.ID, 'com.vbanthia.androidsampleapp:id/divisionButton')
        resultTextView = self.driver.find_element(By.ID, 'com.vbanthia.androidsampleapp:id/resultTextView')

        inputFieldLeft.send_keys('5')
        inputFieldRight.send_keys('0')
        additionButton.click()

        expectedResult = '5.00 / 0.00 = Infinity'
        actualResult = resultTextView.text

        assert expectedResult == actualResult, 'Result should be Infinity'

    def teardown(self):
        self.driver.quit()

