from notion_client import Client
from dotenv import load_dotenv
import os

load_dotenv()
notion = Client(auth=os.getenv("NOTION_TOKEN"))

# Search for your Mission Control page
response = notion.search(query="Mission Control")

print("🔍 Found pages:")
for item in response.get('results', []):
    if item['object'] == 'page':
        title_prop = item.get('properties', {}).get('title', {})
        if title_prop and title_prop.get('title'):
            title = title_prop['title'][0]['plain_text']
        else:
            title = "Untitled"
        print(f"📄 {title} - ID: {item['id']}")