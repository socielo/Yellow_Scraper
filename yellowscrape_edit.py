import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service               # pip install selenium
from selenium.webdriver.common.by import By
import csv
import time

# Input location & Search   (City, ST)
SEARCH = input("Search Parameters: ")
CITY = input("City: ")
STATE = input("State(XY): ")
PAGE = int(input("MaxPage Number: "))

# Initialize
s = Service(r'C:\Users\josep\OneDrive\Desktop\chrome\chromedriver.exe')  # <--PATH
browser = webdriver.Chrome(service=s)
browser.maximize_window()
browser.implicitly_wait(10)

# Launch
data = []
for i in range(PAGE):
    try:
        browser.get(f"https://www.yellowpages.com/search?search_terms={SEARCH}&geo_location_terms={CITY}%2C{STATE}&page={i+1}")
        Business = browser.find_elements(by=By.CSS_SELECTOR, value='.business-name')
        Phone_Number = browser.find_elements(by=By.CSS_SELECTOR, value='.phones.phone.primary')
        if not Business:
            print("No results found.")
        else:
            for j in range(min(len(Business), len(Phone_Number))):
                data.append({'Business Name': Business[j].text, 'Phone Number': Phone_Number[j].text, 'City': CITY,
                             'State': STATE})
    except Exception as e:
        print("An error occured: ", e)

#Save Data
with open("test", "w", newline="") as f:
    fieldnames = ['NY.csv', 'Phone Number', 'City', 'State']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

browser.quit()
print("-----Done-----")