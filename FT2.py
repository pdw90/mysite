import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):  # (1)
    def setUp(self):  # (2)
        self.browser = webdriver.Firefox()  # (4)
        self.browser.implicitly_wait(3)

    def tearDown(self):  # (3)
        self.browser.quit()

    def test_can_start_a_todo_list(self):  # (4)
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get("http://localhost:8000")  # (4)

        # She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)  # (5)

        # She is invited to enter a to-do item straight away
        self.fail("Finish the test!")  # (6)

        [...]

        # Satisfied, she goes back to sleep


if __name__ == "__main__":  # (7)
    unittest.main()  # (7)
