#!/usr/bin/env python3
"""
Media Server Project Template for Notion AI Project Automator
Compatible with: https://github.com/ialrumaih/notion-ai-project-automator

This template creates a complete Local Media Server Setup project with:
- Phase 1: Planning & Research (4 tasks)
- Phase 2: Hardware Setup (5 tasks)  
- Phase 3: Software Configuration (6 tasks)
- Phase 4: Testing & Optimization (4 tasks)
Total: 19 structured tasks with relationships, priorities, and timelines.
"""

import requests
import json
from datetime import datetime, timedelta
import os
from typing import Dict, List, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class NotionMediaServerAutomator:
    def __init__(self):
        self.token = os.getenv('NOTION_TOKEN')
        self.projects_db_id = os.getenv('PROJECTS_DATABASE_ID')
        self.tasks_db_id = os.getenv('TASKS_DATABASE_ID')
        
        if not all([self.token, self.projects_db_id, self.tasks_db_id]):
            raise ValueError("❌ Missing required environment variables!")
        
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }
        self.base_url = "https://api.notion.com/v1"

    def get_media_server_tasks(self) -> List[Dict]:
        """Define all tasks for the Media Server project"""
        base_date = datetime.now()
        
        tasks = [
            # Phase 1: Planning & Research (4 tasks)
            {
                "name": "Research Media Server Platforms",
                "area": "Research",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=2)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Compare Plex, Jellyfin, Emby, and Kodi features, pricing, and hardware requirements"
            },
            {
                "name": "Define Hardware Requirements",
                "area": "Planning",
                "status": "Not started", 
                "due_date": (base_date + timedelta(days=3)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Determine CPU, RAM, storage capacity, and network requirements based on usage needs"
            },
            {
                "name": "Plan Network Architecture",
                "area": "Planning",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=4)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Design network topology, port forwarding, and security configurations"
            },
            {
                "name": "Create Media Organization Strategy",
                "area": "Planning", 
                "status": "Not started",
                "due_date": (base_date + timedelta(days=5)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Define folder structure, naming conventions, and metadata standards"
            },
            
            # Phase 2: Hardware Setup (5 tasks)
            {
                "name": "Acquire Server Hardware",
                "area": "Hardware",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=7)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Purchase or repurpose server, storage drives, and networking equipment"
            },
            {
                "name": "Install Operating System",
                "area": "Hardware",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=9)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Install Ubuntu Server, Windows, or preferred OS with basic configuration"
            },
            {
                "name": "Configure Storage Arrays", 
                "area": "Hardware",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=11)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Set up RAID, file systems, and mount points for media storage"
            },
            {
                "name": "Setup Network Configuration",
                "area": "Hardware",
                "status": "Not started", 
                "due_date": (base_date + timedelta(days=12)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Configure static IP, firewall rules, and basic security settings"
            },
            {
                "name": "Install Monitoring Tools",
                "area": "Hardware",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=13)).strftime("%Y-%m-%d"),
                "priority": "Low",
                "description": "Set up system monitoring for temperature, disk health, and performance"
            },
            
            # Phase 3: Software Configuration (6 tasks)
            {
                "name": "Install Media Server Software",
                "area": "Software",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=15)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Download and install chosen media server platform with initial setup"
            },
            {
                "name": "Configure Library Scanning",
                "area": "Software",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=17)).strftime("%Y-%m-%d"),
                "priority": "High", 
                "description": "Set up automatic library scanning, metadata fetching, and artwork download"
            },
            {
                "name": "Setup User Accounts & Permissions",
                "area": "Software",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=18)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Create user accounts, set viewing restrictions, and configure parental controls"
            },
            {
                "name": "Configure Remote Access",
                "area": "Software",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=20)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Set up port forwarding, VPN access, or cloud tunneling for external access"
            },
            {
                "name": "Install Mobile & TV Apps",
                "area": "Software",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=21)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Download and configure apps on phones, tablets, smart TVs, and streaming devices"
            },
            {
                "name": "Setup Automated Backups",
                "area": "Software",
                "status": "Not started", 
                "due_date": (base_date + timedelta(days=23)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Configure automated backups for metadata, settings, and critical system files"
            },
            
            # Phase 4: Testing & Optimization (4 tasks)
            {
                "name": "Performance Testing",
                "area": "Testing",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=25)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Test streaming quality, concurrent users, and transcoding performance"
            },
            {
                "name": "Quality Assurance Testing",
                "area": "Testing", 
                "status": "Not started",
                "due_date": (base_date + timedelta(days=27)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Test all client devices, subtitle support, and media format compatibility"
            },
            {
                "name": "Security Audit & Hardening",
                "area": "Security",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=29)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Review security settings, update passwords, and implement best practices"
            },
            {
                "name": "Create Documentation",
                "area": "Documentation",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=30)).strftime("%Y-%m-%d"),
                "priority": "Low",
                "description": "Document setup process, troubleshooting guide, and maintenance procedures"
            }
        ]
        
        return tasks

    def create_project(self) -> Optional[str]:
        """Create the main Media Server project"""
        project_data = {
            "parent": {"database_id": self.projects_db_id},
            "properties": {
                "Name": {
                    "title": [
                        {
                            "text": {
                                "content": "Local Media Server Setup"
                            }
                        }
                    ]
                },
                "Area": {
                    "select": {
                        "name": "Technology"
                    }
                },
                "Status": {
                    "status": {
                        "name": "Active"
                    }
                },
                "Due Date": {
                    "date": {
                        "start": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
                    }
                },
                "Priority": {
                    "select": {
                        "name": "High"
                    }
                }
            }
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/pages",
                headers=self.headers,
                json=project_data
            )
            response.raise_for_status()
            result = response.json()
            print(f"✅ Created project: Local Media Server Setup")
            return result['id']
        except requests.exceptions.RequestException as e:
            print(f"❌ Error creating project: {e}")
            return None

    def create_task(self, task: Dict, project_id: str) -> bool:
        """Create a single task linked to the project"""
        task_data = {
            "parent": {"database_id": self.tasks_db_id},
            "properties": {
                "Name": {
                    "title": [
                        {
                            "text": {
                                "content": task["name"]
                            }
                        }
                    ]
                },
                "Related Project": {
                    "relation": [
                        {
                            "id": project_id
                        }
                    ]
                },
                "Area": {
                    "select": {
                        "name": task["area"]
                    }
                },
                "Status": {
                    "status": {
                        "name": task["status"]
                    }
                },
                "Due Date": {
                    "date": {
                        "start": task["due_date"]
                    }
                },
                "Priority": {
                    "select": {
                        "name": task["priority"]
                    }
                },
                "Description": {
                    "rich_text": [
                        {
                            "text": {
                                "content": task["description"]
                            }
                        }
                    ]
                }
            }
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/pages",
                headers=self.headers,
                json=task_data
            )
            response.raise_for_status()
            print(f"✅ Successfully added: {task['name']}")
            return True
        except requests.exceptions.RequestException as e:
            print(f"❌ Failed to add: {task['name']}")
            print(f"   Status: {response.status_code if 'response' in locals() else 'No response'}")
            print(f"   Error: {e}")
            return False

    def run_automation(self):
        """Main automation function"""
        print("🤖 NOTION AI PROJECT MANAGER")
        print("=" * 50)
        print("🎯 Target: Local Media Server Setup")
        print("📋 Action: Add comprehensive task structure") 
        print("⚡ Estimated time: ~30 seconds")
        print("")
        
        # Create main project
        print("📋 Creating main project...")
        project_id = self.create_project()
        
        if not project_id:
            print("❌ Failed to create project. Stopping automation.")
            return
        
        # Create all tasks
        print("\n📝 Creating tasks...")
        tasks = self.get_media_server_tasks()
        created_tasks = 0
        
        for task in tasks:
            if self.create_task(task, project_id):
                created_tasks += 1
        
        # Summary
        print(f"\n🎉 Automation Complete!")
        print(f"   • Created 1 project: 'Local Media Server Setup'")
        print(f"   • Created {created_tasks}/{len(tasks)} tasks")
        print(f"   • Total timeline: 30 days")
        
        print(f"\n📊 Task Addition Summary:")
        print(f"✅ Successfully added: {created_tasks} tasks")
        print(f"❌ Failed to add: {len(tasks) - created_tasks} tasks")
        print(f"📋 Total attempted: {len(tasks)} tasks")
        
        if created_tasks == len(tasks):
            print(f"\n🎉 SUCCESS! Your Notion workspace has been automated!")
            print(f"🎯 Next steps:")
            print(f"  1. Check your Tasks database for new items")
            print(f"  2. Verify project progress updated automatically")
            print(f"  3. Start Phase 1: Research tasks!")
            print(f"🚀 Happy building!")
        else:
            print(f"\nPARTIAL SUCCESS - Some operations failed")
            print(f"Check the error messages above for details")

def main():
    """Entry point for the automation"""
    try:
        automator = NotionMediaServerAutomator()
        automator.run_automation()
    except ValueError as e:
        print(e)
        print("\n🔧 Setup Instructions:")
        print("   1. Create .env file with:")
        print("      NOTION_TOKEN=your_integration_token")
        print("      PROJECTS_DATABASE_ID=your_projects_db_id")
        print("      TASKS_DATABASE_ID=your_tasks_db_id")
        print("   2. Share your databases with the integration")
        print("   3. Run the script again")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()

# Template Usage:
# 1. Save this as templates/media_server.py in your notion-ai-project-automator repo
# 2. Update main.py to import and use this template:
#    from templates.media_server import NotionMediaServerAutomator
# 3. Run: python main.py