from app import app, get_gif_info
import requests  # used to get api_link for testing
import unittest


class AppTests(unittest.TestCase):
    # Route testing
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

        # Unit Testing
        def test_get_gif_info(self):
            r = requests.get(api_link)
            result = get_gif_info("dog", r)
            gif_links = list(  # list of dog GIFs returned on website
                            "https://media.tenor.com/images/a644358f5eb467fa1bfe3707cfa1497f/tenor.gif",
                            "https://media.tenor.com/images/bb58375a91f5e1222affc155715fd19e/tenor.gif",
                            "https://media.tenor.com/images/e00c5b2fc80ee6d77172e8173f002136/tenor.gif",
                            "https://media.tenor.com/images/762be6f3ca924c878919116f8c6ff53f/tenor.gif",
                            "https://media.tenor.com/images/8e1ba89e6963e0829d4c53600dd30bde/tenor.gif",
                            "https://media.tenor.com/images/1e22ebf14bf28e4706e99fed11fa7f9f/tenor.gif",
                            "https://media.tenor.com/images/958cb056895f3bf6f1865c22474e1c09/tenor.gif",
                            "https://media.tenor.com/images/083375b79b611d822798ce6c10a54bc0/tenor.gif",
                            "https://media.tenor.com/images/3df9d26d4766677a45b69de3d7d19a05/tenor.gif",
                            "https://media.tenor.com/images/61ef49d8c9215eb47d9939e9ac8197bb/tenor.gif")
            self.assertEqual(result, gif_links)


if __name__ == "__main__":
    unittest.main()
