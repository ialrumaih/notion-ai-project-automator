#!/usr/bin/env python3
"""
🤖 Notion AI Project Manager - Dynamic Template System

This script automatically discovers all available project templates and 
lets you choose which one to run. Just add new templates to the templates/
folder and they'll appear in the menu automatically!

Author: Ibrahem Al-Rumaih
Email: ibrahem@trymyanalysis.com
GitHub: https://github.com/ialrumaih/notion-ai-project-automator
"""

import os
import sys
import importlib
import inspect
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class DynamicProjectManager:
    """
    Dynamic project manager that auto-discovers and runs templates
    """
    
    def __init__(self):
        """Initialize the dynamic project manager"""
        print("🤖 Notion AI Project Manager - Dynamic Edition")
        print("=" * 60)
        
        self.templates_dir = Path("templates")
        self.available_templates = {}
        
        # Validate environment
        self._check_environment()
        
        # Discover templates
        self._discover_templates()
    
    def _check_environment(self):
        """Check if required environment variables are set"""
        required_vars = ['NOTION_TOKEN', 'PROJECTS_DATABASE_ID', 'TASKS_DATABASE_ID']
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        
        if missing_vars:
            print("❌ Missing required environment variables:")
            for var in missing_vars:
                print(f"   • {var}")
            print("\n🔧 Please check your .env file contains all required variables")
            sys.exit(1)
        
        print("✅ Environment variables loaded successfully")
    
    def _discover_templates(self):
        """Automatically discover all available project templates"""
        print("🔍 Scanning for available project templates...")
        
        if not self.templates_dir.exists():
            print(f"❌ Templates directory not found: {self.templates_dir}")
            print("Please create the templates/ folder and add template files")
            sys.exit(1)
        
        # Look for Python files in templates directory
        template_files = list(self.templates_dir.glob("*.py"))
        template_files = [f for f in template_files if f.name != "__init__.py"]
        
        if not template_files:
            print("❌ No template files found in templates/ directory")
            print("Please add at least one template file (e.g., trading_ai.py)")
            sys.exit(1)
        
        # Import and analyze each template
        for template_file in template_files:
            template_name = template_file.stem  # filename without .py
            
            try:
                # Import the template module
                module_path = f"templates.{template_name}"
                module = importlib.import_module(module_path)
                
                # Look for automator classes (classes that end with 'Automator')
                automator_classes = []
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if name.endswith('Automator') and hasattr(obj, 'run_automation'):
                        automator_classes.append((name, obj))
                
                if automator_classes:
                    # Use the first automator class found
                    class_name, class_obj = automator_classes[0]
                    
                    # Try to get project info from the class or module
                    project_info = self._extract_project_info(module, class_obj, template_name)
                    
                    self.available_templates[template_name] = {
                        'module': module,
                        'class': class_obj,
                        'info': project_info
                    }
                    
                    print(f"✅ Found template: {project_info['display_name']}")
                else:
                    print(f"⚠️  Skipped {template_file}: No Automator class found")
                    
            except Exception as e:
                print(f"❌ Error loading {template_file}: {str(e)}")
        
        if not self.available_templates:
            print("❌ No valid templates found!")
            print("Templates must contain a class ending with 'Automator' and have run_automation() method")
            sys.exit(1)
        
        print(f"🎯 Total templates available: {len(self.available_templates)}")
    
    def _extract_project_info(self, module, class_obj, template_name):
        """Extract project information from template"""
        # Try to get info from module docstring
        project_name = "Unknown Project"
        description = "No description available"
        
        if hasattr(module, '__doc__') and module.__doc__:
            lines = module.__doc__.strip().split('\n')
            # Look for project name in docstring
            for line in lines:
                if 'creates a complete' in line.lower() or 'project' in line.lower():
                    # Extract project name from description
                    if ':' in line:
                        project_name = line.split(':')[0].strip()
                    break
        
        # Fallback: use template name
        if project_name == "Unknown Project":
            project_name = template_name.replace('_', ' ').title()
        
        # Try to get description from docstring
        if hasattr(module, '__doc__') and module.__doc__:
            doc_lines = [line.strip() for line in module.__doc__.strip().split('\n') if line.strip()]
            if len(doc_lines) > 1:
                description = doc_lines[1]  # Second line usually has description
        
        return {
            'display_name': project_name,
            'description': description,
            'template_name': template_name
        }
    
    def _display_template_menu(self):
        """Display available templates and get user selection"""
        print("\n🚀 Available Project Templates:")
        print("=" * 60)
        
        template_list = list(self.available_templates.items())
        
        for i, (template_name, template_data) in enumerate(template_list, 1):
            info = template_data['info']
            print(f"{i}. {info['display_name']}")
            print(f"   📝 {info['description']}")
            print(f"   📁 File: templates/{template_name}.py")
            print()
        
        print("0. Exit")
        print("=" * 60)
        
        while True:
            try:
                choice = input(f"Select template (0-{len(template_list)}): ").strip()
                
                if choice == '0':
                    print("👋 Goodbye!")
                    sys.exit(0)
                
                choice_num = int(choice)
                if 1 <= choice_num <= len(template_list):
                    selected_template = template_list[choice_num - 1]
                    return selected_template[0], selected_template[1]  # template_name, template_data
                else:
                    print(f"❌ Please enter a number between 0 and {len(template_list)}")
                    
            except ValueError:
                print("❌ Please enter a valid number")
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                sys.exit(0)
    
    def _run_selected_template(self, template_name, template_data):
        """Run the selected template"""
        info = template_data['info']
        automator_class = template_data['class']
        
        print(f"\n🎯 Running: {info['display_name']}")
        print(f"📁 Template: {template_name}.py")
        print("=" * 60)
        
        try:
            # Create instance of the automator class
            automator = automator_class()
            
            # Run the automation
            success = automator.run_automation()
            
            # Final status
            if success:
                print(f"\n🎉 SUCCESS! {info['display_name']} has been created!")
            else:
                print(f"\n⚠️  PARTIAL SUCCESS - Check error messages above")
                
            return success
            
        except Exception as e:
            print(f"\n❌ Error running template: {str(e)}")
            return False
    
    def run(self):
        """Main execution flow"""
        try:
            # Show available templates and get user choice
            template_name, template_data = self._display_template_menu()
            
            # Run the selected template
            success = self._run_selected_template(template_name, template_data)
            
            # Exit with appropriate code
            sys.exit(0 if success else 1)
            
        except KeyboardInterrupt:
            print("\n❌ Operation cancelled by user")
            sys.exit(1)
        except Exception as e:
            print(f"\n❌ Unexpected error: {str(e)}")
            sys.exit(1)

def main():
    """Entry point for the dynamic project manager"""
    manager = DynamicProjectManager()
    manager.run()

if __name__ == "__main__":
    main()