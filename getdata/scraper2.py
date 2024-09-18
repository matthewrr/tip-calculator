from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

path = "/Users/matthewr/Library/Application Support/Google/Chrome/Default"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


# chrome_options.add_experimental_option("detach", True)
# service = ChromeService(executable_path="/usr/local/bin/chromedriver")


# options.add_argument(f"user-data-dir=/Users/matthewr/Library/Application Support/Google/Chrome/Default/Default") #)PATH is path to your chrome profile
# options.add_argument(f"user-data-dir={path}")
# w = webdriver.Chrome(service=service, options=options)
w = webdriver.Chrome(options=options)
w.get("https://reddit.com")

# w.implicitly_wait(0.5)





# BEFORE
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(
#     executable_path=CHROMEDRIVER_PATH, 
#     options=options
# )

# AFTER
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# options = webdriver.ChromeOptions()
# service = ChromeService(executable_path=CHROMEDRIVER_PATH)
# driver = webdriver.Chrome(service=service, options=options)

# driver = webdriver.Safari()
# # driver.get("https://manager.union-pos.com/login")
# driver.get("https://manager.union-pos.com/enterprise/dashboard")
# title = driver.title


# driver.implicitly_wait(0.5)





while True:
    pass

