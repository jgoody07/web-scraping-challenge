# Web Scraping Homework - Mission to Mars

 The goal of this project is to build a web application that scrapes various websites for data related to Mars and displays the information in a single HTML page.

# This was a mulit-step process.

1. Initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter. Code for this process can be viewed in the mission_to_mars.ipynb file. This includes the scraping of; 

    * NASA Mars News Site to collect the latest News Title and Paragraph Text 

    * JPL Mars Space Images to collect a Featured Image URL

    * The Mars Facts webpage to collect a table of Mars Facts

    * USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres

2. Convert the Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of the scraping code from the Jupyter Notebook file and return one Python dictionary containing all of the scraped data.

3. Create an app.py file

    * Be sure to establish a connection to a MongoDB so that the return value can be stored in Mongo as a Python dictionary.

    * Within the app.py file create a route called '/scrape' that will import the 'scrape_mars.py' script and call the scrape function. 

    * Create a root route '/' that will query the Mongo database that was created and pass the mars data into an HTML template to display the data

4. Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 


## Requirement include: ##
* MongoDB - download here - https://www.mongodb.com/try/download/community

* Chrome drive - download from repository

* Modules Required
    pandas
    splinter import Browser
    b4 import Beautifulsoup
    requests
    pymongo
    flask import Flask, render_template, redirect, url_for
    from flask_pymongo import PyMongo
    lxml
    Jinja2
