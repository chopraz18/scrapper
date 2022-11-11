import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time



def scroll_page(wd):
    wd.execute_script("window.scrollTo(0,Math.max(document.body.scrollHeight,document.documentElement.scrollHeight,document.body.offsetHeight,document.documentElement.offsetHeight,document.body.clientHeight,document.documentElement.clientHeight));")
    time.sleep(1)
def webdriver_config():
    try:
        s=Service(r'/chromedriver.dmg')
        wd=webdriver.Chrome(service=s)
    except:
        return "webdriver.exe not available"
    return wd
def video_section(wd,search_url):
    try:
        wd.get(search_url)
        wd.find_element(By.XPATH, "//tp-yt-paper-tab[@tabindex='-1']").click()
        time.sleep(1)
    except Exception as e:
        return e
def fetch_video_url(wd,video_count:int):
    link=[]
    try:
        scroll_page(wd=wd)
        link_elements = wd.find_elements(By.ID, "video-title-link")
        time.sleep(5)
        scroll_page(wd=wd)
        if len(link_elements)>=video_count:
            final_link=link_elements[0:video_count]
            for url_element in final_link:
                url=url_element.get_attribute('href')
                link.append(url)
                time.sleep(1)
        else:
            scroll_page(wd=wd)
    except:
        pass
    return link
def fetch_thumbnail_url(wd,thumbnail_count:int):
    thumbnail_url=[]
    try:
        scroll_page(wd=wd)
        link_elements = wd.find_elements(By.XPATH,"//a[@id='thumbnail']")
        time.sleep(5)
        scroll_page(wd=wd)
        if len(link_elements)>=thumbnail_count:
            final_link=link_elements[0:thumbnail_count]
            for url_element in final_link:
                url=url_element.get_attribute('src')
                thumbnail_url.append(url)
                time.sleep(1)
        else:
            scroll_page(wd=wd)
    except:
        pass
    return thumbnail_url
def get_like_title(wd,url):
    try:
        titles=[]
        likes=[]
        wd.get(url)
        scroll_page(wd=wd)
        like= wd.find_element(By.ID, "segmented-like-button").get_attribute("innerText")
        title=wd.find_element(By.XPATH,"//h1[@class='style-scope ytd-watch-metadata']").get_attribute("innerText")
        titles.append(title)
        likes.append(like)
        time.sleep(5)
    except:
        pass
    return titles,likes
def get_commentor_name(wd):
    wd.execute_script("window.scrollTo(0,600);")
    time.sleep(2)
    wd.execute_script("window.scrollTo(0,600);")
    time.sleep(2)
    name_element= wd.find_elements(By.XPATH, "//a[@id='author-text']")
    comment_element=wd.find_elements(By.XPATH,"//yt-formatted-string[@id='content-text']")
    names=[]
    comments=[]
    for name in name_element:
        name_text=name.text
        names.append(name_text)
    for comment in comment_element:
        comment_text = comment.text
        comments.append(comment_text)

    return names,comments



wd=webdriver_config()
video_section(wd=wd,search_url="https://www.youtube.com/user/krishnaik06/")
urls=fetch_video_url(wd=wd,video_count=3)
titles_all=[]
likes_all=[]
names_all=[]
comments_all=[]
for url in urls:
    titles_all1,likes_all2=get_like_title(wd=wd,url=url)
    names_all1,comments_all1=get_commentor_name(wd=wd)
    titles_all.append(titles_all1)
    likes_all.append(likes_all2)
    names_all.append(names_all1)
    comments_all.append(comments_all1)
print(urls)
print(titles_all)
print(likes_all)
print(names_all)
print(comments_all)



