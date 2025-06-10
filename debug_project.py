import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('NOTION_TOKEN')
projects_db_id = os.getenv('PROJECTS_DATABASE_ID')

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# Query for the trading project
response = requests.post(
    f"https://api.notion.com/v1/databases/{projects_db_id}/query",
    headers=headers,
    json={
        "filter": {
            "property": "Name",
            "title": {
                "contains": "Dynamic Stock Trading"
            }
        }
    }
)

print(f"Query status: {response.status_code}")
if response.status_code == 200:
    results = response.json().get('results', [])
    if results:
        project = results[0]
        print(f"✅ Found project!")
        print(f"Project ID: {project['id']}")
        print(f"Project Name: {project['properties']['Name']['title'][0]['text']['content']}")
        
        # Try to access this specific project page
        project_id = project['id']
        page_response = requests.get(f"https://api.notion.com/v1/pages/{project_id}", headers=headers)
        print(f"Project page access: {page_response.status_code}")
        
    else:
        print("❌ No project found with 'Dynamic Stock Trading' in name")
else:
    print(f"Error: {response.text}")