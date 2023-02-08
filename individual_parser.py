from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.chrome.options import ChromeOptions

# create Chrome options
# options = ChromeOptions()
# options.add_argument("-foreground")
# options.add_argument("--private")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--user-data-dir=~/Library/Application\ Support/Google/Chrome/Default')
driver = webdriver.Chrome(chrome_options=chrome_options)

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--remote-debugging-port=9222')
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-extensions')
driver.get("https://dev-ru-hginj.pantheonsite.io/")



# # create a new Chrome browser instance and reuse an existing browser session
# # driver = webdriver.Chrome(options=options, service_log_path='/dev/null')

# # create Chrome options
# # options = Options()
# # options.add_argument("--headless")

# # # create a new Chrome browser instance in headless mode
# # driver = webdriver.Chrome(options=options)
# # Open the file
# with open("/Users/abhinavacharya/Desktop/newtxt.txt", "r") as file:
#     # Read the contents of the file
#     lines = file.readlines()

# # Create an empty list to store the data
# links = []

# list_of_names = []

# # navigate to the webpage
# def run_browser(link):
#     driver.get(link)

#     xpath = "//*[@id=\"main\"]/div[3]/div[1]/h2"
#     elements = driver.find_elements(By.XPATH, xpath)

#     # locate all elements that match the xpath
#     # create an empty list to store the data
#     print(elements[0].text)
#     list_of_names.append(elements[0].text)

# # Iterate through each line of the file
# for line in lines:
#     # Strip newline characters from the line
#     line = line.strip()
#     # Append the line to the links list
#     links.append(line)
#     run_browser(line)

# for item in list_of_names:
#     print(item)

# driver.quit()
