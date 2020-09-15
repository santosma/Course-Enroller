import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import smtplib


class CunyRegister(object):

    def __init__(self):
        #self.site = "https://cunyfirst.cuny.edu"
        #self.cId = cuny id
        #self.cPass  cuny psw
        #self.eAccount =
        #self.ePass =
        #self.recipient =
        #self.eServer = smtplib.SMTP('smtp.gmail.com', 587)
        self.driver = webdriver.Chrome("C:/Users/Miguel S/Downloads/chromedriver")
        self.enroll_link = "https://hrsa.cunyfirst.cuny.edu/psc/cnyhcprd/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?Page=SSR_SSENRL_CART&Action=A&ACAD_CAREER=UGRD&EMPLID=23467262&ENRL_REQUEST_ID=&INSTITUTION=QNS01&STRM=1196"
        self.enroll_section = "//*[@id='SSR_REGFORM_VW$scroll$0'"

    def find_link_on_site(self, value):
        return WebDriverWait(self.driver, timeout=15).until(EC.presence_of_element_located((By.NAME, "usernameH")))

    def login(self):
        # retrieving site
        self.driver.get(self.site)

        # inputting login
        login = WebDriverWait(self.driver, timeout=15).until(EC.presence_of_element_located((By.NAME, "usernameH")))
        login.send_keys(self.cId)

        # inputting password
        psw = WebDriverWait(self.driver, timeout=15).until(EC.presence_of_element_located((By.NAME, "password")))
        psw.send_keys(self.cPass)

        # Entering info
        psw.send_keys(Keys.ENTER)

    def enroll_list_page(self):
        student_center_link = WebDriverWait(self.driver, timeout=15).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Student Center")))

        student_center_link.click()

        self.driver.get(self.enroll_link)


if __name__ == "__main__":
    # launch registration process
    program = CunyRegister()
    # login to site
    program.login()
    # Go to enrollment page
    program.enroll_list_page()

    #the colleges enrollment link is dynamic and unique based on each account, would require to manual declare link
    #program.do_enrollment()
