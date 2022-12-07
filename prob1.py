from selenium import webdriver
from selenium.webdriver.common.by import By

# path of driver
PATH = 'F:\\rirm\\venv\\lib\\site-packages\\chromedriver_autoinstaller\\108\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=PATH)
driver.maximize_window()


def web_data(url):
    driver.get(url)

    media_xpath = "//*[@id='__next']/div/div[5]/footer/div/div/div[2]"
    contants_xpath = "//*[@id='__next']/div/div[5]/footer/div/div[2]/div[4]/div"

    m_anchor_loc = driver.find_element(By.XPATH, media_xpath)
    m_anchors = m_anchor_loc.find_elements(By.TAG_NAME, 'a')
    for anchor in m_anchors:
        print(anchor.get_attribute('href'))

    c_anchor_loc = driver.find_element(By.XPATH, contants_xpath)
    c_anchors = c_anchor_loc.find_elements(By.TAG_NAME, 'a')
    for anchor in c_anchors:
        print(anchor.text)


web_data("https://ful.io")
