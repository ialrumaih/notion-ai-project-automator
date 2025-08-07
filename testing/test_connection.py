import requests
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('NOTION_TOKEN')
print(f"Token loaded: {token[:10]}...")  # Show first 10 chars only

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

response = requests.get("https://api.notion.com/v1/users/me", headers=headers)
print(f"Status: {response.status_code}")
print(f"Response: {response.text}")