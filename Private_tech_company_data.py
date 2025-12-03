from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Setup Selenium
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



driver = webdriver.Chrome()
url = "https://finance.yahoo.com/markets/private-companies/highest-valuation/"
driver.get(url)

time.sleep(3)




table = driver.find_element(By.CLASS_NAME, "yf-14a4l34")
tbody = table.find_element(By.TAG_NAME, "tbody")
rows = tbody.find_elements(By.TAG_NAME, "tr")


data = []
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    col_data = [col.text for col in cols]
    data.append(col_data)

print(data)

headers = ["Symbol" , "Company" , "Price" , "52 Week Change %" , "Estimated Valuation" , "Total Funding Raised" , "Latest Funding Date" , "Latest Amount Raised" , "Latest Round Share Class" , "Private Company Sector"]

df = pd.DataFrame(data, columns=headers)
print(df.head)()
# df.to_csv("Private_Companies_valuation_data.csv", index=False)

