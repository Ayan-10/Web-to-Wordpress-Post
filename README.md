# Web to Wordpess post

## Installation
pip install requests, bs4

## Environment Variables
Go to constants.py
1. Create an API Key and add it to **API_KEY** variable.
     - Go to ScrappingBee [https://www.scrapingbee.com/].
     - Generate an API key, copy it, and put it in **API_KEY** variable.
2. Put the URL you want to scrape, and add it to the **SCRAPE_URL** variable.
3. You haven't provided me your WordPress base URL, So add your base WordPress URL to **WORDPRESS_BASE_URL** variable.
4. Add your WordPress username and password to **WORDPRESS_USERNAME**, **WORDPRESS_PASSWORD**.

## RUN
python post_to_wordpress.py
