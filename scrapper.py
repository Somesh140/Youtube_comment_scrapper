from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
import csv
from utils import read_yaml

#driver = webdriver.Chrome(service=ChromeService(
#    ChromeDriverManager().install()))
#driver = webdriver.Chrome(ChromeDriverManager().install())

from selenium.webdriver.chrome.service import Service

# Set the path to the chromedriver executable 
chrome_path = r"chromedriver.exe"

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Add this line if you want to run Chrome in headless mode

# Create a Service object instead of passing the executable path
service = Service(chrome_path)

# Create the WebDriver instance with the Service and Chrome options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Number of times to scroll down to load more comments
#scroll_down_count = 15
CONFIG=read_yaml("config\config.yaml")

# Load the YouTube video page
driver.get(CONFIG["VIDEO_URL"])  

# Scroll down to load comments (optional)
# Add code here to scroll down the page if the comments are dynamically loaded
last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(2)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Scroll down to load comments (optional)
# Add code here to scroll down the page if the comments are dynamically loaded
#for _ in range(scroll_down_count):
#    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
#    time.sleep(2)

# Get the page source
page_source = driver.page_source

# Close the webdriver
driver.quit()

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Find the comments
comment_elements = soup.find_all('yt-formatted-string', {'id': 'content-text'})
print("Number of comments:", len(comment_elements))

# Store the comments in csv

comments = []
for comment in comment_elements:
    text = comment.text.strip()
    if text:
        comments.append(text)

with open('comment.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Comment'])
    writer.writerows([[comment] for comment in comments])

print("Comments stored in comment.csv file.")