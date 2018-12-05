"""
Custom WebElement to add additional support
"""
import time

import selenium.webdriver.remote.webelement


class WebElement(selenium.webdriver.remote.webelement.WebElement):
    """
    Custom WebElement class for additional support
    """

    def send_value(self, value, clear=True, human=False):
        """
        Clears the input field before sending the value

        Support human like natural writing to the input element
        """
        if clear:
            self.clear()
        if human:
            for v in value: # pylint: disable=C0103
                self.send_keys(v)
                time.sleep(0.250)
        else:
            self.send_keys(value)
