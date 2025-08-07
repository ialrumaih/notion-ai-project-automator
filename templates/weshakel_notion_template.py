#!/usr/bin/env python3
"""
WeshAkel Restaurant App - Notion Project Template
AI-powered restaurant recommendation app for Saudi Arabia

This template creates a complete project structure in Notion for developing
the WeshAkel app with all tasks, phases, and documentation references.
"""

import requests
import json
from datetime import datetime, timedelta
import os
from typing import Dict, List, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class WeshAkelAutomator:
    """
    WeshAkel Restaurant App Project Automator
    Compatible with: https://github.com/ialrumaih/notion-ai-project-automator
    """
    
    def __init__(self):
        """Initialize the WeshAkel project automator"""
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
    
    def get_weshakel_tasks(self) -> List[Dict]:
        """Define all tasks for the WeshAkel Restaurant App project"""
        base_date = datetime.now()
        
        tasks = [
            # Phase 1: Project Setup & Architecture
            {
                "name": "1.1 - Create Xcode project with Core Data integration",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=2)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Set up iOS project with SwiftUI, Core Data, and proper folder structure"
            },
            {
                "name": "1.2 - Set up GitHub repository and CI/CD pipeline",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=3)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Configure version control, automated testing, and deployment pipeline"
            },
            {
                "name": "1.3 - Configure Firebase Analytics and Crashlytics",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=4)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Set up app monitoring, crash reporting, and user analytics"
            },
            {
                "name": "1.4 - Implement Core Data models for restaurants and users",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=7)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Create database entities for UserProfile, Restaurant, UserInteraction"
            },
            
            # Phase 2: Psychology Framework
            {
                "name": "2.1 - Design and validate 5 psychology questions",
                "area": "Research",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=12)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Create culturally-appropriate questions for Saudi users measuring dining psychology"
            },
            {
                "name": "2.2 - Create psychology onboarding UI flow",
                "area": "Design",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=16)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Build SwiftUI interface for psychology assessment with Arabic-first design"
            },
            {
                "name": "2.3 - Implement psychology scoring algorithm",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=19)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Convert question answers to 0-1 psychology dimension scores"
            },
            {
                "name": "2.4 - Test cultural appropriateness with Saudi focus group",
                "area": "Research",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=26)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Validate questions and UI with target demographic in Riyadh"
            },
            
            # Phase 3: AI Recommendation Engine
            {
                "name": "3.1 - Build hybrid intelligence recommendation algorithm",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=33)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Implement core recommendation logic combining psychology, context, and learning"
            },
            {
                "name": "3.2 - Implement restaurant scoring system (5 factors)",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=38)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Psychology (35%), History (25%), Context (20%), Distance (15%), Popularity (5%)"
            },
            {
                "name": "3.3 - Create user interaction tracking for learning",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=41)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Track accept/reject/visit/rate actions to improve recommendations"
            },
            {
                "name": "3.4 - Optimize recommendation performance (<500ms)",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=45)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Ensure fast recommendation generation for real-time user experience"
            },
            
            # Phase 4: API Integrations
            {
                "name": "4.1 - Integrate Google Places API for restaurant data",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=49)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Fetch restaurant information, ratings, and location data for Riyadh"
            },
            {
                "name": "4.2 - Implement Core Location for user positioning",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=51)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Get user GPS coordinates for proximity-based recommendations"
            },
            {
                "name": "4.3 - Set up restaurant data caching and refresh system",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=54)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Cache restaurant data locally and refresh weekly for offline capability"
            },
            {
                "name": "4.4 - Implement external Google Maps navigation",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=55)).strftime("%Y-%m-%d"),
                "priority": "Low",
                "description": "Open Google Maps app with restaurant destination for turn-by-turn directions"
            },
            
            # Phase 5: User Experience & Interface
            {
                "name": "5.1 - Design Arabic-first UI components and layout",
                "area": "Design",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=60)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Create culturally-appropriate design system with RTL support"
            },
            {
                "name": "5.2 - Implement main recommendation interface",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=64)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Build primary 'وش أكل؟' button and recommendation display"
            },
            {
                "name": "5.3 - Create recommendation card with explanations",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=67)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Display restaurant with clear Arabic explanation of why it was recommended"
            },
            {
                "name": "5.4 - Implement accessibility features (VoiceOver, Dynamic Type)",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=70)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Ensure app is accessible to users with disabilities"
            },
            
            # Phase 6: MVP Features Implementation
            {
                "name": "6.1 - Build guest-first user flow (no signup required)",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=72)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Allow immediate app usage without account creation"
            },
            {
                "name": "6.2 - Implement context selection (mood, companions, time)",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=75)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Allow users to specify current dining context for better recommendations"
            },
            {
                "name": "6.3 - Create recommendation interaction flow (accept/reject)",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=77)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Handle user responses to recommendations for algorithm learning"
            },
            {
                "name": "6.4 - Implement offline functionality for core features",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=81)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Ensure app works without internet using cached data"
            },
            
            # Phase 7: Testing & Quality Assurance
            {
                "name": "7.1 - Write unit tests for recommendation algorithm",
                "area": "Testing",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=85)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Test all components of the AI recommendation system"
            },
            {
                "name": "7.2 - Create UI automation tests for core user flows",
                "area": "Testing",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=88)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Automated testing of onboarding and recommendation flows"
            },
            {
                "name": "7.3 - Conduct Saudi cultural validation testing",
                "area": "Testing",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=93)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Validate app appropriateness with target Saudi demographic"
            },
            {
                "name": "7.4 - Performance testing and optimization",
                "area": "Testing",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=96)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Ensure app meets speed and reliability requirements"
            },
            
            # Phase 8: Launch Preparation
            {
                "name": "8.1 - Populate Riyadh restaurant database (500+ restaurants)",
                "area": "Data",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=103)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Build comprehensive database of halal restaurants in Riyadh"
            },
            {
                "name": "8.2 - Create App Store listing with Arabic localization",
                "area": "Marketing",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=106)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Prepare compelling App Store presence with screenshots and description"
            },
            {
                "name": "8.3 - Set up beta testing program with Saudi users",
                "area": "Testing",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=111)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Recruit and manage beta testing group in Riyadh"
            },
            {
                "name": "8.4 - Prepare launch analytics and monitoring dashboard",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=114)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Set up comprehensive tracking for post-launch optimization"
            }
        ]
        
        return tasks
    
    def create_project(self) -> Optional[str]:
        """Create the main WeshAkel project in Notion"""
        project_data = {
            "parent": {"database_id": self.projects_db_id},
            "properties": {
                "Name": {
                    "title": [
                        {
                            "text": {
                                "content": "WeshAkel Restaurant App Development"
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
                        "start": (datetime.now() + timedelta(days=120)).strftime("%Y-%m-%d")
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
            print(f"✅ Created project: WeshAkel Restaurant App Development")
            return result['id']
        except requests.exceptions.RequestException as e:
            print(f"❌ Error creating project: {e}")
            if 'response' in locals():
                print(f"   Response: {response.text}")
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
        """Main automation function that creates the project in Notion"""
        print("🍽 WESHAKEL RESTAURANT APP - NOTION PROJECT MANAGER")
        print("=" * 50)
        print("🎯 Target: WeshAkel Restaurant App Development")
        print("📋 Action: Create comprehensive project structure")
        print("⚡ Estimated time: ~1 minute")
        print("")
        
        # Create main project
        print("📋 Creating main project...")
        project_id = self.create_project()
        
        if not project_id:
            print("❌ Failed to create project. Stopping automation.")
            return False
        
        # Create all tasks
        print("\n📝 Creating tasks...")
        tasks = self.get_weshakel_tasks()
        created_tasks = 0
        
        for i, task in enumerate(tasks, 1):
            print(f"📝 Adding task {i}/{len(tasks)}: {task['name']}")
            if self.create_task(task, project_id):
                created_tasks += 1
        
        # Summary
        print(f"\n📊 Task Addition Summary:")
        print(f"✅ Successfully added: {created_tasks} tasks")
        print(f"❌ Failed to add: {len(tasks) - created_tasks} tasks")
        print(f"📋 Total attempted: {len(tasks)} tasks")
        
        print(f"\n📊 Project Breakdown:")
        print(f"   • Phase 1 (Setup & Architecture): 4 tasks")
        print(f"   • Phase 2 (Psychology Framework): 4 tasks")
        print(f"   • Phase 3 (AI Recommendation): 4 tasks")
        print(f"   • Phase 4 (API Integrations): 4 tasks")
        print(f"   • Phase 5 (UI/UX): 4 tasks")
        print(f"   • Phase 6 (MVP Features): 4 tasks")
        print(f"   • Phase 7 (Testing): 4 tasks")
        print(f"   • Phase 8 (Launch): 4 tasks")
        print(f"   • Total timeline: ~4 months")
        
        if created_tasks == len(tasks):
            print(f"\n🎉 SUCCESS! Your WeshAkel project has been created in Notion!")
            print(f"🎯 Next steps:")
            print(f"  1. Check your Projects database for the new project")
            print(f"  2. Review all tasks in the Tasks database")
            print(f"  3. Assign team members to tasks")
            print(f"  4. Start with Phase 1: Project Setup")
            print(f"🚀 Happy building! وبالتوفيق")
            return True
        else:
            print(f"\nPARTIAL SUCCESS - Some operations failed")
            print(f"Check the error messages above for details")
            return False

def main():
    """Entry point for the automation"""
    try:
        automator = WeshAkelAutomator()
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