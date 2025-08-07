import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('NOTION_TOKEN')
tasks_db_id = os.getenv('TASKS_DATABASE_ID')
project_id = "20e2eeca-eb8a-8075-8f0a-d40ea3291e96"  # ✅ CORRECT ID

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

task_data = {
    "parent": {"database_id": tasks_db_id},
    "properties": {
        "Name": {
            "title": [{"text": {"content": "TEST TASK - DELETE ME"}}]
        },
        "Related Project": {
            "relation": [{"id": project_id}]
        },
        "Status": {
            "status": {"name": "Not started"}
        }
    }
}

response = requests.post("https://api.notion.com/v1/pages", headers=headers, json=task_data)
print(f"Status: {response.status_code}")
print(f"Response: {response.text}")