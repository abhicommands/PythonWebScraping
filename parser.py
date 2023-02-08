from selenium import webdriver
from selenium.webdriver.common.by import By

# create a new Firefox browser instance
driver = webdriver.Firefox()

# navigate to the webpage
# driver.get("https://hginj.org/research/index.php?limit=0&limitstart=0&option=com_profileview&view=list&listid=6")
driver.get("https://hginj.org/component/profileview/profile/Abbas,Kinza")

xpath = "//*[@id='userlist']/div[{}]/div[2]/div[1]/a"

# locate all elements that match the xpath
# create an empty list to store the data
data = []

for i in range(1, 400):
    # locate all elements that match the xpath
    elements = driver.find_elements(By.XPATH, xpath.format(i))
    for element in elements:
        # extract the link from the element
        link = element.get_attribute("href")
        data.append(link)
        print(link)

# print the data
#print(data)

# close the browser
driver.quit()

