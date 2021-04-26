import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import csv



def getOnePageJob( driver, writer ):
    jobInfos = driver.find_elements_by_class_name('job-primary')
    for info in jobInfos:
        print( info.text)
        strText = info.text
        arrTxt = strText.split("\n")
        tmp = arrTxt[2].split("-")
        arrTxt.insert( 2, tmp[0] )
        writer.writerow(arrTxt)

url='https://www.zhipin.com/hangzhou/'

driver = webdriver.Chrome()
driver.get(url)

#找到输入框
searchEle = driver.find_element_by_class_name('ipt-search')
searchEle.send_keys('IOS')

#点击搜索按钮
btnSearch = driver.find_element_by_css_selector('button.btn.btn-search')
btnSearch.click()

i =1 
while i < 11 :
    csvfile = open("data.csv", 'a')
    writer = csv.writer(csvfile)

    getOnePageJob(driver,writer)
    i = i + 1
    driver.implicitly_wait(30)
    btnnext = driver.find_element_by_css_selector("a.next")
    btnnext.click()

    csvfile.close()
    


    