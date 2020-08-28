from selenium import webdriver
browser=webdriver.Chrome("D:\\isb2020\\chromedriver.exe")
browser.get('https://www.facebook.com/')
enter credentials
user_id=input("enter the email or phone number:")
password=input("enter the password")
ep=browser.find_element_by_id("email")
ep.send_keys(user_id)
pw=browser.find_element_by_id("pass")
pw.send_keys(password)
login=browser.find_element_by_id("u_0_b")
login.click()
browser.close()
