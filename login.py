from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from bs4 import BeautifulSoup

username = input("Enter the username: ")
password = input("Enter the password: ")

url = "https://www.iitm.ac.in/viewgrades/"

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = s)

driver.get(url)

driver.find_element_by_name("rollno").send_keys(username)
driver.find_element_by_name("pwd").send_keys(password)
driver.find_element_by_css_selector("input[type=\"submit\" i]").click()

print("LoggedIn Successfully!!")
sleep(1)

driver.get("https://www.iitm.ac.in/viewgrades/studentauth/studpass.php")

#print(driver.find_element_by_xpath("/html/body/center/center/table[1]/tbody/tr[39]/td[2]/b/font").text)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

tags = soup('FRAME')
#for tag in tags:
#    print(tag.get('SRC', None))

input("Press enter to end the program and close the site....")
