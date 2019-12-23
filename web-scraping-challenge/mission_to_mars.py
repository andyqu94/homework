#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import datetime as dt


def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)
browser = init_browser()

def mars_news(browser):
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    soup = bs(browser.html, 'html.parser')
    news_title = soup.find("div", class_="content_title").text
    news_p =soup.find("div", class_ ="article_teaser_body").text
    return news_title,news_p

def featured_image(browser):
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)
    full_image = browser.find_by_id("full_image")
    full_image.click()
    more_info = browser.links.find_by_partial_text("more info")
    more_info.click()
    html = browser.html
    image_soup = bs(html, "html.parser")
    img_url = image_soup.select_one("figure.lede a img").get("src")
    img_url = f"https://www.jpl.nasa.gov{img_url}"
    return img_url


# # Mars Weather
# 
def mars_weather(browser):
    mars_weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(mars_weather_url)
    html = browser.html
    weather_soup = bs(html, "html.parser")
    mars_weather_info = weather_soup.find("p", "tweet-text").get_text()
    return mars_weather_info


# # Mars Facts

def mars_facts():
    mars_fact_url = "https://space-facts.com/mars/"
    df = pd.read_html(mars_fact_url)[0]
    df.columns=["description", "value"]
    return df.to_html(classes="table table-striped")


# # Mars Hemispheres

def mars_hem(browser):
    mars_hem_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hem_url)
    hemisphere_image_urls = []
    links = browser.find_by_css("a.product-item h3")
    for item in range(len(links)):
        hemisphere = {}
        browser.find_by_css("a.product-item h3")[item].click()
        sample_element = browser.find_by_text("Sample").first
        hemisphere["title"] = browser.find_by_css("h2.title").text
        hemisphere["img_url"] = sample_element["href"]
        hemisphere_image_urls.append(hemisphere)
        browser.back()
        return hemisphere_image_urls

def scrape():
    news_title, news_paragraph = mars_news(browser)
    img_url = featured_image(browser)
    mars_weather_info = mars_weather(browser)
    facts = mars_facts()
    hemisphere_image_urls = mars_hem(browser)
    timestamp = dt.datetime.now()

    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": img_url,
        "weather": mars_weather_info,
        "facts": facts,
        "hemispheres": hemisphere_image_urls,
        "last_modified": timestamp
    }
    browser.quit()
    return data 

if __name__ == "__main__":
    print(scrape())
