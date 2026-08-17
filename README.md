# ⭐ Personal Journal Manager

<p align="center">
  <strong>A simple, practical and user-friendly console-based Journal Management application built with Python.</strong>
</p>

<p align="center">
  🐍 Python &nbsp;•&nbsp; 🧱 OOP &nbsp;•&nbsp; 📁 File Handling &nbsp;•&nbsp; 🛡️ Exception Handling
</p>

---

## 📌 About the Project

**Personal Journal Manager** is a Python console application created to demonstrate how fundamental Python concepts can be combined to build a complete, practical application.

The application provides a simple way to **create, store, view, search and delete personal journal entries** using persistent text-file storage.

It is designed as a learning project with a focus on **Python File Handling, Object-Oriented Programming, Input Validation and Exception Handling**.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 📝 **Create Entry** | Add a new personal journal entry |
| 👀 **View Entries** | Display saved journal entries |
| 🔍 **Search** | Find journal entries using search functionality |
| 🗑️ **Delete** | Remove individual journal entries |
| 💾 **Persistent Storage** | Keep journal data inside a text file |
| 🛡️ **Input Validation** | Handle invalid or unexpected user input |
| ⚠️ **Exception Handling** | Prevent common runtime errors |
| 📋 **Menu-Driven UI** | Easy-to-use console interface |
| 🧱 **OOP Design** | Organized using a `JournalManager` class |

---

## 🧠 Concepts Demonstrated

This project practically implements the following Python concepts:

```text
Python Programming
        ↓
Object-Oriented Programming
        ↓
File Handling
        ↓
File I/O Operations
        ↓
Exception Handling
        ↓
Input Validation
        ↓
Menu-Driven Application
        ↓
Persistent Text-Based Storage
```

### 🐍 Python Programming
Variables, data types, operators, conditions, loops, functions, input/output and built-in functions.

### 🧱 Object-Oriented Programming
The `JournalManager` class provides a structured and maintainable design for journal operations.

### 📁 File Handling

The project demonstrates the commonly used file modes:

| Mode | Purpose |
|---|---|
| `r` | Read existing file data |
| `w` | Write/overwrite file data |
| `a` | Append new data |
| `x` | Create a new file |

### ⚠️ Exception Handling
Runtime and input-related errors are handled so the application can continue running safely.

### 🛡️ Input Validation
User input is checked before processing to reduce invalid operations.

---

## 🔄 Application Workflow

```text
                    ┌───────────────┐
                    │     START     │
                    └───────┬───────┘
                            ↓
                    ┌───────────────┐
                    │   MAIN MENU   │
                    └───────┬───────┘
                            ↓
          ┌─────────────────┼─────────────────┐
          ↓                 ↓                 ↓
       CREATE             VIEW              SEARCH
          │                 │                 │
          └─────────────────┼─────────────────┘
                            ↓
                         DELETE
                            ↓
                    ┌───────────────┐
                    │  TEXT FILE    │
                    │   STORAGE     │
                    └───────┬───────┘
                            ↓
                    ┌───────────────┐
                    │   MAIN MENU   │
                    └───────┬───────┘
                            ↓
                          EXIT
```

---

## 🛠️ Technology Stack

- **Language:** Python 3
- **Interface:** Console / Terminal
- **Storage:** Text File
- **Programming Style:** Object-Oriented Programming
- **Core Concepts:** File I/O, Exception Handling, Input Validation

---

## 🚀 How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

### 2. Clone the Repository

```bash
git clone <your-repository-url>
```

### 3. Open the Project

```bash
cd Personal-Journal-Manager
```

### 4. Run the Application

```bash
python journal_manager.py
```

> Replace `journal_manager.py` with your actual Python filename if it is different.

---

## 📂 Project Structure

