from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome()
driver.get('http://selfreport.shu.edu.cn/')

username = ""#账号
password = ""#密码
driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)

driver.find_element_by_id("submit").click()
WebDriverWait(driver,1)

driver.find_element_by_id("lnkReportHistory").click()
WebDriverWait(driver, 1)
for i in range(32,0,-1):
    xpath = '//*[@id="Panel1_DataList1"]/ul/li[' + str(i) + ']/a'
    tempXpath = driver.find_element_by_xpath(xpath)
    if "未填报" in tempXpath.text :
        tempXpath.click()
        WebDriverWait(driver, 1)
        try:
            driver.find_element_by_xpath('//*[@id="p1_ChengNuo-inputEl-icon"]').click()  # 我承诺
            driver.find_element_by_xpath('//*[@id="fineui_6-inputEl-icon"]').click()  # 宝山校区
            driver.find_element_by_xpath('//*[@id="fineui_11-inputEl-icon"]').click()  # 宝山校区
            sleep(1)
            driver.find_element_by_xpath('//*[@id="fineui_15-inputEl-icon"]').click()  # 食堂
            driver.find_element_by_xpath('//*[@id="fineui_19-inputEl-icon"]').click()  # 在上海
            sleep(1)
            driver.find_element_by_xpath('//*[@id="fineui_21-inputEl-icon"]').click()  # 住校
            driver.find_element_by_xpath('//*[@id="p1_ddlXian-inputEl"]').send_keys("宝山区")  # 宝山区
            driver.find_element_by_xpath('//*[@id="p1_XiangXDZ-inputEl"]').send_keys("上海大学宝山校区")

            driver.find_element_by_xpath('//*[@id="fineui_25-inputEl-icon"]').click()#否
            driver.find_element_by_xpath('//*[@id="fineui_27-inputEl-icon"]').click()#否

            driver.find_element_by_xpath('//*[@id="p1_ctl00_btnSubmit"]/span/span').click()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="fineui_46"]/span/span').click()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="fineui_51"]/span/span').click()

            driver.find_element_by_id("lnkReportHistory").click()
            WebDriverWait(driver, 1)
        except NoSuchElementException:
            driver.find_element_by_xpath('//*[@id="ctl03_ctl00_btnReturn"]/span/span').click()
    else:
        continue
driver.close()