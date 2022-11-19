    # -*- coding: utf-8 -*-


from selenium import webdriver
import time
from pytube import YouTube as yt
import os
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By; 

ydl_opts = {} 
playlist=[]   
print(" \t \t \t ****************************************** \t \t \t ") 
print("\t \t \t Welcome to the YouTube PlayList Downloader \t \t \t") 
print(" \t \t \t ****************************************** \t \t \t") 
print("\n \t \t \t \t Made by Vishnu Bhanderi \t \t \t \t \n \n") 


url = input("Enter youtube playlist link to start downloading : ")
Path = input("\nWhere do you want to download this playlist in your system?\nEnter the path : ")
print("\n\n###################################################################################################\n\n") 

if url.find('playlist?list=')!=-1:
    chrome_options = Options()  
    chrome_options.add_argument("--headless")  

    driver = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options)
    driver.get(url)
    time.sleep(5)

    videos=driver.find_elements(By.ID,'video-title')
    for video in videos:
        link=video.get_attribute("href")
        end=link.find("&")
        link=link[:end]
        playlist.append(link)
    driver.close()

elif url.find('watch?v=')!=-1:
    playlist.append(url)


os.chdir(Path) 

for link in playlist:
    vid=yt(link)
    print("--------------------------------")
    print(vid.title+" is Downloading Now !!")
    vid.streams.get_highest_resolution().download()
    print(vid.title+" has been downloaded successfully !!")
    print("--------------------------------")


