import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
#Scraping each players career data starting with all player list
#then code goes to each players profile and scrape their career data, so 100 different page

#the code is using firefox and related geckodriver for that purpose
#please change the location of the path of your driver
gecko_path = 'C:/Users/Lanzelit/PycharmProjects/geckodriver'
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.headless = False
browser = webdriver.Firefox(options = options, service=ser)

browser.get('https://stathead.com/tiny/tTuxM')
time.sleep(2)
list_data={}
all_profile_urls = []
all_links = browser.find_elements(By.TAG_NAME,'a')
i = 0
#getting the url and appending it to all_profile_urls
for row in all_links:
    if row.get_attribute('rel') == "noopener":
        all_profile_urls.append(row.get_attribute('href'))
        i = i + 1
#number of how many page will be scraped
        if(i == 10):
            break    

j = 0
base_column = 10
#scraping each players career data via iterating all the players url
for row in all_profile_urls:
    browser.get(row)
    time.sleep(1)
#getting the info of the player then put the player's name into to front of the dictionary
    player_name = browser.find_element(By.XPATH, '//*[@id="meta"]/div[2]/h1/span').text
    stats_pullout = browser.find_element(By.CLASS_NAME,"stats_pullout").text
    list_data[j] = {}
    list_data[j]['player_name'] = player_name
#spliting the career stats for result consistency with the other solutions
    player_career = stats_pullout.split("\n")
    incremnt_by = int(len(player_career)/base_column)
    remove_val = 0
    del player_career[remove_val:incremnt_by]
    split_lists = [player_career[x:x+incremnt_by] for x in range(0, len(player_career), incremnt_by)]
    player_career.clear()
#appending the data
    for each_list in split_lists:
        del each_list[1:len(each_list)-1]
        for element in each_list:
            player_career.append(element)
    key_flag = True
    index = 0
    
    for index in range(index,len(player_career),2):
            list_data[j][player_career[index]] = player_career[index + 1]

    print(row)
    j = j + 1
print(list_data)
print("Printing the first 10 player otherwise it taking so much time ")
browser.quit()
