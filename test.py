from django.test import TestCase
from selenium import webdriver

# Create your tests here.
class MyTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    # def test_1(self):
    #     self.assertEqual(1+1, 2)

    def test_2(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Con', self.browser.title)