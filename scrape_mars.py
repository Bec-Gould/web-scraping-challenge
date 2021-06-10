
import pandas as pd
import os
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

def scrape():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    url1 = 'https://redplanetscience.com/'

    browser.visit(url1)

    soup = bs(browser.html, 'html.parser')

    print(soup.prettify())

    news_title = soup.find("div", class_="content_title").get_text()
    news_title

    news_p = soup.find("div", class_="article_teaser_body").get_text()
    news_p


    url2 = 'https://spaceimages-mars.com/'

    browser.visit(url2)


    html = browser.html
    soup = bs(html, "html.parser")


    relative_image_path = soup.find_all('a')[2]["href"]
    featured_image_url = url2 + relative_image_path
    featured_image_url

    url3 = 'https://galaxyfacts-mars.com/'

    tables = pd.read_html(url3)
    tables


    type(tables)


    df = tables[0]
    # df.head()


    df.columns=["Info","Mars","Earth"]


    df = df.reset_index(drop=True)
    # df.head()


    df = df.iloc[1:]
    print(df)


    html_table = df.to_html(index=False,classes=["table", "table-striped","table-hover"])
  

    url4 = 'https://marshemispheres.com/'
    browser.visit(url4)


    soup = bs(browser.html, 'html.parser')

    title_list = []

    titles = soup.find_all("h3")
    # titles


    for title in titles:
        title_list.append(title.text)
    

    title_list = title_list[0:4]
    # title_list


    hemisphere_image_urls = []


    for title in title_list:
        url4 = 'https://marshemispheres.com/'
        browser.visit(url4)
        browser.click_link_by_partial_text(title)
        html = browser.html
        soup = bs(html, "html.parser")
        image_url = soup.find_all('li')[0].a["href"]
        dict1 = {"title":title, "image_url":url4+ image_url}    
        hemisphere_image_urls.append(dict1)
    
        
        #hemisphere_image_urls
        
    Mars_data = {
    "News_Title": news_title,
    "Paragraph_Text": news_p,
    "Featured_Image": featured_image_url,
    "Facts": html_table,
    "Hemispheres": hemisphere_image_urls
    }

    browser.quit()

    return Mars_data

