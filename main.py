from selenium import webdriver
import unittest


class DjangoTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_check_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('install', self.browser.title)


if __name__ == '__main__':
    unittest.main()