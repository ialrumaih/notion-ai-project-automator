#!/usr/bin/env python3
"""
Web Development Project Template for Notion AI Project Automator
Creates a complete Full-Stack Web Application project with:
- Phase 1: Planning & Design (6 tasks)
- Phase 2: Backend Development (8 tasks)
- Phase 3: Frontend Development (7 tasks)
- Phase 4: Testing & Deployment (6 tasks)
Total: 27 structured tasks for modern web development
"""

import requests
import json
from datetime import datetime, timedelta
import os
from typing import Dict, List, Optional
from dotenv import load_dotenv

load_dotenv()

class NotionWebDevAutomator:
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

    def get_web_dev_tasks(self) -> List[Dict]:
        """Define all tasks for the Web Development project"""
        base_date = datetime.now()
        
        tasks = [
            # Phase 1: Planning & Design (6 tasks)
            {
                "name": "Requirements Gathering & Analysis",
                "area": "Planning",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=3)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Define project scope, user stories, functional requirements, and technical specifications"
            },
            {
                "name": "Technology Stack Selection",
                "area": "Planning",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=5)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Choose frontend framework, backend technology, database, hosting platform, and development tools"
            },
            {
                "name": "Database Schema Design",
                "area": "Design",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=7)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Design entity relationships, create ERD, define tables, indexes, and data constraints"
            },
            {
                "name": "API Design & Documentation",
                "area": "Design",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=9)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Design RESTful API endpoints, request/response formats, and create OpenAPI documentation"
            },
            {
                "name": "UI/UX Wireframes & Mockups",
                "area": "Design",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=12)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Create wireframes, user flow diagrams, and high-fidelity mockups for all pages"
            },
            {
                "name": "Development Environment Setup",
                "area": "Development",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=14)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Set up local development environment, version control, CI/CD pipeline, and code standards"
            },
            
            # Phase 2: Backend Development (8 tasks)
            {
                "name": "Project Structure & Configuration",
                "area": "Backend",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=16)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Initialize project structure, configure build tools, environment variables, and dependencies"
            },
            {
                "name": "Database Implementation",
                "area": "Backend",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=19)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Create database tables, relationships, migrations, and seed data for development"
            },
            {
                "name": "Authentication & Authorization",
                "area": "Backend",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=23)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Implement user registration, login, JWT tokens, password hashing, and role-based access"
            },
            {
                "name": "Core API Endpoints",
                "area": "Backend",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=28)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Develop CRUD operations, business logic, data validation, and error handling"
            },
            {
                "name": "File Upload & Media Handling",
                "area": "Backend",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=32)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Implement file upload, image processing, cloud storage integration, and media optimization"
            },
            {
                "name": "Email & Notification System",
                "area": "Backend",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=35)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Set up email templates, SMTP configuration, push notifications, and notification preferences"
            },
            {
                "name": "API Security & Rate Limiting",
                "area": "Backend",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=38)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Implement CORS, input sanitization, rate limiting, API key management, and security headers"
            },
            {
                "name": "Logging & Monitoring Setup",
                "area": "Backend",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=40)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Configure application logging, error tracking, performance monitoring, and health checks"
            },
            
            # Phase 3: Frontend Development (7 tasks)
            {
                "name": "Frontend Project Setup",
                "area": "Frontend",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=42)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Initialize frontend framework, configure build tools, routing, and development server"
            },
            {
                "name": "UI Component Library",
                "area": "Frontend",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=47)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Create reusable components, design system, theme configuration, and component documentation"
            },
            {
                "name": "State Management Implementation",
                "area": "Frontend",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=50)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Set up global state management, API integration, caching, and data flow patterns"
            },
            {
                "name": "User Authentication Flow",
                "area": "Frontend",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=53)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Build login/register forms, protected routes, token management, and session handling"
            },
            {
                "name": "Core Application Features",
                "area": "Frontend",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=60)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Develop main application screens, user interactions, form validations, and data display"
            },
            {
                "name": "Responsive Design & Mobile Optimization",
                "area": "Frontend",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=65)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Implement responsive layouts, mobile-first design, touch interactions, and cross-browser compatibility"
            },
            {
                "name": "Performance Optimization",
                "area": "Frontend",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=68)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Optimize bundle size, implement lazy loading, image optimization, and performance monitoring"
            },
            
            # Phase 4: Testing & Deployment (6 tasks)
            {
                "name": "Unit & Integration Testing",
                "area": "Testing",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=72)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Write unit tests, integration tests, API tests, and achieve minimum 80% code coverage"
            },
            {
                "name": "End-to-End Testing",
                "area": "Testing",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=75)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Create E2E test scenarios, user journey tests, and automated browser testing"
            },
            {
                "name": "Security Testing & Audit",
                "area": "Security",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=77)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Conduct security audit, vulnerability scanning, penetration testing, and security compliance"
            },
            {
                "name": "Production Environment Setup",
                "area": "Deployment",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=80)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Configure production servers, database, CDN, SSL certificates, and monitoring systems"
            },
            {
                "name": "CI/CD Pipeline & Deployment",
                "area": "Deployment",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=83)).strftime("%Y-%m-%d"),
                "priority": "High",
                "description": "Set up automated deployment, staging environment, rollback procedures, and release management"
            },
            {
                "name": "Documentation & Handover",
                "area": "Documentation",
                "status": "Not started",
                "due_date": (base_date + timedelta(days=85)).strftime("%Y-%m-%d"),
                "priority": "Medium",
                "description": "Create technical documentation, user guides, deployment instructions, and maintenance procedures"
            }
        ]
        
        return tasks

    def create_project(self) -> Optional[str]:
        """Create the main Web Development project"""
        project_data = {
            "parent": {"database_id": self.projects_db_id},
            "properties": {
                "Name": {
                    "title": [
                        {
                            "text": {
                                "content": "Full-Stack Web Application"
                            }
                        }
                    ]
                },
                "Area": {
                    "select": {
                        "name": "Development"
                    }
                },
                "Status": {
                    "status": {
                        "name": "Active"
                    }
                },
                "Due Date": {
                    "date": {
                        "start": (datetime.now() + timedelta(days=85)).strftime("%Y-%m-%d")
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
            print(f"✅ Created project: Full-Stack Web Application")
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
            print(f"✅ Created task: {task['name']}")
            return True
        except requests.exceptions.RequestException as e:
            print(f"❌ Error creating task '{task['name']}': {e}")
            return False

    def run_automation(self):
        """Main automation function"""
        print("🚀 Web Development Project Automation")
        print("=" * 50)
        
        # Create main project
        print("📋 Creating main project...")
        project_id = self.create_project()
        
        if not project_id:
            print("❌ Failed to create project. Stopping automation.")
            return
        
        # Create all tasks
        print("\n📝 Creating tasks...")
        tasks = self.get_web_dev_tasks()
        created_tasks = 0
        
        for task in tasks:
            if self.create_task(task, project_id):
                created_tasks += 1
        
        # Summary
        print(f"\n🎉 Automation Complete!")
        print(f"   • Created 1 project: 'Full-Stack Web Application'")
        print(f"   • Created {created_tasks}/{len(tasks)} tasks")
        print(f"   • Total timeline: 85 days (~3 months)")
        print(f"   • Ready for development!")
        
        print(f"\n📊 Task Breakdown:")
        print(f"   • Phase 1 (Planning & Design): 6 tasks")
        print(f"   • Phase 2 (Backend Development): 8 tasks") 
        print(f"   • Phase 3 (Frontend Development): 7 tasks")
        print(f"   • Phase 4 (Testing & Deployment): 6 tasks")

def main():
    """Entry point for the automation"""
    try:
        automator = NotionWebDevAutomator()
        automator.run_automation()
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()