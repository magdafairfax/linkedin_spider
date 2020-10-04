import unittest
from linkedin_spider import JobSearch
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class JobSearchCase(unittest.TestCase):
    def setUp(self):
        #initialise firefox options
        options = FirefoxOptions()
        #add cookies on driver
        options.add_argument("user-data-dir=selenium")
        #initialise driver
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_options=options)

        self.jobSearch = JobSearch(linkedin_url="https://www.linkedin.com/jobs/", job_title="Software developer", location="United Kingdom", driver=driver)

    def test_job_search(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
