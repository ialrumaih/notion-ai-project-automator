"""
🤖 Notion AI Project Manager - Main Automation Script

This script automatically populates your Notion workspace with a complete
Trading AI project structure including tasks, relationships, and timelines.

Author: Ibrahem Al-Rumaih
Email: ibrahem@trymyanalysis.com
GitHub: https://github.com/ialrumaih/notion-ai-project-manager
"""

import os
import sys
import requests
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class NotionAIProjectManager:
    """
    Main class for automating Notion project setup
    
    This class handles:
    - Connection to Notion API
    - Finding existing projects
    - Adding new tasks with proper relationships
    - Updating project timelines
    """
    
    def __init__(self):
        """Initialize the Notion API connection"""
        print("🤖 Initializing Notion AI Project Manager...")
        
        # Load credentials from environment variables
        self.token = os.getenv('NOTION_TOKEN')
        self.projects_db_id = os.getenv('PROJECTS_DATABASE_ID') 
        self.tasks_db_id = os.getenv('TASKS_DATABASE_ID')
        
        # Validate credentials
        if not all([self.token, self.projects_db_id, self.tasks_db_id]):
            print("❌ Missing required environment variables!")
            print("Please check your .env file contains:")
            print("- NOTION_TOKEN")
            print("- PROJECTS_DATABASE_ID") 
            print("- TASKS_DATABASE_ID")
            sys.exit(1)
        
        # Notion API configuration
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json", 
            "Notion-Version": "2022-06-28"  # API version
        }
        self.base_url = "https://api.notion.com/v1"
        
        print("✅ Configuration loaded successfully!")
    
    def test_connection(self):
        """Test if we can connect to Notion API"""
        print("🔗 Testing Notion API connection...")
        
        try:
            response = requests.get(
                f"{self.base_url}/users/me",
                headers=self.headers
            )
            
            if response.status_code == 200:
                user_data = response.json()
                print(f"✅ Connected as: {user_data.get('name', 'Unknown User')}")
                return True
            else:
                print(f"❌ Connection failed: {response.status_code}")
                print(f"Error: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Connection error: {str(e)}")
            return False
    
    def find_trading_project(self):
        """
        Find the existing 'Dynamic Stock Trading AI Platform' project
        
        Returns:
            str: Project ID if found, None otherwise
        """
        print("🔍 Looking for existing Trading AI project...")
        
        try:
            # Query the Projects database for our specific project
            response = requests.post(
                f"{self.base_url}/databases/{self.projects_db_id}/query",
                headers=self.headers,
                json={
                    "filter": {
                        "property": "Name",
                        "title": {
                            "contains": "Dynamic Stock Trading"
                        }
                    }
                }
            )
            
            if response.status_code == 200:
                results = response.json().get('results', [])
                
                if results:
                    project_id = results[0]['id']
                    project_name = results[0]['properties']['Name']['title'][0]['text']['content']
                    print(f"✅ Found project: {project_name}")
                    print(f"📋 Project ID: {project_id}")
                    return project_id
                else:
                    print("❌ Trading AI project not found!")
                    print("Please make sure you have a project named 'Dynamic Stock Trading AI Platform'")
                    return None
            else:
                print(f"❌ Database query failed: {response.status_code}")
                print(f"Error: {response.text}")
                return None
                
        except Exception as e:
            print(f"❌ Error finding project: {str(e)}")
            return None
    
    def get_task_templates(self):
        """
        Define all the tasks to be added to the Trading AI project
        
        Returns:
            list: List of task dictionaries with all properties
        """
        return [
            # Phase 1: Universal Exit Rule Framework
            {
                "name": "1.5 Performance Benchmarking System",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-06-28",
                "priority": "Medium",
                "description": "Compare against buy-and-hold for any stock"
            },
            {
                "name": "1.6 Exit Rule Validation Framework", 
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-06-30",
                "priority": "Medium",
                "description": "Robust testing across different stocks and time periods"
            },
            
            # Phase 2: Adaptive ML Entry Signal Engine
            {
                "name": "2.1 Universal Feature Engineering Pipeline",
                "area": "Company", 
                "status": "Not started",
                "due_date": "2025-06-26",
                "priority": "High",
                "description": "Technical indicators that work across all stocks"
            },
            {
                "name": "2.2 Stock-Specific Feature Adaptation",
                "area": "Company",
                "status": "Not started", 
                "due_date": "2025-06-28",
                "priority": "High",
                "description": "Auto-adjust features based on stock volatility, sector, size"
            },
            {
                "name": "2.3 Dynamic Target Label Creation",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-06-30", 
                "priority": "High",
                "description": "Use Phase 1 optimal exits per stock to create training labels"
            },
            {
                "name": "2.4 Meta-Learning Model Architecture",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-02",
                "priority": "Medium",
                "description": "Model that learns how to learn new stocks quickly"
            },
            {
                "name": "2.5 Stock Characteristic Classification",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-05",
                "priority": "Medium", 
                "description": "Auto-categorize stocks (high-vol, trending, mean-reverting)"
            },
            {
                "name": "2.6 Adaptive Model Selection",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-08",
                "priority": "Medium",
                "description": "Different ML models for different stock types"
            },
            {
                "name": "2.7 Cross-Stock Validation",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-12",
                "priority": "High",
                "description": "Test model trained on one stock, applied to others"
            },
            {
                "name": "2.8 Feature Importance Ranking",
                "area": "Company", 
                "status": "Not started",
                "due_date": "2025-07-15",
                "priority": "Medium",
                "description": "Which indicators matter most for which stock types"
            },
            {
                "name": "2.9 Signal Confidence Scoring",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-18",
                "priority": "High",
                "description": "Dynamic confidence thresholds per stock"
            },
            {
                "name": "2.10 Multi-Stock Signal Generation",
                "area": "Company",
                "status": "Not started", 
                "due_date": "2025-07-20",
                "priority": "High",
                "description": "Unified pipeline for any Tadawul stock"
            },
            
            # Phase 3: Platform Development & UI
            {
                "name": "3.1 Stock Selection Interface",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-22",
                "priority": "High",
                "description": "User picks any Tadawul stock, system adapts automatically"
            },
            {
                "name": "3.2 Auto-Optimization Dashboard",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-25", 
                "priority": "High",
                "description": "Real-time exit rule optimization for selected stock"
            },
            {
                "name": "3.3 Model Training Interface",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-28",
                "priority": "Medium",
                "description": "One-click ML training for new stocks"
            },
            {
                "name": "3.4 Signal Generation Dashboard",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-08-01",
                "priority": "High",
                "description": "Live signals for user's selected stock portfolio"
            },
            {
                "name": "3.5 Performance Analytics",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-08-05",
                "priority": "Medium",
                "description": "Compare strategies across multiple stocks"
            },
            {
                "name": "3.6 Risk Management Module",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-08-08",
                "priority": "High",
                "description": "Portfolio-level risk across different stocks"
            },
            {
                "name": "3.7 Alert System",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-08-12",
                "priority": "Medium",
                "description": "Notifications when signals trigger for any tracked stock"
            },
            {
                "name": "3.8 Strategy Export/Import",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-08-15",
                "priority": "Low",
                "description": "Save/load optimized parameters for different stocks"
            },
            
            # Phase 4: Multi-Stock Validation & Deployment
            {
                "name": "4.1 Tadawul Top 50 Testing",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-08-17",
                "priority": "High",
                "description": "Test system on major Saudi stocks"
            },
            {
                "name": "4.2 Sector-Specific Analysis",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-08-19",
                "priority": "Medium",
                "description": "Banks vs Tech vs Oil vs Real Estate performance"
            },
            {
                "name": "4.3 Portfolio-Level Backtesting",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-08-22",
                "priority": "High", 
                "description": "Multi-stock portfolio with dynamic allocation"
            },
            {
                "name": "4.4 Market Condition Adaptation",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-08-25",
                "priority": "Medium",
                "description": "Bull/bear/sideways market performance"
            },
            {
                "name": "4.5 Production Deployment",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-08-28",
                "priority": "High",
                "description": "Live system ready for real trading"
            },
            {
                "name": "4.6 User Documentation",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-08-30",
                "priority": "Medium",
                "description": "Complete guide for using the platform"
            },
            {
                "name": "4.7 Final System Validation",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-08-31",
                "priority": "High",
                "description": "End-to-end testing and performance review"
            },
            
            # Research Tasks
            {
                "name": "R1 Tadawul Market Structure Analysis",
                "area": "Company",
                "status": "In progress",  # ✅ FIXED: lowercase 'p' to match database
                "due_date": "2025-06-26",
                "priority": "Medium",
                "description": "Sector correlations, market cap effects, liquidity patterns"
            },
            {
                "name": "R2 Transfer Learning for Finance",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-06-28",
                "priority": "Low",
                "description": "How models trained on one stock apply to others"
            },
            {
                "name": "R3 Dynamic Parameter Optimization",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-05",
                "priority": "Medium",
                "description": "Real-time adaptation as market conditions change"
            },
            {
                "name": "R4 Alternative Data Integration",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-12",
                "priority": "Low",
                "description": "News sentiment, economic indicators, oil prices"
            }
        ]
    
    def add_tasks_to_project(self, project_id):
        """
        Add all task templates to the specified project
        
        Args:
            project_id (str): The Notion page ID of the project
            
        Returns:
            bool: True if successful, False otherwise
        """
        print("🚀 Adding tasks to project...")
        
        tasks = self.get_task_templates()
        added_count = 0
        failed_count = 0
        
        for i, task in enumerate(tasks, 1):
            print(f"📝 Adding task {i}/{len(tasks)}: {task['name']}")
            
            # Create the task data structure for Notion API
            task_data = {
                "parent": {"database_id": self.tasks_db_id},
                "properties": {
                    "Name": {
                        "title": [{"text": {"content": task["name"]}}]
                    },
                    "Related Project": {
                        "relation": [{"id": project_id}]
                    },
                    "Area": {
                        "select": {"name": task["area"]}
                    },
                    "Status": {
                        "status": {"name": task["status"]}  # ✅ FIXED: Using "status" instead of "select"
                    },
                    "Due Date": {
                        "date": {"start": task["due_date"]}
                    },
                    "Priority": {
                        "select": {"name": task["priority"]}
                    },
                    "Description": {
                        "rich_text": [{"text": {"content": task["description"]}}]
                    }
                }
            }
            
            try:
                # Make the API call to create the task
                response = requests.post(
                    f"{self.base_url}/pages",
                    headers=self.headers,
                    json=task_data
                )
                
                if response.status_code == 200:
                    added_count += 1
                    print(f"✅ Successfully added: {task['name']}")
                else:
                    failed_count += 1
                    print(f"❌ Failed to add: {task['name']}")
                    print(f"   Status: {response.status_code}")
                    print(f"   Error: {response.text}")
                    
            except Exception as e:
                failed_count += 1
                print(f"❌ Exception adding {task['name']}: {str(e)}")
        
        print(f"\n📊 Task Addition Summary:")
        print(f"✅ Successfully added: {added_count} tasks")
        print(f"❌ Failed to add: {failed_count} tasks")
        print(f"📋 Total attempted: {len(tasks)} tasks")
        
        return failed_count == 0
    
    def update_project_timeline(self, project_id):
        """
        Update the project due date to August 31, 2025
        
        Args:
            project_id (str): The Notion page ID of the project
            
        Returns:
            bool: True if successful, False otherwise
        """
        print("📅 Updating project timeline...")
        
        try:
            update_data = {
                "properties": {
                    "Due Date": {
                        "date": {"start": "2025-08-31"}
                    }
                }
            }
            
            response = requests.patch(
                f"{self.base_url}/pages/{project_id}",
                headers=self.headers,
                json=update_data
            )
            
            if response.status_code == 200:
                print("✅ Project timeline updated to August 31, 2025")
                return True
            else:
                print(f"❌ Failed to update timeline: {response.status_code}")
                print(f"Error: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Exception updating timeline: {str(e)}")
            return False
    
    def cleanup_test_tasks(self):
        """
        Optional: Clean up any test tasks that were created during debugging
        """
        print("🧹 Checking for test tasks to clean up...")
        
        try:
            # Query for test tasks
            response = requests.post(
                f"{self.base_url}/databases/{self.tasks_db_id}/query",
                headers=self.headers,
                json={
                    "filter": {
                        "property": "Name",
                        "title": {
                            "contains": "TEST TASK"
                        }
                    }
                }
            )
            
            if response.status_code == 200:
                results = response.json().get('results', [])
                
                if results:
                    print(f"🗑️ Found {len(results)} test tasks to delete...")
                    
                    for task in results:
                        task_id = task['id']
                        task_name = task['properties']['Name']['title'][0]['text']['content']
                        
                        # Archive the test task
                        delete_response = requests.patch(
                            f"{self.base_url}/pages/{task_id}",
                            headers=self.headers,
                            json={"archived": True}
                        )
                        
                        if delete_response.status_code == 200:
                            print(f"✅ Cleaned up: {task_name}")
                        else:
                            print(f"❌ Failed to clean up: {task_name}")
                else:
                    print("✅ No test tasks found - workspace is clean!")
                    
        except Exception as e:
            print(f"❌ Error during cleanup: {str(e)}")
    
    def run_automation(self):
        """
        Main automation workflow
        
        This method orchestrates the entire process:
        1. Test API connection
        2. Find the trading project
        3. Clean up any test tasks
        4. Add all tasks
        5. Update project timeline
        """
        print("🤖 NOTION AI PROJECT MANAGER")
        print("=" * 50)
        print("🎯 Target: Dynamic Stock Trading AI Platform")
        print("📋 Action: Add comprehensive task structure")
        print("⚡ Estimated time: ~1 minute")
        print("")
        
        # Step 1: Test connection
        if not self.test_connection():
            print("❌ Cannot proceed without API connection")
            return False
        
        # Step 2: Find the trading project
        project_id = self.find_trading_project()
        if not project_id:
            print("❌ Cannot proceed without finding the project")
            return False
        
        # Step 3: Clean up test tasks (optional)
        print("\n" + "="*50)
        self.cleanup_test_tasks()
        
        # Step 4: Add all tasks
        print("\n" + "="*50)
        tasks_success = self.add_tasks_to_project(project_id)
        
        # Step 5: Update project timeline
        print("\n" + "="*50)
        timeline_success = self.update_project_timeline(project_id)
        
        # Final summary
        print("\n" + "🎉"*20)
        if tasks_success and timeline_success:
            print("SUCCESS! Your Notion workspace has been automated!")
            print("🎯 Next steps:")
            print("  1. Check your Tasks database for new items")
            print("  2. Verify project progress updated automatically") 
            print("  3. Delete the test task if it still exists")
            print("  4. Start Phase 2 development!")
            print("🚀 Happy coding!")
        else:
            print("PARTIAL SUCCESS - Some operations failed")
            print("Check the error messages above for details")
        print("🎉"*20)
        
        return tasks_success and timeline_success

def main():
    """
    Entry point for the automation script
    """
    try:
        # Create and run the automation
        manager = NotionAIProjectManager()
        success = manager.run_automation()
        
        # Exit with appropriate code
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print("\n❌ Automation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()