from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from decouple import config
import time

TTV_USER = config('TTV_USER')
TTV_PSWD = config('TTV_PSWD')
OPENAI_KEY = config('OPENAI_KEY')

def login(driver):
  driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button').click()
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'login-username'))).send_keys(TTV_USER)
  driver.find_element(By.ID, 'password-input').send_keys(TTV_PSWD)
  driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[2]/form/div/div[3]/div/button').click()

def get_chat(driver):
  last_msg = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='log']/*[last()]")))
  try:
    user = last_msg.find_element(By.CLASS_NAME, 'chat-author__display-name').text
  except:
    print('uh')
  msg = last_msg.find_element(By.CLASS_NAME, 'text-fragment').text
  return user, msg

def is_question(user, text):
  return None

def request_answer(text):
  return None

def send_msg(driver, text):
  #tbf
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.TAG_NAME, "textarea"))).click().send_keys(text)
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/aside/div/div/div[2]/div/div/section/div/div[6]/div[2]/div[2]/div[2]/div[3]/div/button"))).click()

def main():
  options = webdriver.ChromeOptions()
  options.add_argument("--user-data-dir=C:\\Users\\danie\\AppData\\Local\\Google\\Chrome\\User Data")
  options.add_argument('--profile-directory=Profile 6')
  driver = webdriver.Chrome(options=options)
  driver.get('https://www.twitch.tv/emilyywang')

  #Twitch hates bots
  
  while True:
    user, msg = get_chat(driver)
    print(user, msg)
    if (user == 'Nightbot'):
      send_msg(driver, "what up")
    time.sleep(0.1)

  




  





main()