from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
try:
    driver.get("https://concertcraze.netlify.app/")  
    driver.maximize_window()
    time.sleep(2)

   
    signup_button = driver.find_element(By.XPATH, "//button[@id='signBtn']")
    signup_button.click()
    print("Sign Up button clicked successfully!")
except Exception as e:
    print("Error:", e)


    driver.find_element(By.ID, "username").send_keys("TestUser")  
    driver.find_element(By.ID, "email").send_keys("testuser@example.com")  
    driver.find_element(By.ID, "password").send_keys("Test@1234")  
    driver.find_element(By.ID, "confirm-password").send_keys("Test@1234")  


    signup_button.click()
    time.sleep(2)


    modal_message = driver.find_element(By.ID, "modalMessage").text
    assert "Registration Successful!" in modal_message, "Sign Up failed!"
    print("Sign Up completed successfully!")

except Exception as e:
    print(f"Test failed: {e}")

finally:

    driver.quit()
