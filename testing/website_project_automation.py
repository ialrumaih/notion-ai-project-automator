"""
🌐 Website Project Automation - Notion AI Project Manager

This script automatically populates your Notion workspace with a complete
website development project structure for WordPress + Elementor builds.

Designed for: TryMyAnalysis.com website project
Author: Ibrahem Alrumaih
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

class WebsiteProjectAutomator:
    """
    Automates Notion setup for website development projects
    
    This class handles:
    - Connection to Notion API
    - Finding existing website projects
    - Archiving old website tasks
    - Adding comprehensive website development task structure
    - Setting proper phases and timelines
    """
    
    def __init__(self):
        """Initialize the Notion API connection"""
        print("🌐 Initializing Website Project Automator...")
        
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
            "Notion-Version": "2022-06-28"
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
    
    def find_website_project(self):
        """
        Find the existing website project
        
        Returns:
            str: Project ID if found, None otherwise
        """
        print("🔍 Looking for existing website project...")
        
        try:
            # Query the Projects database for website project
            response = requests.post(
                f"{self.base_url}/databases/{self.projects_db_id}/query",
                headers=self.headers,
                json={
                    "filter": {
                        "property": "Name",
                        "title": {
                            "contains": "TryMyAnalysis"
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
                    print("❌ Website project not found!")
                    print("Please make sure you have a project containing 'TryMyAnalysis'")
                    return None
            else:
                print(f"❌ Database query failed: {response.status_code}")
                print(f"Error: {response.text}")
                return None
                
        except Exception as e:
            print(f"❌ Error finding project: {str(e)}")
            return None
    
    def archive_old_website_tasks(self, project_id):
        """
        Archive existing website-related tasks to clean the workspace
        
        Args:
            project_id (str): The Notion page ID of the website project
        """
        print("🗑️ Archiving old website tasks...")
        
        try:
            # Query for tasks related to this project
            response = requests.post(
                f"{self.base_url}/databases/{self.tasks_db_id}/query",
                headers=self.headers,
                json={
                    "filter": {
                        "property": "Related Project",
                        "relation": {
                            "contains": project_id
                        }
                    }
                }
            )
            
            if response.status_code == 200:
                results = response.json().get('results', [])
                
                if results:
                    print(f"🗂️ Found {len(results)} existing tasks to archive...")
                    
                    archived_count = 0
                    for task in results:
                        task_id = task['id']
                        task_name = task['properties']['Name']['title'][0]['text']['content']
                        
                        # Archive the task
                        archive_response = requests.patch(
                            f"{self.base_url}/pages/{task_id}",
                            headers=self.headers,
                            json={"archived": True}
                        )
                        
                        if archive_response.status_code == 200:
                            archived_count += 1
                            print(f"📦 Archived: {task_name}")
                        else:
                            print(f"❌ Failed to archive: {task_name}")
                    
                    print(f"✅ Successfully archived {archived_count} old tasks")
                else:
                    print("✅ No existing tasks found - clean workspace!")
                    
        except Exception as e:
            print(f"❌ Error during archival: {str(e)}")
    
    def get_website_task_templates(self):
        """
        Define all the tasks for the website development project
        
        Returns:
            list: List of task dictionaries with all properties
        """
        return [
            # Phase 1: Setup & Infrastructure (COMPLETED)
            {
                "name": "1.1 Hostinger Hosting Setup",
                "area": "Company",
                "status": "Done",
                "due_date": "2025-06-08",
                "priority": "High",
                "description": "Premium hosting plan activated, domain connected, WordPress installed"
            },
            {
                "name": "1.2 WordPress Configuration", 
                "area": "Company",
                "status": "Done",
                "due_date": "2025-06-08",
                "priority": "High",
                "description": "Latest WordPress version, PHP 8.3, basic security settings"
            },
            {
                "name": "1.3 Essential Plugins Installation",
                "area": "Company",
                "status": "Done",
                "due_date": "2025-06-08",
                "priority": "High",
                "description": "Elementor, RankMath SEO, Wordfence Security, LiteSpeed Cache"
            },
            
            # Phase 2: Branding & Design Foundation (COMPLETED)
            {
                "name": "2.1 Brand Identity Setup",
                "area": "Company",
                "status": "Done",
                "due_date": "2025-06-09",
                "priority": "Medium",
                "description": "Custom logos, favicon, color palette, typography settings"
            },
            {
                "name": "2.2 Elementor Global Configuration",
                "area": "Company",
                "status": "Done",
                "due_date": "2025-06-09",
                "priority": "Medium",
                "description": "Global fonts, colors, spacing, container settings, responsive breakpoints"
            },
            {
                "name": "2.3 Coming Soon Page Setup",
                "area": "Company",
                "status": "Done",
                "due_date": "2025-06-09",
                "priority": "Low",
                "description": "Temporary page during development to hide site from public"
            },
            
            # Phase 3: Home Page Development (COMPLETED)
            {
                "name": "3.1 Home Page Hero Section",
                "area": "Company",
                "status": "Done",
                "due_date": "2025-06-10",
                "priority": "High",
                "description": "Main headline, value proposition, primary CTA, hero image/video"
            },
            {
                "name": "3.2 Home Page Intro Statement",
                "area": "Company",
                "status": "Done",
                "due_date": "2025-06-10",
                "priority": "Medium",
                "description": "Company overview, mission statement, credibility building"
            },
            {
                "name": "3.3 Home Page Services Preview",
                "area": "Company",
                "status": "Done",
                "due_date": "2025-06-10",
                "priority": "High",
                "description": "6-service grid layout with icons, titles, brief descriptions"
            },
            {
                "name": "3.4 Home Page About Preview",
                "area": "Company",
                "status": "Done",
                "due_date": "2025-06-10",
                "priority": "Medium",
                "description": "Personal introduction, expertise preview, link to full About page"
            },
            {
                "name": "3.5 Home Page Contact CTA",
                "area": "Company",
                "status": "Done",
                "due_date": "2025-06-10",
                "priority": "Medium",
                "description": "Contact form preview, consultation booking, contact information"
            },
            
            # Phase 4: About Page Development (IN PROGRESS)
            {
                "name": "4.1 About Page Bio Section",
                "area": "Company",
                "status": "In progress",
                "due_date": "2025-06-26",
                "priority": "High",
                "description": "Personal story, background, professional journey, photo"
            },
            {
                "name": "4.2 About Page Experience Section",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-06-27",
                "priority": "High",
                "description": "Work history, key projects, industry experience, achievements"
            },
            {
                "name": "4.3 About Page Skills & Expertise",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-06-28",
                "priority": "Medium",
                "description": "Technical skills, analytical capabilities, industry knowledge"
            },
            {
                "name": "4.4 About Page Credentials & Education",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-06-29",
                "priority": "Medium",
                "description": "Certifications, education, professional memberships, awards"
            },
            {
                "name": "4.5 About Page Personal Touch",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-06-30",
                "priority": "Low",
                "description": "Interests, values, working style, what makes you unique"
            },
            
            # Phase 5: Services Page Development
            {
                "name": "5.1 Services Page Header & Overview",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-01",
                "priority": "High",
                "description": "Services introduction, value proposition, service categories overview"
            },
            {
                "name": "5.2 Detailed Service #1 Section",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-02",
                "priority": "High",
                "description": "First service detailed description, benefits, process, pricing"
            },
            {
                "name": "5.3 Detailed Service #2 Section",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-02",
                "priority": "High",
                "description": "Second service detailed description, benefits, process, pricing"
            },
            {
                "name": "5.4 Detailed Service #3 Section",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-03",
                "priority": "High",
                "description": "Third service detailed description, benefits, process, pricing"
            },
            {
                "name": "5.5 Detailed Service #4 Section",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-03",
                "priority": "Medium",
                "description": "Fourth service detailed description, benefits, process, pricing"
            },
            {
                "name": "5.6 Detailed Service #5 Section",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-04",
                "priority": "Medium",
                "description": "Fifth service detailed description, benefits, process, pricing"
            },
            {
                "name": "5.7 Detailed Service #6 Section",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-04",
                "priority": "Medium",
                "description": "Sixth service detailed description, benefits, process, pricing"
            },
            {
                "name": "5.8 Services Page CTA & Consultation",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-05",
                "priority": "High",
                "description": "Service inquiry form, consultation booking, contact information"
            },
            
            # Phase 6: Contact Page Development
            {
                "name": "6.1 Contact Page Header & Information",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-06",
                "priority": "High",
                "description": "Contact introduction, business hours, response expectations"
            },
            {
                "name": "6.2 Contact Form Development",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-07",
                "priority": "High",
                "description": "Multi-field contact form with validation, service selection, message"
            },
            {
                "name": "6.3 Contact Information Display",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-07",
                "priority": "Medium",
                "description": "Email, phone, location, social media links, business address"
            },
            {
                "name": "6.4 Google Maps Integration",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-08",
                "priority": "Low",
                "description": "Embedded map if physical location, or region coverage area"
            },
            {
                "name": "6.5 Social Media & Professional Links",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-08",
                "priority": "Medium",
                "description": "LinkedIn, Twitter, GitHub, professional profiles integration"
            },
            
            # Phase 7: SEO, Performance & Mobile Optimization
            {
                "name": "7.1 RankMath SEO Configuration",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-09",
                "priority": "High",
                "description": "Meta titles, descriptions, keywords, schema markup, XML sitemap"
            },
            {
                "name": "7.2 Mobile Responsiveness Testing",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-10",
                "priority": "High",
                "description": "Test all pages on mobile devices, tablet optimization, touch targets"
            },
            {
                "name": "7.3 Page Speed Optimization",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-11",
                "priority": "High",
                "description": "LiteSpeed Cache configuration, image optimization, CSS/JS minification"
            },
            {
                "name": "7.4 Cross-Browser Testing",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-12",
                "priority": "Medium",
                "description": "Test on Chrome, Firefox, Safari, Edge, mobile browsers"
            },
            {
                "name": "7.5 Accessibility Testing",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-13",
                "priority": "Medium",
                "description": "Screen reader compatibility, keyboard navigation, color contrast"
            },
            {
                "name": "7.6 Analytics Setup",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-14",
                "priority": "Medium",
                "description": "Google Analytics, Search Console, conversion tracking setup"
            },
            
            # Phase 8: Launch Preparation & Go-Live
            {
                "name": "8.1 Final Content Review",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-15",
                "priority": "High",
                "description": "Proofread all content, check links, verify contact information"
            },
            {
                "name": "8.2 Security & Backup Setup",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-16",
                "priority": "High",
                "description": "Wordfence final config, automated backups, SSL certificate verification"
            },
            {
                "name": "8.3 DNS & Domain Configuration",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-17",
                "priority": "High",
                "description": "Final DNS settings, www redirect, subdomain setup if needed"
            },
            {
                "name": "8.4 Launch Checklist Completion",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-18",
                "priority": "High",
                "description": "Complete pre-launch checklist, final testing, stakeholder approval"
            },
            {
                "name": "8.5 Disable Coming Soon Mode",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-19",
                "priority": "High",
                "description": "Make site public, announce launch, submit to search engines"
            },
            {
                "name": "8.6 Post-Launch Monitoring",
                "area": "Company",
                "status": "Not started",
                "due_date": "2025-07-20",
                "priority": "Medium",
                "description": "Monitor site performance, check analytics, address any immediate issues"
            }
        ]
    
    def add_website_tasks(self, project_id):
        """
        Add all website task templates to the specified project
        
        Args:
            project_id (str): The Notion page ID of the project
            
        Returns:
            bool: True if successful, False otherwise
        """
        print("🚀 Adding website development tasks...")
        
        tasks = self.get_website_task_templates()
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
                        "status": {"name": task["status"]}
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
        Update the project due date to mid-July 2025 (accounting for travel)
        
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
                        "date": {"start": "2025-07-20"}
                    }
                }
            }
            
            response = requests.patch(
                f"{self.base_url}/pages/{project_id}",
                headers=self.headers,
                json=update_data
            )
            
            if response.status_code == 200:
                print("✅ Project timeline updated to July 20, 2025 (post-travel)")
                return True
            else:
                print(f"❌ Failed to update timeline: {response.status_code}")
                print(f"Error: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Exception updating timeline: {str(e)}")
            return False
    
    def run_automation(self):
        """
        Main automation workflow for website project
        
        This method orchestrates the entire process:
        1. Test API connection
        2. Find the website project
        3. Archive old website tasks (clean slate)
        4. Add comprehensive new task structure
        5. Update project timeline for post-travel launch
        """
        print("🌐 WEBSITE PROJECT AUTOMATOR")
        print("=" * 50)
        print("🎯 Target: TryMyAnalysis.com Website Project")
        print("📋 Action: Replace with comprehensive task structure")
        print("⏰ Timeline: Adjusted for June 13-25 travel")
        print("⚡ Estimated time: ~1 minute")
        print("")
        
        # Step 1: Test connection
        if not self.test_connection():
            print("❌ Cannot proceed without API connection")
            return False
        
        # Step 2: Find the website project
        project_id = self.find_website_project()
        if not project_id:
            print("❌ Cannot proceed without finding the project")
            return False
        
        # Step 3: Archive old tasks (clean slate)
        print("\n" + "="*50)
        self.archive_old_website_tasks(project_id)
        
        # Step 4: Add comprehensive new task structure
        print("\n" + "="*50)
        tasks_success = self.add_website_tasks(project_id)
        
        # Step 5: Update project timeline
        print("\n" + "="*50)
        timeline_success = self.update_project_timeline(project_id)
        
        # Final summary
        print("\n" + "🎉"*20)
        if tasks_success and timeline_success:
            print("SUCCESS! Your website project has been automated!")
            print("🎯 Project Structure:")
            print("  ✅ Phase 1-3: Marked as DONE (completed work)")
            print("  🔄 Phase 4: About Page (IN PROGRESS)")
            print("  📅 Phase 5-8: Ready for post-travel development")
            print("")
            print("🚀 Next steps:")
            print("  1. Check your Tasks database for new website tasks")
            print("  2. Verify project progress updated automatically") 
            print("  3. Resume Phase 4 work on June 26 after travel")
            print("  4. Follow the structured timeline to July 20 launch!")
            print("")
            print("🌐 Happy website building!")
        else:
            print("PARTIAL SUCCESS - Some operations failed")
            print("Check the error messages above for details")
        print("🎉"*20)
        
        return tasks_success and timeline_success

def main():
    """
    Entry point for the website automation script
    """
    try:
        # Create and run the automation
        automator = WebsiteProjectAutomator()
        success = automator.run_automation()
        
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