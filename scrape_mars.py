# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import pymongo

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=True)

def scrape():
    browser = init_browser()
    
    ## ======Scraping Mars News====== ##
    url = 'https://mars.nasa.gov/news'
    browser.visit(url)

    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
    
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')

    # Retrieve News title and News text
    news_title = news_soup.find_all('div', class_='content_title')[0].text
    news_para = news_soup.find_all('div', class_='article_teaser_body')[0].text

    ## ======Scraping Mars Feature Image====== ##
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    browser.visit(image_url)

    html = browser.html
    image_soup = BeautifulSoup(html, 'html.parser')

    # Retrieve featured image link
    # Retrieve background-image url from style tag 
    image_url = image_soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

    # Website Url 
    base_url = 'https://www.jpl.nasa.gov'

    # Concatenate website url with scrapped route
    featured_image_url = base_url + image_url

    ## ======Scraping Mars Facts====== ##
    facts_url = 'https://space-facts.com/mars/'
    table = pd.read_html(facts_url)

    mars_facts = table[2]
    mars_facts.columns = ["Description", "Value"]

    mars_html_table = mars_facts.to_html()
    mars_html_table = mars_html_table.replace('\n', '')

    ## ======Scraping Mars Hemisphere name and image====== ##
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)

    hemispheres_html = browser.html
    hemispheres_soup = BeautifulSoup(hemispheres_html, 'html.parser')

    hem_img = hemispheres_soup.find_all('div', class_= 'item')

    # Create empty list for hemisphere urls 
    hemisphere_image_urls = []

    # Store the main_ul 
    hemispheres_main_url = 'https://astrogeology.usgs.gov'

    # Create a For Loop to loop through items stored
    for i in hem_img: 
        # Store title
        title = i.find('h3').text
        
        # Store link that leads to full image website
        part_img_url = i.find('a', class_='itemLink product-item')['href']
        
        # Visit the link that contains the full image website 
        browser.visit(hemispheres_main_url + part_img_url)
        
        # HTML Object of individual hemisphere information website 
        part_img_html = browser.html
        
        # Parse HTML with Beautiful Soup for every individual hemisphere information website 
        soup = BeautifulSoup( part_img_html, 'html.parser')
        
        # Retrieve full image source 
        img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
        
        # Append the retreived information into a list of dictionaries 
        hemisphere_image_urls.append({"title" : title, "img_url" : img_url})

    ## ======Set up the dictionary====== ##
    mars_dict = {
            "news_title": news_title,
            "news_para": news_para,
            "featured_image_url": featured_image_url,
            "fact_table": str(mars_html_table),
            "hemisphere_images": hemisphere_image_urls
        }

# Close the browser after scraping
    browser.quit()
    print(mars_dict)
    return mars_dict

init_browser()
scrape()
