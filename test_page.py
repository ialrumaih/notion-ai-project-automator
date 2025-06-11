from notion_client import Client
from dotenv import load_dotenv
import os

load_dotenv()
notion = Client(auth=os.getenv("NOTION_TOKEN"))

# Test both formats
page_ids = [
    "20f2eecaeb8a8096a7b4fab940e26537",
    "20f2eeca-eb8a-8096-a7b4-fab940e26537"
]

for page_id in page_ids:
    try:
        response = notion.pages.retrieve(page_id=page_id)
        print(f"✅ Found page with ID: {page_id}")
        print(f"NOTION_PAGE_ID={page_id}")
        break
    except Exception as e:
        print(f"❌ Failed with ID: {page_id}")