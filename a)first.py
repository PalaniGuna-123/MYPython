from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://concertcraze.netlify.app/")
print("Open Browser")
title = browser.title
print(title)