```text
Personal-Journal-Manager/
│
├── 📄 journal_manager.py
├── 📄 journal.txt
├── 📄 README.md
│
└── 📁 screenshots/
    ├── 01-main-menu.jpg
    ├── 02-sample-execution.jpg
    ├── 03-view-search-delete.jpg
    ├── 04-search-delete-invalid.jpg
    ├── 05-features-how-to-run.jpg
    ├── 06-project-structure.jpg
    ├── 07-requirements-checklist.jpg
    ├── 08-future-enhancements-learning.jpg
    ├── 09-learning-outcomes.jpg
    ├── 10-author-conclusion.jpg
    ├── 11-acknowledgement.jpg
    ├── 12-conclusion.jpg
    ├── 13-limitations-future.jpg
    ├── 14-assumptions.jpg
    └── 15-full-project-preview.jpg
```

---

## 📚 Learning Outcomes

Through this project, the following concepts were practically implemented:

- Python programming fundamentals
- Object-Oriented Programming
- File Handling
- File I/O operations
- Exception Handling
- Input Validation
- Menu-driven application development
- Persistent text-based storage
- Problem-solving and application design

The project helped demonstrate how individual Python concepts can be combined to create a **complete and functional application**.

---

## 🔮 Future Enhancements

The current application can be further improved with:

- 🔐 Password Protection
- ✏️ Edit Individual Entries
- 🗑️ Advanced Delete Options
- 📅 Date-Range Searching
- 🏷️ Entry Categories
- 😊 Mood Tracking
- 📊 Journal Statistics
- 📤 Export Functionality
- 🔒 File Encryption
- 🗄️ SQLite Database Integration
- 🖥️ GUI Version
- 🌐 Web-Based Version

---

## 📸 More Project Documentation

🏠 01 — Main Menu
<img width="826" height="453" alt="WhatsApp Image 2026-08-17 at 15 53 35" src="https://github.com/user-attachments/assets/f255cbcc-cc99-47e6-a938-dc887e281b0c" />



📝 02 — Add New Entry
<img width="1599" height="625" alt="WhatsApp Image 2026-08-17 at 15 53 35 (1)" src="https://github.com/user-attachments/assets/9c2e70dc-8a44-4677-8838-bae7c92451ee" />



📖 03 — View All Entries
<img width="1213" height="407" alt="WhatsApp Image 2026-08-17 at 15 53 35 (2)" src="https://github.com/user-attachments/assets/60113af5-3494-440b-885f-fba324fd43ef" />



🔍 04 Search Entry

<img width="1688" height="396" alt="WhatsApp Image 2026-08-17 at 15 53 37" src="https://github.com/user-attachments/assets/faa5147f-9fa0-4683-a185-6387d895b04c" />



✅ 05 — Delete Success

<img width="1496" height="358" alt="WhatsApp Image 2026-08-17 at 15 53 37 (1)" src="https://github.com/user-attachments/assets/470247c9-b50e-4c7b-bdac-ddda4f637ac0" />


👋 06 — Exit

<img width="1343" height="358" alt="WhatsApp Image 2026-08-10 at 22 09 11" src="https://github.com/user-attachments/assets/e0bc938d-e8bf-43e4-8420-774b9fc3b49e" />

---

## 👨‍💻 Author

### Vishwas Solanki

🎓 **b.com-f.y student**  
📊 **Data Analysis Learner**  
🐍 **Python • OOP • File Handling**

### Submitted To

**Prof. Girish Gondaliya**

---

## 🙏 Acknowledgement

I would like to sincerely thank **Prof. Girish Gondaliya** for providing valuable guidance, support and encouragement throughout the development of this project.

This project provided an opportunity to apply theoretical knowledge to a practical application and gain hands-on programming experience.

---

## 🏁 Conclusion

**Personal Journal Manager** successfully demonstrates the practical implementation of:

> **Python File Handling + Object-Oriented Programming + Exception Handling + User Input Validation**

The application provides a simple and effective way to **create, store, view, search and delete personal journal entries** using a text file.

The implementation of `r`, `w`, `a` and `x` file modes demonstrates practical file operations, while the `JournalManager` class provides a structured OOP design.

Overall, this project demonstrates how fundamental Python concepts can be combined to build a **complete, practical and user-friendly console application**.

---

<p align="center">
  ⭐ <strong>Personal Journal Manager</strong><br>
  Built with 🐍 Python
</p>

<p align="center">
  <sub>Academic / Learning Project</sub>
</p>
