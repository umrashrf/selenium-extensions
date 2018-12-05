"""
Generalized browser module for selenium web driver
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from . import settings
from .web_element import WebElement


class Browser(webdriver.Chrome):
    """
    Generalized Browser class

    Defaults: webdriver.Firefox
    """

    _web_element_cls = WebElement

    def __init__(self, *args, **kwargs):
        capabilities = {'browserName': 'chrome',
                        'chromeOptions':  {
                            'useAutomationExtension': False,
                            'forceDevToolsScreenshot': True,
                            'args': ['--start-maximized',
                                     '--disable-infobars']}}
        kwargs.update({'desired_capabilities': capabilities})
        self.timeout = settings.SELENIUM_ELEMENT_TIMEOUT
        super().__init__(*args, **kwargs)

    def css(self, *args, **kwargs):
        """
        Use css library to enable css based selectors
        """
        raise NotImplementedError

    def id(self, id_): # pylint: disable=
        """
        Handy function to find element by id

        Built-in support for waiting for element to be visible
        """
        WebDriverWait(self, self.timeout).until(
            EC.presence_of_element_located((By.ID, id_))
        )
        return self.find_element_by_id(id_)

    def by_name(self, name):
        """
        Handy function to find element by name

        Built-in support for waiting for element to be visible
        """
        WebDriverWait(self, self.timeout).until(
            EC.presence_of_element_located((By.NAME, name))
        )
        return self.find_element_by_name(name)

    def tag_name(self, name):
        """
        Handy function to find element by tag name

        Built-in support for waiting for element to be visible
        """
        WebDriverWait(self, self.timeout).until(
            EC.presence_of_element_located((By.TAG_NAME, name))
        )
        return self.find_element_by_tag_name(name)

    def xpath(self, xpath):
        """
        Handy function to find element by xpath

        Built-in support for waiting for element to be visible
        """
        WebDriverWait(self, self.timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return self.find_element_by_xpath(xpath)

    def xpath_all(self, xpath):
        """
        Handy function to find elements by xpath

        Built-in support for waiting for element to be visible
        """
        WebDriverWait(self, self.timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return self.find_elements_by_xpath(xpath)

    def __exit__(self, *args, **kwargs):
        time.sleep(2)
        super().__exit__(self, *args, **kwargs)
