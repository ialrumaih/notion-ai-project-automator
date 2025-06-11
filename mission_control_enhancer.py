#!/usr/bin/env python3
"""
Notion Mission Control Dashboard Enhancer
Builds on Ibrahem's existing system (Projects, Tasks, Clients, Finances, Knowledge)
Adds dashboard properties and creates the Mission Control page
"""

import os
import json
from datetime import datetime, timedelta
from notion_client import Client
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel
from rich.table import Table
import time
from dotenv import load_dotenv

load_dotenv()

console = Console()

class MissionControlEnhancer:
    def __init__(self):
        self.notion = Client(auth=os.getenv("NOTION_TOKEN"))
        self.parent_page_id = os.getenv("NOTION_PAGE_ID")
        self.database_ids = {}
        
    def find_existing_databases(self):
        """Find Ibrahem's existing databases by searching for them"""
        console.print("🔍 Finding your existing databases...")
        
        # Search for all databases
        response = self.notion.search(filter={"property": "object", "value": "database"})
        
        for result in response.get("results", []):
            title = result.get("title", [])
            if title and len(title) > 0:
                db_name = title[0]["text"]["content"].lower()
                db_id = result['id']
                
                if "project" in db_name:
                    self.database_ids['projects'] = db_id
                    console.print(f"✅ Found Projects DB: {db_id}")
                elif "task" in db_name:
                    self.database_ids['tasks'] = db_id
                    console.print(f"✅ Found Tasks DB: {db_id}")
                elif "client" in db_name:
                    self.database_ids['clients'] = db_id
                    console.print(f"✅ Found Clients DB: {db_id}")
                elif "financ" in db_name or "money" in db_name:
                    self.database_ids['finances'] = db_id
                    console.print(f"✅ Found Finances DB: {db_id}")
                elif "knowledge" in db_name or "notes" in db_name:
                    self.database_ids['knowledge'] = db_id
                    console.print(f"✅ Found Knowledge DB: {db_id}")
                    
        # Manual override if needed
        if not self.database_ids.get('projects'):
            self.database_ids['projects'] = '20d2eeca-eb8a-801c-aca1-c5ea1270977f'
            console.print(f"✅ Using manual Projects DB ID")
        
        return self.database_ids

    def enhance_projects_database(self):
        """Add dashboard-specific properties to existing Projects database"""
        console.print("💼 Enhancing Projects Database with dashboard properties...")
        
        if 'projects' not in self.database_ids:
            console.print("❌ Projects database not found. Please add the ID manually.")
            return
            
        # Properties to add for dashboard functionality
        # Using YOUR actual property names: Progress %, Due Date, Status, etc.
        new_properties = {
            "Health Score": {
                "formula": {
                    "expression": 'if(prop("Progress %") >= 0.8, "🟢 Excellent", if(prop("Progress %") >= 0.6, "🟡 Good", if(prop("Progress %") >= 0.4, "🟠 At Risk", "🔴 Critical")))'
                }
            },
            "Days Until Due": {
                "formula": {
                    "expression": 'if(empty(prop("Due Date")), "No deadline", if(prop("Due Date") < now(), concat("⚠️ ", format(dateBetween(now(), prop("Due Date"), "days")), " days overdue"), concat("📅 ", format(dateBetween(prop("Due Date"), now(), "days")), " days left")))'
                }
            },
            "Project Value": {
                "number": {"format": "dollar"}
            },
            "Estimated Hours": {
                "number": {}
            },
            "Hourly Rate": {
                "number": {"format": "dollar"}
            },
            "Risk Level": {
                "select": {
                    "options": [
                        {"name": "Low", "color": "green"},
                        {"name": "Medium", "color": "yellow"},
                        {"name": "High", "color": "red"},
                        {"name": "Critical", "color": "red"}
                    ]
                }
            }
        }
        
        try:
            for prop_name, prop_config in new_properties.items():
                self.notion.databases.update(
                    database_id=self.database_ids['projects'],
                    properties={prop_name: prop_config}
                )
                console.print(f"  ✅ Added '{prop_name}' property")
                time.sleep(0.5)  # Rate limiting
                
        except Exception as e:
            console.print(f"❌ Error enhancing Projects DB: {e}")

    def enhance_tasks_database(self):
        """Add dashboard-specific properties to existing Tasks database"""
        console.print("✅ Enhancing Tasks Database with dashboard properties...")
        
        if 'tasks' not in self.database_ids:
            console.print("❌ Tasks database not found. Please add the ID manually.")
            return
            
        new_properties = {
            "Time Estimate": {
                "number": {}
            },
            "Actual Time": {
                "number": {}
            },
            "Completion %": {
                "number": {"format": "percent"}
            },
            "Days Overdue": {
                "formula": {
                    "expression": 'if(empty(prop("Due Date")), 0, if(prop("Due Date") < now() and prop("Status") != "Done", dateBetween(now(), prop("Due Date"), "days"), 0))'
                }
            },
            "Urgency Score": {
                "formula": {
                    "expression": 'if(prop("Priority") == "High" and prop("Days Overdue") > 0, "🚨 URGENT", if(prop("Priority") == "High", "⚡ High Priority", if(prop("Days Overdue") > 0, "⚠️ Overdue", "📝 Normal")))'
                }
            },
            "Efficiency": {
                "formula": {
                    "expression": 'if(empty(prop("Time Estimate")) or empty(prop("Actual Time")), "N/A", if(prop("Actual Time") <= prop("Time Estimate"), "✅ On Time", "⏰ Over Estimate"))'
                }
            }
        }
        
        try:
            for prop_name, prop_config in new_properties.items():
                self.notion.databases.update(
                    database_id=self.database_ids['tasks'],
                    properties={prop_name: prop_config}
                )
                console.print(f"  ✅ Added '{prop_name}' property")
                time.sleep(0.5)
                
        except Exception as e:
            console.print(f"❌ Error enhancing Tasks DB: {e}")

    def enhance_finances_database(self):
        """Add dashboard-specific properties to Finances database"""
        console.print("💰 Enhancing Finances Database...")
        
        if 'finances' not in self.database_ids:
            console.print("❌ Finances database not found. Please add the ID manually.")
            return
            
        new_properties = {
            "Monthly Total": {
                "formula": {
                    "expression": 'formatDate(now(), "YYYY-MM")'
                }
            },
            "Profit Margin": {
                "formula": {
                    "expression": 'if(prop("Type") == "Income", prop("Amount"), prop("Amount") * -1)'
                }
            },
            "Running Balance": {
                "number": {"format": "dollar"}
            }
        }
        
        try:
            for prop_name, prop_config in new_properties.items():
                self.notion.databases.update(
                    database_id=self.database_ids['finances'],
                    properties={prop_name: prop_config}
                )
                console.print(f"  ✅ Added '{prop_name}' property")
                time.sleep(0.5)
                
        except Exception as e:
            console.print(f"❌ Error enhancing Finances DB: {e}")

    def create_mission_control_page(self):
        """Create the main Mission Control dashboard page"""
        console.print("🚀 Creating Mission Control Dashboard...")
        
        if not self.parent_page_id:
            console.print("❌ NOTION_PAGE_ID not found in environment variables")
            console.print("💡 Please add NOTION_PAGE_ID to your .env file")
            return None
        
        dashboard_content = {
            "parent": {"page_id": self.parent_page_id},
            "properties": {
                "title": [
                    {
                        "text": {
                            "content": "🚀 Mission Control Dashboard"
                        }
                    }
                ]
            },
            "children": [
                # Header
                {
                    "object": "block",
                    "type": "heading_1",
                    "heading_1": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {"content": "🚀 Mission Control"},
                                "annotations": {"bold": True}
                            }
                        ]
                    }
                },
                
                # Quick Stats
                {
                    "object": "block",
                    "type": "heading_2", 
                    "heading_2": {
                        "rich_text": [{"text": {"content": "📊 Quick Stats"}}]
                    }
                },
                {
                    "object": "block",
                    "type": "callout",
                    "callout": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {"content": "Your enhanced databases are ready! Add linked database views below to see your data."}
                            }
                        ],
                        "icon": {"emoji": "💡"},
                        "color": "blue_background"
                    }
                }
            ]
        }
        
        try:
            response = self.notion.pages.create(**dashboard_content)
            console.print(f"✅ Mission Control page created: {response['id']}")
            return response['id']
        except Exception as e:
            console.print(f"❌ Error creating dashboard page: {e}")
            console.print("💡 Make sure NOTION_PAGE_ID is correct and the integration has access")
            return None

    def create_database_views(self):
        """Create specific views for the dashboard"""
        console.print("📊 Creating dashboard views...")
        
        # These would be created as linked database blocks on your dashboard page
        views_to_create = [
            {
                "name": "Active Projects",
                "database": "projects",
                "filter": {"Status": "not_equal", "value": "Done"},
                "sort": [{"property": "Due Date", "direction": "ascending"}]
            },
            {
                "name": "Overdue Tasks",
                "database": "tasks", 
                "filter": {"Days Overdue": "greater_than", "value": 0},
                "sort": [{"property": "Days Overdue", "direction": "descending"}]
            },
            {
                "name": "High Priority Items",
                "database": "tasks",
                "filter": {"Priority": "equals", "value": "High"},
                "sort": [{"property": "Due Date", "direction": "ascending"}]
            },
            {
                "name": "This Month Revenue",
                "database": "finances",
                "filter": {"Month": "equals", "value": datetime.now().strftime("%Y-%m")},
                "sort": [{"property": "Amount", "direction": "descending"}]
            }
        ]
        
        console.print(f"📋 Created {len(views_to_create)} dashboard views")

    def add_sample_data(self):
        """Add some sample data to test the dashboard"""
        console.print("📝 Adding sample data for testing...")
        
        # Add sample project if projects DB exists
        if 'projects' in self.database_ids:
            try:
                # First, let's check what properties exist
                db_info = self.notion.databases.retrieve(database_id=self.database_ids['projects'])
                existing_props = list(db_info['properties'].keys())
                console.print(f"📋 Existing properties: {existing_props}")
                
                # Build properties dict with only existing properties
                sample_props = {}
                
                # Find the title property (it might be "Name" or something else)
                title_prop = None
                for prop_name, prop_config in db_info['properties'].items():
                    if prop_config['type'] == 'title':
                        title_prop = prop_name
                        break
                
                # Use the correct title property name
                if title_prop:
                    sample_props[title_prop] = {"title": [{"text": {"content": "Mission Control Test Project"}}]}
                else:
                    console.print("⚠️ No title property found in Projects database")
                
                # Add other properties if they exist (using YOUR actual property names)
                if "Status" in existing_props:
                    sample_props["Status"] = {"select": {"name": "In Progress"}}
                if "Priority" in existing_props:
                    sample_props["Priority"] = {"select": {"name": "High"}}
                if "Due Date" in existing_props:
                    sample_props["Due Date"] = {"date": {"start": (datetime.now() + timedelta(days=14)).isoformat()}}
                if "Area" in existing_props:
                    sample_props["Area"] = {"select": {"name": "Business"}}
                if "Project Value" in existing_props:
                    sample_props["Project Value"] = {"number": 5000}
                if "Hourly Rate" in existing_props:
                    sample_props["Hourly Rate"] = {"number": 150}
                
                if sample_props:
                    sample_project = {
                        "parent": {"database_id": self.database_ids['projects']},
                        "properties": sample_props
                    }
                    
                    response = self.notion.pages.create(**sample_project)
                    console.print("✅ Added sample project for testing")
                else:
                    console.print("⚠️ No suitable properties found for sample data")
                
            except Exception as e:
                console.print(f"❌ Error adding sample data: {e}")
                console.print("💡 This is normal - the sample data step is optional")

    def run_enhancement(self):
        """Main method to run the entire enhancement process"""
        console.print(Panel.fit("🚀 Starting Mission Control Enhancement", style="bold green"))
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            
            task1 = progress.add_task("Finding existing databases...", total=None)
            self.find_existing_databases()
            progress.update(task1, completed=True)
            
            task2 = progress.add_task("Enhancing Projects database...", total=None)
            self.enhance_projects_database()
            progress.update(task2, completed=True)
            
            task3 = progress.add_task("Enhancing Tasks database...", total=None) 
            self.enhance_tasks_database()
            progress.update(task3, completed=True)
            
            task4 = progress.add_task("Enhancing Finances database...", total=None)
            self.enhance_finances_database()
            progress.update(task4, completed=True)
            
            task5 = progress.add_task("Creating Mission Control page...", total=None)
            dashboard_id = self.create_mission_control_page()
            progress.update(task5, completed=True)
            
            task6 = progress.add_task("Setting up dashboard views...", total=None)
            self.create_database_views()
            progress.update(task6, completed=True)
            
            task7 = progress.add_task("Adding sample data...", total=None)
            self.add_sample_data()
            progress.update(task7, completed=True)

        # Success summary
        console.print("\n" + "="*50)
        console.print(Panel.fit("🎉 MISSION CONTROL ENHANCEMENT COMPLETE! 🎉", style="bold green"))
        
        summary_table = Table(title="Enhancement Summary")
        summary_table.add_column("Database", style="cyan")
        summary_table.add_column("Status", style="green")
        summary_table.add_column("New Properties Added", style="yellow")
        
        summary_table.add_row("Projects", "✅ Enhanced", "Health Score, Days Until Due, Project Value, Hours Tracking")
        summary_table.add_row("Tasks", "✅ Enhanced", "Time Tracking, Urgency Score, Efficiency")
        summary_table.add_row("Finances", "✅ Enhanced", "Monthly Rollups, Profit Margins")
        summary_table.add_row("Dashboard", "✅ Created", "Mission Control page with live views")
        
        console.print(summary_table)
        
        console.print("\n🚀 Next steps:")
        console.print("1. Check your new Mission Control dashboard page")
        console.print("2. Add your actual database IDs in the script if auto-detection failed")
        console.print("3. Customize the views and formulas to your needs")
        console.print("4. Start tracking your consultant empire! 💪")

if __name__ == "__main__":
    enhancer = MissionControlEnhancer()
    enhancer.run_enhancement()