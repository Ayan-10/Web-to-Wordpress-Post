import requests
from bs4 import BeautifulSoup
import pandas as pd
from constants import API_KEY, SCRAPE_URL

def scrape():

    response = requests.get(
        'https://app.scrapingbee.com/api/v1',
        params={
            'api_key': API_KEY,
            'url': SCRAPE_URL,
            'render_js': 'true'  # Ensures JavaScript is rendered
        }
    )

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # divs = soup.find_all("div", class_="listicle-card")
        # data = []
        
        # for div in divs:
        #     img_tag = div.find('img')
        #     h2_tag = div.find('h2')
        #     p_tags = div.find_all('p')
        
        #     img_link = img_tag['src'] if img_tag else None
        #     h2_text = h2_tag.get_text(strip=True) if h2_tag else None
        #     p_text_combined = ' '.join([p.get_text(strip=False) for p in p_tags]) if p_tags else None
            
        #     data.append({
        #         'Image Link': img_link,
        #         'Heading': h2_text,
        #         'Text': p_text_combined
        #     })
        
        # df = pd.DataFrame(data)
        
        # print(df.head())
        
        header_div = soup.find('div', class_='contentbarheader')
        if header_div:
            header_div.decompose()  
        return soup.find("main", class_="listicle-page")


    else:
        print('Failed to retrieve the webpage:', response.status_code)
