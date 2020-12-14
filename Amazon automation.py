import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import JavascriptException
from selenium.webdriver.common.action_chains import ActionChains 
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys

ignored_exceptions = (NoSuchElementException,StaleElementReferenceException,)
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get('https://www.amazon.com/')
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
item = input(str("Enter the item you want to search: \n".replace('/','')))

# this function takes the above user inputs and searches item and filters it
def find_product(option):
    search = driver.find_element_by_xpath("""/html/body/div[1]
    /header/div/div[1]/div[2]/div/form/div[2]/div[1]/input""").send_keys( option + '\n')

    sort_by = input("""If you want to sort by featured product, press 1. 
    \n If you want to sort by price , press 2. 
    \n If you want to sort by custmer review, press 3.
    \n""")

    driver.implicitly_wait(15)
    wait = WebDriverWait(driver, 10)
    sel = Select(driver.find_element_by_xpath("""/html/body/div[1]/div[2]/span
    /div/span/h1/div/div[2]/div/div/form/span/select"""))

    driver.implicitly_wait(15)
    wait = WebDriverWait(driver, 10) 

    if sort_by == str(1):
        sort_value = sel.select_by_visible_text("Featured")
        time.sleep(0.8)
    elif sort_by == str(2):
        sort_value = sel.select_by_visible_text("Price: Low to High")
        time.sleep(0.8)
    elif sort_by == str(3):
        sort_value = sel.select_by_visible_text("Avg. Customer Review")


        time.sleep(0.8)

def product_click(): # this function clicks on every other image within the results page and clicks items into new tabs to be viewed by user
    
    elems = driver.find_elements_by_xpath("""//img[@src]""")
    i = 1
    cw = driver.current_window_handle
    for elem in elems[i:35:i+5]:    
        try:   
            tw = ActionChains(driver).context_click(elem).key_down(Keys.CONTROL).click(elem).perform()
            time.sleep(0.8)
            i += 2
        except JavascriptException:
            continue

    tabs = driver.window_handles
    return cw, tabs

def review_tabs(result_tab,open_tabs): # this function reviews each tab that is open, scrolls down the page, and closes the tab after each view
    for x in range(len(open_tabs)):
        if open_tabs[x] != result_tab:
            driver.switch_to.window(open_tabs[x])
            driver.execute_script("window.scrollTo (0, 540)")
            time.sleep(1.2)
            driver.close()
        else:
            driver.close()

if __name__ == "__main__": 
    product = find_product(option=item)
    results_page = product_click()
    tab_pages = review_tabs(results_page[0],results_page[1])



