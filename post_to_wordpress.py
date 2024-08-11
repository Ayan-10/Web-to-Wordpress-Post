import requests
from constants import WORDPRESS_BASE_URL, WORDPRESS_USERNAME, WORDPRESS_PASSWORD
from web_scrapper import scrape
from requests.auth import HTTPBasicAuth

# WordPress credentials

df = scrape()

print(df.head())

post_content = ""
for index, row in df.iterrows():
    # Create the post content
    post_content += f"""
    <h1>{row['Heading']}</h1>
    <img src="{row['Image Link']}" alt="{row['Heading']}">
    <p>{row['Text']}</p><br><br>
    """

# Create the post data
post_data = {
    'title': 'Dog Memes',
    'content': post_content,
    'status': 'publish'  # or 'draft' if you don't want to publish immediately
}

# Send the post request
response = requests.post(
    WORDPRESS_BASE_URL,
    auth=HTTPBasicAuth(WORDPRESS_USERNAME, WORDPRESS_PASSWORD),
    json=post_data
)


if response.status_code == 201:
    print(f"Post  published successfully.")
else:
    print(f"Failed to publish post . Response: {response.content}")

