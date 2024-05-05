# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# %%
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.com/")

# %%
try:
     time.sleep(20)
     

     search_dropdown=driver.find_element(By.ID, "searchDropdownBox")
     search_dropdown.click()

     baby_option=driver.find_element(By.XPATH, "//select[@id='searchDropdownBox']/option[text()='Baby']")
     baby_option.click()
     

     search_input=driver.find_element(By.ID, "twotabsearchtextbox") 
     search_input.send_keys("Bag")

     time.sleep(2) 
     
     search_button=driver.find_element(By.ID, "nav-search-submit-button")
     search_button.click()

     Today_deal=driver.find_element(By.XPATH, "//*[@id='nav-xshop']/a[1]")
     Today_deal.click()

     Select_Prime_programs=driver.find_element(By.XPATH, "//*[@id='grid-main-container']/div[2]/span[2]/ul/li[1]/label/input")
     Select_Prime_programs.click()
    
finally:
     time.sleep(2) 
     driver.quit()   


