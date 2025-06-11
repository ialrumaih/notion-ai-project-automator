#!/usr/bin/env python3
"""
Debug script to check your actual Notion database schema
This will show us exactly what properties and options are available
"""

import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

def debug_database_schema():
    """Check the actual structure of your databases"""
    
    token = os.getenv('NOTION_TOKEN')
    projects_db_id = os.getenv('PROJECTS_DATABASE_ID')
    tasks_db_id = os.getenv('TASKS_DATABASE_ID')
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    
    print("🔍 DEBUGGING NOTION DATABASE SCHEMA")
    print("=" * 60)
    
    # Check Projects Database
    print("📋 PROJECTS DATABASE SCHEMA:")
    print("-" * 30)
    
    try:
        response = requests.get(f"https://api.notion.com/v1/databases/{projects_db_id}", headers=headers)
        if response.status_code == 200:
            db_info = response.json()
            properties = db_info['properties']
            
            for prop_name, prop_info in properties.items():
                prop_type = prop_info['type']
                print(f"✅ {prop_name}: {prop_type}")
                
                # Show options for select/status properties
                if prop_type == 'select' and 'select' in prop_info:
                    options = prop_info['select'].get('options', [])
                    if options:
                        option_names = [opt['name'] for opt in options]
                        print(f"   Options: {option_names}")
                
                elif prop_type == 'status' and 'status' in prop_info:
                    options = prop_info['status'].get('options', [])
                    if options:
                        option_names = [opt['name'] for opt in options]
                        print(f"   Status options: {option_names}")
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")
    
    except Exception as e:
        print(f"❌ Error checking projects database: {e}")
    
    print("\n📝 TASKS DATABASE SCHEMA:")
    print("-" * 30)
    
    try:
        response = requests.get(f"https://api.notion.com/v1/databases/{tasks_db_id}", headers=headers)
        if response.status_code == 200:
            db_info = response.json()
            properties = db_info['properties']
            
            for prop_name, prop_info in properties.items():
                prop_type = prop_info['type']
                print(f"✅ {prop_name}: {prop_type}")
                
                # Show options for select/status properties
                if prop_type == 'select' and 'select' in prop_info:
                    options = prop_info['select'].get('options', [])
                    if options:
                        option_names = [opt['name'] for opt in options]
                        print(f"   Options: {option_names}")
                
                elif prop_type == 'status' and 'status' in prop_info:
                    options = prop_info['status'].get('options', [])
                    if options:
                        option_names = [opt['name'] for opt in options]
                        print(f"   Status options: {option_names}")
                        
                elif prop_type == 'relation' and 'relation' in prop_info:
                    database_id = prop_info['relation']['database_id']
                    print(f"   Relates to: {database_id}")
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")
    
    except Exception as e:
        print(f"❌ Error checking tasks database: {e}")

    print("\n💡 TESTING A SIMPLE PROJECT CREATION:")
    print("-" * 40)
    
    # Test creating a minimal project
    minimal_project = {
        "parent": {"database_id": projects_db_id},
        "properties": {
            "Name": {
                "title": [{"text": {"content": "TEST PROJECT - DELETE ME"}}]
            }
        }
    }
    
    try:
        response = requests.post(
            "https://api.notion.com/v1/pages",
            headers=headers,
            json=minimal_project
        )
        
        if response.status_code == 200:
            print("✅ Basic project creation works!")
            
            # Clean up the test project
            test_project_id = response.json()['id']
            cleanup_response = requests.patch(
                f"https://api.notion.com/v1/pages/{test_project_id}",
                headers=headers,
                json={"archived": True}
            )
            if cleanup_response.status_code == 200:
                print("✅ Test project cleaned up")
        else:
            print(f"❌ Basic project creation failed: {response.status_code}")
            print(f"Response: {response.text}")
    
    except Exception as e:
        print(f"❌ Error testing project creation: {e}")

if __name__ == "__main__":
    debug_database_schema()