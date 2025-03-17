import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
os.makedirs("data", exist_ok=True)

# Setup Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no UI)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the website
url = "http://bookcoverarchive.com/"
driver.get(url)
time.sleep(3)  # Wait for JavaScript to load content

# Extract book details
books = []
book_elements = driver.find_elements(By.CSS_SELECTOR, "article.book_cover")

for book in book_elements:
    title_element = book.find_element(By.TAG_NAME, "a")
    title = title_element.get_attribute("title")
    link = title_element.get_attribute("href")
    
    # Extract background image (cover)
    style = book.find_element(By.TAG_NAME, "style").get_attribute("innerHTML")
    img_url = style.split("background-image:url('")[1].split("');")[0] if "background-image:url('" in style else None
    
    books.append({
        "title": title,
        "link": link,
        "cover_image": img_url,
        "reviews": []
    })

# Save to JSON file
with open("books.json", "w", encoding="utf-8") as f:
    json.dump(books, f, indent=4)

print("Data saved to books.json")

# Close the browser
driver.quit()
