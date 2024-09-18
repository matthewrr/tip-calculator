from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
# driver.get("https://manager.union-pos.com/login")
driver.get("https://manager.union-pos.com/enterprise/dashboard")
title = driver.title


driver.implicitly_wait(0.5)

# user_name = driver.find_element(by=By.ID, value="user-email-input")
# password = driver.find_element(by=By.ID, value="user-password-input")

# user_name.send_keys("myemail@gmail.com")

# driver.add_cookie({"name": "foo", "value": "bar"})
# print(driver.get_cookie("foo"))
# "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --remote-debugging-port=9111 --no-first-run --no-default-browser-check --user-data-dir="/Users/YourUsername/Library/Application Support/Google/Chrome"




while True:
    pass








# Get cookie details with named cookie 'foo'


# text = message.text
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
# submit_button.click()
# driver.quit()