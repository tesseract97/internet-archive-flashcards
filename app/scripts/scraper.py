
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
import pytesseract
import time
import requests
from io import BytesIO
from flask import current_app

# Configure the webdriver to Chrome
driver = webdriver.Chrome()

#Access the Internet Archive website
driver.get("https://archive.org/account/login")
#sleep to give time to load
time.sleep(3)

#access my Internet Archive credentials from config
username = current_app.config['IA_USERNAME']
password = current_app.config['IA_PASSWORD']

#enter my login credentials
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
username.send_keys(username)  
password.send_keys(password)           
password.send_keys(Keys.RETURN)
time.sleep(5) 

# Navigate to book selected
BOOK_ID = current_app.config['BOOK_ID']
driver.get(f"https://archive.org/details/{BOOK_ID}") 
# Wait for the book to load
time.sleep(5)

# Borrow the book
#TODO: button has dynamic content, so this does not work currently, even adding and managing the wait has not improved
wait = WebDriverWait(driver, 10)
#borrow_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ia-button primary initial']")))
#borrow_button.click()
#time.sleep(10)  

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "BRpagecontainer")))

#Number of pages in the book that I want to scrape
# TODO: replace with function to extract number of pages are dictionary
pages = 1  

for page_num in range(5):
    try:
        # Locate the page image element
        page_img = driver.find_element(By.XPATH, f"//div[@id='IABookReaderWrapper']//img[@class='BRpageimage']")
        # Get the source URL of the image
        img_url = page_img.get_attribute("src")
        
        #Print statements for debugging purposes
        print("img_url: ", img_url)
        print(f"Page {page_num + 1}: {img_url}")
        
        #Download the image using requests
        image_response = requests.get(img_url)
        print("img_response: ", image_response.text)

        #TODO: use OCR to extract text from the image
        #Currently not working, as the image_response.content is text, not image

        #image = Image.open(BytesIO(image_response.content))
        
        # Apply OCR using pytesseract
        #text = pytesseract.image_to_string(image)
        
        #print(f"Text from page {page_num + 1}:\n{text}\n")
        
        # Switch pages (functional)
        next_button = driver.find_element(By.XPATH, "//button[contains(@title, 'Flip right')]")
        next_button.click()
        time.sleep(5)  # Allow time for page to load
    except Exception as e:
        print(f"Error on page {page_num + 1}: {e}")
        continue
# Close the browser
driver.quit()