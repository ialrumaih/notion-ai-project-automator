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

### Common Issues

**❌ "Database not found"**
- Verify your database ID is correct
- Ensure the integration has access to your database
- Check that you're using the database ID, not the page ID

**❌ "Property not found"**
- Make sure your database has all required properties
- Check property names match exactly (case-sensitive)
- Verify property types (Select, Date, etc.)

**❌ "Unauthorized"**
- Confirm your integration token is valid
- Ensure the integration is shared with your databases
- Check token permissions in Notion integrations settings

### Debug Mode

Run with verbose output:
```bash
python main.py --debug
```

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