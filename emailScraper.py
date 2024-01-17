import time
import re
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_emails(url, output_file):
    # Set up the Chrome WebDriver (replace with the path to your chromedriver executable)
    driver = webdriver.Chrome()

    try:
        # Open the URL in the browser
        driver.get(url)

        # Replace 'num_of_pages' to actual number of pages you want to scrape (e.g 100)
        for i in range(num_of_pages):
            # You may need to adjust the sleep time based on the page content loading time
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(200)


            # Check if there's a "Load More" button
            load_more_button = driver.find_element(By.XPATH, '//span[@class="kQdGHd"]')
            try:
                
                load_more_button.click()
            except:
                pass
            else:
                pass
                

        # Parse the HTML content of the page
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find all text content that matches an email pattern
        email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        emails = re.findall(email_pattern, soup.get_text())

        # Save emails to Excel file
        df = pd.DataFrame({'Email': emails})
        df.to_excel(output_file, index=False)
        print(f"Email addresses saved to {output_file}")

    finally:
        # Close the browser window
        driver.quit()

# Replace 'your_url_here' with the actual URL of the google webpage you want to scrape
# Replace 'output.xlsx' with the desired output Excel file name
scrape_emails('your_url_here', 'output.xlsx')
