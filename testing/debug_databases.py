import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('NOTION_TOKEN')
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# Test database access
projects_id = os.getenv('PROJECTS_DATABASE_ID')
tasks_id = os.getenv('TASKS_DATABASE_ID')

print("Testing Projects database...")
response = requests.get(f"https://api.notion.com/v1/databases/{projects_id}", headers=headers)
print(f"Projects: {response.status_code}")

print("Testing Tasks database...")  
response = requests.get(f"https://api.notion.com/v1/databases/{tasks_id}", headers=headers)
print(f"Tasks: {response.status_code}")