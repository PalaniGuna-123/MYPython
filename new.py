from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Open the website
    driver.get("https://concertcraze.netlify.app/") 
    driver.maximize_window()
    time.sleep(2)

    # Step 2: Wait for Sign Up button to be clickable
    signup_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='signBtn']"))
    )
    signup_button.click()
    print("Sign Up button clicked successfully!")

    # Step 3: Fill the form fields
    driver.find_element(By.ID, "username").send_keys("TestUser")
    driver.find_element(By.ID, "email").send_keys("testuser13777999@example.com")
    driver.find_element(By.ID, "password").send_keys("Test@1234")
    driver.find_element(By.ID, "confirm-password").send_keys("Test@1234")

    # Step 4: Click on the Sign Up button
    signup_submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    signup_submit_button.click()
    print("Form submitted, waiting for response...")

    # Step 5: Wait for the page to load after sign-up
    WebDriverWait(driver, 10).until(
        EC.url_changes(driver.current_url)
    )  # Wait for URL to change (indicating successful sign-up redirection)

    # Step 6: Check if redirected to the home page
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "searchBox"))
    )  # Wait until the search bar on the home page is present

    # Verify if we are on the Home Page (you can check for an element that uniquely identifies the home page)
    assert "index.html" in driver.current_url, "Sign Up failed! Didn't navigate to home page."
    print("Sign Up completed successfully and navigated to the Home Page!")

    # Step 7: Now interact with the search bar
    search_box = driver.find_element(By.ID, "searchBox")
    search_box.send_keys("Aniruth")  # Example search query
    search_box.submit()  # Submit the search

    # Wait for search results or confirmation
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "concertCards"))
    )
    print("Search completed successfully!")

except Exception as e:
    print(f"Test failed: {e}")

finally:
    # Close the browser
    driver.quit()
