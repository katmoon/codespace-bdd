from .base_element import BaseElement


class Checkbox(BaseElement):
    def __init__(self, browser, label):
        locator = '//label[contains(., "{}")]/' \
                  'preceding::input[@type="checkbox"]'.format(label)
        super(Checkbox, self).__init__(browser, locator)

    def fill(self, value):
    	if value in ('x', 'X', 'v', 'V'):
    		self.click()

