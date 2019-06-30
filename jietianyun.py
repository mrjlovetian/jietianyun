#coding=utf-8
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from time import sleep

# 下载
import requests

driver = webdriver.Chrome()
index = 1
while index <= 1000:
    url = 'https://www.ysts8.com/play_17872_55_1_'+ str(index) +'.html'
    driver.get(url)
    sleep(1)
    driver.switch_to.frame("play"); 
    mp3url=driver.find_element_by_xpath('//*[@id="jp_audio_0"]').get_attribute("src")
    print('............', mp3url)
    indexstr = str(index)
    # loval = './{}.mp3'.format(indexstr)
    response = requests.get(mp3url).content
    # urllib.urlretrieve(result, local, cbk)
    f = open('./{}.mp3'.format(indexstr), 'wb')
    f.write(response)
    f.close() 
    index += 1


