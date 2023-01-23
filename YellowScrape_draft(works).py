import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service               # pip install selenium/pandas
from selenium.webdriver.common.by import By


# Input location & Search   (City, ST) #
SEARCH = input("Search Parameters: ")
STATE = input("State(XY): ")
CITY = input("City: ")
PAGE = int(input("MaxPage Number: "))


# Initialize
s = Service(r'')  # 'PATH' #
browser = webdriver.Chrome(service=s)
browser.implicitly_wait(10)


# Launch #
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
                data.append({'Business': Business[j].text, 'Phone_Number': Phone_Number[j].text})
    except Exception as e:
        print("An error occured: ", e)


# Create File #
df = pd.DataFrame(data)
df.to_csv("", index=False)   # "File Name" #
browser.quit()
print("-----Done-----")