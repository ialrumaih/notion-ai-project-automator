# Create test_status.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('NOTION_TOKEN')
tasks_db_id = os.getenv('TASKS_DATABASE_ID')

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# Get database schema to see exact status options
response = requests.get(f"https://api.notion.com/v1/databases/{tasks_db_id}", headers=headers)
db_info = response.json()

status_property = db_info['properties']['Status']
print("Available status options:")
for option in status_property['status']['options']:
    print(f"- '{option['name']}'")