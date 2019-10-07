from bs4 import BeautifulSoup as Bs
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import io


    #variables

search_query=""

#functions

#-------------------------------------------------------
#replaces the spaces in between with "+ "
def convertTheString(word):
    lists = word.split()
    newString=""
    for x in lists:
        newString += x + "+"

    newString = newString[:-1]

    return str(newString)


#-------------------------------------------------------
#creates a Url of searched page of youtube
def createUrl(correctedWord):
    url = ""
    root = "https://www.youtube.com/results?search_query="

    base = convertTheString(search_query)
    # print(base)
    url = str(root) + str(base)
    return url
    # print(url)

#-------------------------------------------------------
# write the file
def NewFileCreate(soup):

    with open("YoutubeData.txt", "w+",encoding="utf-8") as f:
     f.write(soup)
    f.close()
#code

#-------------------------------------------------------
# append the file
def AppendFile(bsoup):
    f = open("YoutubeData.txt", "a+")
    f.write(Bsoup)
    f.close()


# code

# -------------------------------------------------------

# Read the file
def ReadFile(bsoup):
    f = open("YoutubeData.txt", "a+")
    if(f.mode=='r'):
        f.read()

    f.close()


# code

# -------------------------------------------------------



# Automatically opens google and search for youtube
driver = webdriver.Chrome(r"C:\Users\Trupti\PycharmProjects\Youtube automated search for likes\venv\Div\chromedriver.exe");

driver.set_page_load_timeout(15)
print("hello world")
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("https://www.youtube.com/")
driver.find_element_by_name("q").send_keys(Keys.ENTER)
driver.find_element_by_class_name("LC20lb").click()
print("please enter the correct form do y")
search_query=input()
URL = createUrl(search_query)
print(URL+"URL")
driver.find_element_by_name("search_query").send_keys(search_query)
time.sleep(4)
driver.find_element_by_name("search_query").send_keys(Keys.ENTER)




#requesting for the url and obtaining the data
headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
page = requests.get(URL,headers=headers)

Bsoup= Bs(page.content,'html.parser')
#print(Bsoup.prettify())

print((str(Bsoup)))
NewFileCreate(str(Bsoup))
title = Bsoup.find(id="metadata-line")
print(title)
#driver.execute_script("window.open ('https://www.facebook.com/','new window')")

'''

get = urllib.request.urlopen(URL)
html = get.read()


soup = BeautifulSoup(html)
NewFileCreate(soup)

print(soup)
'''
time.sleep(4)




