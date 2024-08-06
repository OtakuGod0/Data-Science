from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode for no GUI

# Path to your chromedriver executable
service = Service('/home/otakugod/Downloads/chrome-linux64/chrome')

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open the webpage
    driver.get("https://neb.ntc.net.np/results.php")

    # Wait until the table is present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "table.border-main"))
    )

    # Get page source and parse with BeautifulSoup
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the table
    table = soup.find('table', {'class': 'border-main'})

    # Extract rows from the table
    rows = table.find_all('tr')

    # Iterate over rows and print data
    for row in rows:
        columns = row.find_all('td')
        data = [col.get_text(strip=True) for col in columns]
        print(data)

finally:
    # Close the WebDriver
    driver.quit()
