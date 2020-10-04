from linkedin_spider import JobSearch, connect
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions

#initialise firefox options
options = FirefoxOptions()
#add cookies on driver
options.add_argument("user-data-dir=selenium")

#initialise driver
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_options=options)

# In order to vire some frofiles LinkedIN will ask you to connect
#email = "your_email"
#password = "yours_password"
#connect.login(driver, email, password)

#Job search use example
jobSearch = JobSearch(linkedin_url="https://www.linkedin.com/jobs/", job_title="Software developer", location="United Kingdom", driver=driver, close_on_complete=False)
