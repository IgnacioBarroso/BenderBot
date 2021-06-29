from selenium import webdriver
from time import sleep

def w2g(search):
        driver = webdriver.Edge(executable_path=r'C:\Users\ignac\OneDrive\Escritorio\Bot Discord\src\navdrivers\msedgedriver.exe')
        driver.get('https://w2g.tv/')
        driver.maximize_window()
        driver.implicitly_wait(15)
        create_sala = driver.find_element_by_xpath('//*[@id="create_room_button"]')
        create_sala.click()
        unlock_sala = driver.find_element_by_xpath('//*[@id="intro-modal"]/div[2]/div')
        unlock_sala.click()
        share = driver.find_element_by_xpath('//*[@id="w2g-top-inviteurl"]/div[2]')
        share.click()
        sleep(2)
        copy_link_part2 = driver.find_element_by_xpath('//*[@id="invite-modal"]/div[2]/div[2]/div[2]/button')
        copy_link_part2.click()
        close_share = driver.find_element_by_xpath('//*[@id="invite-modal"]/div[3]/div')
        close_share.click()
        search_bar = driver.find_element_by_xpath('//*[@id="search-bar-input"]')
        search_bar.send_keys(search)
        search_bar.submit()
        sleep(4)
        select_video = driver.find_element_by_xpath('//*[@id="w2g-search-results"]/div[4]/div/div[1]/img')
        select_video.click()
        sleep(4)
        pause_for_wait = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/div[1]/div[2]/div[2]/a')
        pause_for_wait.click()

