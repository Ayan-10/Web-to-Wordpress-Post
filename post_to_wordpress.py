import requests
from constants import WORDPRESS_BASE_URL, WORDPRESS_USERNAME, WORDPRESS_PASSWORD
from web_scrapper import scrape
import base64


# WordPress credentials

content = scrape()

# print(df.head())
# print(df)

# post_content = ""
# for index, row in df.iterrows():
#     # Create the post content
#     post_content += f"""
#     <img src="{row['Image Link']}" alt="{row['Heading']}">
#     <h1>{row['Heading']}</h1>
#     <p>{row['Text']}</p><br><br>
#     """

# Create the post data
post_data = {
    'title': '57 Dog Memes That Are Paws-itively Hilarious',
    'content': str(content),
    # 'status': 'publish'  # or 'draft' if you don't want to publish immediately
}

creds = WORDPRESS_USERNAME + ':' + WORDPRESS_PASSWORD
token = base64.b64encode(creds.encode())
headers = {'Authorization' : 'Basic ' + token.decode('utf-8')}
# Send the post request
response = requests.post(
    WORDPRESS_BASE_URL+'/wp-json/wp/v2/posts',
    headers=headers,
    json=post_data
)


if response.status_code == 201:
    print(f"Post published successfully.")
else:
    print(f"Failed to publish post . Response: {response.content}")

