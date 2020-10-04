from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .objects import Experience, Education, Scraper, Interest, Accomplishment
import os

class JobSummary(object):
    """
    Class which holds and process information about a particular job found on LinkedIn
    """
    linkedin_url = None
    title = None
    description = None
    company = None

    def __init__(self, linkedin_url = None, title = None, description = None):
        self.linkedin_url = linkedin_url
        self.title = title
        self.description = description

    def __repr__(self):
        if self.description == None:
            return """ {title} """.format(title = self.title)
        else:
            return """ {title} {description} """.format(title = self.title, description = self.description)


class JobSearch(Scraper):
    """
        Scrapper which will colect jobs offer found on LinkedIn
    """
    def __init__(self, linkedin_url=None, job_title=None, location=None, company=None, driver=None, get=True, scrape=True, close_on_complete=True):
        self.linkedin_url = linkedin_url
        self.job_title = job_title
        self.location = location
        self.company = company

        self.jobs_found = []

        if driver is None:
            try:
                if os.getenv("CHROMEDRIVER") == None:
                    driver_path = os.path.join(os.path.dirname(
                        __file__), 'drivers/chromedriver')
                else:
                    driver_path = os.getenv("CHROMEDRIVER")

                driver = webdriver.Chrome(driver_path)
            except:
                driver = webdriver.Chrome()

        if get:
            driver.get(linkedin_url)

        self.driver = driver

        if scrape:
            self.scrape(close_on_complete)

    def scrape(self, close_on_complete=True):

        if self.is_signed_in():
            self.scrape_logged_in(close_on_complete=close_on_complete)
        else:
            print('you are not logged in!')
            x = input(
                'please verify the capcha then press any key to continue...')
            self.scrape_not_logged_in(close_on_complete=close_on_complete)

    def scrape_logged_in(self, close_on_complete=True):
        driver = self.driver
        duration = None

        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "global-nav")))
        button = driver.find_element_by_tag_name("button")
        print ("Press button: " + button.get_attribute("class"))
        button.click()

        #driver.execute_script(
        #    "window.scrollTo(0, Math.ceil(document.body.scrollHeight/2));")

        # get jobs
        #try:
        #    _ = WebDriverWait(driver, 3).until(
        #        EC.presence_of_element_located((By.ID, "experience-section")))
        #    exp = driver.find_element_by_id("experience-section")
        #except:
        #    exp = None


        if close_on_complete:
            driver.close()


    def scrape_logged_in(self, close_on_complete=True):
        driver = self.driver
        duration = None

        job_title_box = root.find_element_by_class_name("dismissable-input__input")
        job_title_box.click()
        job_title_box.send_keys(self.job_title)
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(job_title_box, 40, 40)
        action.click()
        action.perform()
        root.click()

        if close_on_complete:
            driver.close()


    def __repr__(self):
        report = ""
        for job in self.jobs_found:
            report += "{title} \n Job Description \n {desc}\n".format(title=self.title, desc=self.desc)

        return report
