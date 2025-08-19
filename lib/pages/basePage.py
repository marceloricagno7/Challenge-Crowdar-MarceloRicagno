import allure
import time

from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorvalue, locatorType):
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver, 30, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        if locatorType == "id":
            element = wait.until(lambda x: x.find_element(By.ID, locatorvalue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element(By.CLASS_NAME, locatorvalue))
            return element
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element(By.XPATH, locatorvalue))
            return element
        elif locatorType == "name":
            element = wait.until(lambda x: x.find_element(By.NAME, locatorvalue))
            return element
        elif locatorType == "css":
            element = wait.until(lambda x: x.find_element(By.CSS_SELECTOR, locatorvalue))
            return element
        elif locatorType == "tag":
            element = wait.until(lambda x: x.find_element(By.TAG_NAME, locatorvalue))
            return element
        elif locatorType == "link":
            element = wait.until(lambda x: x.find_element(By.LINK_TEXT, locatorvalue))
            return element
        elif locatorType == "plink":
            element = wait.until(lambda x: x.find_element(By.PARTIAL_LINK_TEXT, locatorvalue))
            return element
        else:
            print("Locator value " + locatorvalue + "not found")

        return element

    def getElement(self, locatorValue, locatorType):
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
        except:
            print(
                "Element not found with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)
            assert False

        return element

    def clickElement(self, locatorValue, locatorType):
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.click()
        except:
            print(
                "Unable to click on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)
            assert False

    def sendText(self, text, locatorValue, locatorType):
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.send_keys(text)
        except:
            print(
                "Unable to send text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)

    def isDisplayed(self, locatorValue, locatorType):
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.is_displayed()
            return True
        except:
            print(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + " is not displayed")
            self.takeScreenshot(locatorType)
            return False

    def screenShot(self, screenshotName):
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            print("Screenshot save to Path : " + screenshotPath)

        except:
            print("Unable to save Screenshot to the Path : " + screenshotPath)

    def takeScreenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def keyCode(self, value):
        self.driver.press_keycode(value)

    def scrollElement(self, locatorValue, locatorType):
        actions = ActionChains(self.driver)
        try:
            element = self.waitForElement(locatorValue, locatorType)
            actions.move_to_element(element).perform()
            element.click()

        except:
            print("Unable to scroll")

    def getText(self, locatorValue, locatorType):
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            return element.text
        except:
            print(
                "Element not found with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)
            assert False

    def getAttribute(self, locatorValue, locatorType, attribute):
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            text_element = element.get_attribute(attribute)
            return text_element
        except:
            print(
                "Element not found with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)
            assert False
