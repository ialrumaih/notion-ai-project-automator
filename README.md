# 🤖 Notion AI Project Manager

**Intelligent project automation for Notion workspaces. Automatically populate your Notion databases with structured project plans, tasks, and timelines in seconds.**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Notion API](https://img.shields.io/badge/Notion%20API-2022--06--28-black.svg)](https://developers.notion.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🎯 What It Does

Transform hours of manual Notion setup into **30 seconds of automation**:

- ✅ **Auto-populate** project databases with comprehensive task lists
- ✅ **Smart relationships** between projects and tasks
- ✅ **Timeline management** with proper due dates and priorities
- ✅ **Progress tracking** that updates automatically
- ✅ **Template-based** - easily add new project types

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Notion account with integration access
- Existing Notion workspace with Projects and Tasks databases

### Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/ialrumaih/notion-ai-project-manager.git
   cd notion-ai-project-manager
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Notion integration**
   - Go to [Notion Integrations](https://www.notion.so/my-integrations)
   - Create a new **Internal Integration**
   - Copy your integration token
   - Share your databases with the integration

4. **Configure your credentials**
   ```bash
   cp .env.example .env
   # Edit .env with your actual tokens and database IDs
   ```

5. **Run the automation**
   ```bash
   python main.py
   ```

---

## 🔧 Configuration

### Getting Your Database IDs

1. Open your Notion database in a web browser
2. Copy the URL: `https://notion.so/DATABASE_ID?v=VIEW_ID`
3. Extract the `DATABASE_ID` (the long string before `?v=`)

### Environment Variables

Create a `.env` file with:

```env
NOTION_TOKEN=your_integration_token_here
PROJECTS_DATABASE_ID=your_projects_db_id
TASKS_DATABASE_ID=your_tasks_db_id
```

---

## 📋 Project Templates

### Trading AI Platform Template

The included template creates a complete **Dynamic Stock Trading AI Platform** project with:

- **Phase 1:** Exit Rule Optimization (6 tasks)
- **Phase 2:** ML Entry Signal Engine (10 tasks)
- **Phase 3:** Platform Development (8 tasks)
- **Phase 4:** Validation & Deployment (7 tasks)
- **Research:** Market Analysis (4 tasks)

**Total:** 35 structured tasks with relationships, priorities, and timelines.

### Custom Templates

Add your own project templates in `templates/`:

```python
# templates/my_project.py
def get_project_tasks():
    return [
        {
            "name": "Task Name",
            "area": "Work Area",
            "status": "Not started",
            "due_date": "2025-07-01",
            "priority": "High",
            "description": "Task description"
        },
        # Add more tasks...
    ]
```

---

## 🏗️ Database Structure

### Required Notion Properties

**Projects Database:**
- `Name` (Title)
- `Area` (Select)
- `Status` (Select) 
- `Due Date` (Date)
- `Priority` (Select)
- `Total Tasks` (Rollup from Tasks)
- `Completed Tasks` (Rollup from Tasks)
- `Progress %` (Formula)

**Tasks Database:**
- `Name` (Title)
- `Related Project` (Relation to Projects)
- `Area` (Select)
- `Status` (Select)
- `Due Date` (Date)
- `Priority` (Select)
- `Description` (Rich Text)
- `Is Done` (Formula: if Status = "Done", 1, 0)

---

## 📊 Features

### ⚡ Smart Automation
- **Relationship Management:** Automatically links tasks to projects
- **Progress Tracking:** Rollup formulas update completion percentages
- **Timeline Intelligence:** Respects dependencies and critical paths
- **Priority Assignment:** Based on project phase and importance

### 🎯 Template System
- **Extensible:** Easy to add new project types
- **Configurable:** Adjust timelines, priorities, and descriptions
- **Reusable:** Same template works for multiple projects

### 🔒 Safe & Reliable
- **Non-destructive:** Only adds new content, never modifies existing
- **Error Handling:** Graceful failures with clear error messages
- **Validation:** Checks database structure before automation

---

## 🎨 Customization

### Adding New Project Types

1. Create a new template file in `templates/`
2. Define your task structure
3. Import and use in `main.py`

```python
# Example: templates/web_development.py
def get_web_dev_tasks():
    return [
        {
            "name": "Set up development environment",
            "area": "Development",
            "status": "Not started",
            "due_date": "2025-07-01",
            "priority": "High",
            "description": "Initialize project with proper tooling"
        }
        # More tasks...
    ]
```

### Modifying Task Properties

Edit the task creation logic in `main.py` to match your specific Notion setup:

```python
task_data = {
    "parent": {"database_id": self.tasks_db_id},
    "properties": {
        "Name": {"title": [{"text": {"content": task["name"]}}]},
        "Your Custom Property": {"select": {"name": task["custom_field"]}},
        # Add your specific properties...
    }
}
```

---

## 🔍 Troubleshooting

### Common Issues & Solutions

#### **❌ "API token is invalid" (401 Error)**

**Symptoms:**
```
❌ Connection failed: 401
Error: {"object":"error","status":401,"code":"unauthorized","message":"API token is invalid."}
```

**Solutions:**
1. **Verify integration token**:
   - Go to [Notion Integrations](https://www.notion.so/my-integrations)
   - Ensure your integration is **Active**
   - Copy a fresh token

2. **Check workspace selection**:
   - Make sure integration was created for the correct workspace
   - Delete and recreate if wrong workspace selected

3. **Test connection**:
   ```bash
   # Create test_connection.py
   import requests
   from dotenv import load_dotenv
   import os

   load_dotenv()
   token = os.getenv('NOTION_TOKEN')
   headers = {
       "Authorization": f"Bearer {token}",
       "Content-Type": "application/json",
       "Notion-Version": "2022-06-28"
   }
   response = requests.get("https://api.notion.com/v1/users/me", headers=headers)
   print(f"Status: {response.status_code}")
   print(f"Response: {response.text}")
   ```

#### **❌ "Could not find page" (404 Error)**

**Symptoms:**
```
❌ Could not find page with ID: xxx. Make sure the relevant pages and databases are shared with your integration.
```

**Solutions:**
1. **Share databases with integration**:
   - Go to each database in Notion
   - Click "Share" → "Add people, emails, or integrations"
   - Add your integration

2. **Test database access**:
   ```bash
   # Create debug_databases.py
   import os
   import requests
   from dotenv import load_dotenv

   load_dotenv()
   token = os.getenv('NOTION_TOKEN')
   headers = {
       "Authorization": f"Bearer {token}",
       "Content-Type": "application/json",
       "Notion-Version": "2022-06-28"
   }

   projects_id = os.getenv('PROJECTS_DATABASE_ID')
   tasks_id = os.getenv('TASKS_DATABASE_ID')

   print("Testing Projects database...")
   response = requests.get(f"https://api.notion.com/v1/databases/{projects_id}", headers=headers)
   print(f"Projects: {response.status_code}")

   print("Testing Tasks database...")  
   response = requests.get(f"https://api.notion.com/v1/databases/{tasks_id}", headers=headers)
   print(f"Tasks: {response.status_code}")
   ```

#### **❌ "Status is expected to be status" (400 Error)**

**Symptoms:**
```
❌ Status is expected to be status.
```

**Solutions:**
1. **Check property types in your database**:
   - Status properties use `"status"` not `"select"`
   - Other properties (Area, Priority) use `"select"`

2. **Verify exact status option names**:
   ```bash
   # Create test_status.py
   import os
   import requests
   from dotenv import load_dotenv

   load_dotenv()
   token = os.getenv('NOTION_TOKEN')
   tasks_db_id = os.getenv('TASKS_DATABASE_ID')
   headers = {
       "Authorization": f"Bearer {token}",
       "Content-Type": "application/json",
       "Notion-Version": "2022-06-28"
   }

   response = requests.get(f"https://api.notion.com/v1/databases/{tasks_db_id}", headers=headers)
   db_info = response.json()
   status_property = db_info['properties']['Status']
   print("Available status options:")
   for option in status_property['status']['options']:
       print(f"- '{option['name']}'")
   ```

3. **Update task templates** to match exact spelling:
   - Common variations: `"Not started"` vs `"Not Started"`
   - Case sensitivity: `"In progress"` vs `"In Progress"`

#### **❌ Integration Not Showing in Share Menu**

**Symptoms:**
- Integration doesn't appear when clicking "Share" on databases

**Solutions:**
1. **Recreate integration**:
   - Delete current integration
   - Create new one with **correct workspace**
   - Ensure it's **Internal** type

2. **Check workspace match**:
   - Integration workspace must match database workspace
   - Verify in integration settings

#### **❌ "Project not found"**

**Symptoms:**
```
❌ Trading AI project not found!
```

**Solutions:**
1. **Check project name**:
   - Must contain "Dynamic Stock Trading" in the title
   - Case sensitive search

2. **Debug project search**:
   ```bash
   # Create debug_project.py
   import os
   import requests
   from dotenv import load_dotenv

   load_dotenv()
   token = os.getenv('NOTION_TOKEN')
   projects_db_id = os.getenv('PROJECTS_DATABASE_ID')
   headers = {
       "Authorization": f"Bearer {token}",
       "Content-Type": "application/json",
       "Notion-Version": "2022-06-28"
   }

   response = requests.post(
       f"https://api.notion.com/v1/databases/{projects_db_id}/query",
       headers=headers,
       json={
           "filter": {
               "property": "Name",
               "title": {"contains": "Dynamic Stock Trading"}
           }
       }
   )

   print(f"Query status: {response.status_code}")
   if response.status_code == 200:
       results = response.json().get('results', [])
       if results:
           project = results[0]
           print(f"✅ Found project!")
           print(f"Project ID: {project['id']}")
           print(f"Project Name: {project['properties']['Name']['title'][0]['text']['content']}")
       else:
           print("❌ No project found with 'Dynamic Stock Trading' in name")
   else:
       print(f"Error: {response.text}")
   ```

### Debug Scripts

The following debug scripts help isolate issues:

| Script | Purpose | When to Use |
|--------|---------|-------------|
| `test_connection.py` | Verify API token works | 401 Unauthorized errors |
| `debug_databases.py` | Check database access | 404 Not found errors |
| `debug_project.py` | Verify project finding | Project not found errors |
| `test_status.py` | Check status options | Status validation errors |
| `test_single_task.py` | Test task creation | Task creation failures |

### Environment Setup Issues

#### **❌ Missing Environment Variables**

**Symptoms:**
```
❌ Missing required environment variables!
```

**Solutions:**
1. **Create .env file** in project root
2. **Copy from .env.example** and fill in values
3. **Check .env format**:
   ```bash
   NOTION_TOKEN=your_token_here
   PROJECTS_DATABASE_ID=your_projects_id
   TASKS_DATABASE_ID=your_tasks_id
   ```

#### **❌ Dependencies Not Installed**

**Symptoms:**
```
ModuleNotFoundError: No module named 'requests'
```

**Solutions:**
```bash
pip install -r requirements.txt
```

### Performance Tips

- **Large projects**: The script handles 31 tasks in ~30 seconds
- **Rate limiting**: Notion API allows ~3 requests/second
- **Error recovery**: Script continues on individual task failures
- **Cleanup**: Script automatically removes test tasks

### Getting Help

If you encounter issues not covered here:

1. **Run debug scripts** to isolate the problem
2. **Check Notion integration settings** 
3. **Verify database properties** match expectations
4. **Create an issue** with debug script output

---

## 🎉 Success Stories

### Dynamic Stock Trading AI Platform

**Project**: Complete ML trading system for Saudi stock market  
**Tasks Added**: 31 comprehensive tasks across 4 phases  
**Time Saved**: ~4 hours of manual Notion setup  
**Result**: Fully structured project with automatic progress tracking  

**Phases Automated**:
- ✅ **Phase 1**: Universal Exit Rule Framework (6 tasks)
- ✅ **Phase 2**: ML Entry Signal Engine (10 tasks)  
- ✅ **Phase 3**: Platform Development (8 tasks)
- ✅ **Phase 4**: Validation & Deployment (7 tasks)

*"Transformed hours of manual setup into 30 seconds of automation!"* - Project Creator

---

## 🤝 Contributing

We welcome contributions! Here's how:

1. **Fork the repository**
2. **Create a feature branch**
3. **Add your project template** or improvement
4. **Test thoroughly**
5. **Submit a pull request**

### Template Contributions

Share your project templates! Popular submissions will be included in the main repository.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Notion API** - For providing excellent developer tools
- **Trading AI Community** - For inspiration and testing
- **Open Source Contributors** - For making this project better

---

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/ialrumaih/notion-ai-project-manager/issues)
- **Discussions:** [GitHub Discussions](https://github.com/ialrumaih/notion-ai-project-manager/discussions)
- **Email:** ibrahem@trymyanalysis.com

---

**⭐ If this project helps you, please give it a star! It helps others discover the tool.**

---

## 🔮 Roadmap

- [ ] **GUI Interface** - No-code project setup
- [ ] **More Templates** - Software development, research, business
- [ ] **Advanced Scheduling** - Dependency management, resource allocation
- [ ] **Multi-workspace** - Support for multiple Notion workspaces
- [ ] **Import/Export** - Backup and restore project configurations
- [ ] **Team Collaboration** - Multi-user project coordination

---

*Built with ❤️ for the Notion community*