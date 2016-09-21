from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retreive_it_later(self):
        # Kimani has heard about a to-do lists website
        # To check out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # He is asked to enter a to-do item

        # He types "Buying fish fillets" into a text box

        # When he hits enter, the page updates, and it lists;
        # 1. Buying fish fillets >> as an item in the to do list

        # There is still a text box inviting him to add another item. He 
        # enters "Feed my cat with the fish fillets."

        # The site gives her a link to follow in order to view her list

        #He confirms the url is working
if __name__ == '__main__':
    unittest.main(warnings='ignore')



