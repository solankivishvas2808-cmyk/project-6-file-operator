# 📔 Personal Journal Manager

> **A simple, reliable, menu-driven Python application for creating, viewing, searching, and deleting personal journal entries.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Interface](https://img.shields.io/badge/Interface-CLI-black)
![Storage](https://img.shields.io/badge/Storage-Text%20File-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📌 Project Overview

**Personal Journal Manager** is a command-line Python application designed to manage journal entries using a plain text file.

The application provides a clear menu with five operations:

1. **Add New Entry**
2. **View All Entries**
3. **Search Entry**
4. **Delete All Entries**
5. **Exit**

Journal information is stored in `journal.txt`. New entries are saved with the current date and time.

---

## 🎯 Project Objective

The main objective of this project is to demonstrate practical Python programming concepts through a small, usable application.

### Key objectives

- Build a menu-driven Python program.
- Store information permanently using file handling.
- Add date and time to journal entries.
- Read and display stored data.
- Search journal content using keywords.
- Delete stored entries after confirmation.
- Handle common file-related errors safely.

---

## ✨ Features

| Feature | Description |
|---|---|
| ➕ Add Entry | Creates a new journal entry and stores its date/time |
| 📖 View Entries | Reads and displays all stored journal data |
| 🔍 Search Entry | Finds matching journal lines using a keyword |
| 🗑️ Delete Entries | Clears all journal data after confirmation |
| 🚪 Exit | Safely exits the application |
| 🛡️ Error Handling | Handles missing files and permission/file-access errors |
| ⏰ Date & Time | Automatically records `datetime.now()` for new entries |

---

## 🧠 Python Concepts Demonstrated

This project demonstrates the following concepts from the source program:

- `import`
- `datetime`
- `while` loop
- `if / elif / else`
- `input()`
- String methods such as `lower()` and `split()`
- File opening modes:
  - `"a"` — append
  - `"r"` — read
  - `"w"` — write/clear
- `read()`
- `write()`
- `close()`
- `try / except`
- `PermissionError`
- `OSError`
- `FileNotFoundError`
- `break`

---

## 🔄 Program Workflow

```text
                 ┌─────────────────────┐
                 │       START         │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │    Display Menu     │
                 └──────────┬──────────┘
                            ↓
                  ┌───────────────────┐
                  │  User selects     │
                  │     option        │
                  └─────────┬─────────┘
                            ↓
        ┌──────────┬────────┼────────┬──────────┐
        ↓          ↓        ↓        ↓          ↓
      Add       View      Search    Delete     Exit
        │          │        │        │          │
        └──────────┴────────┴────────┴──────────┘
                            ↓
                     Display Menu Again
                            │
                            └───────→ until Exit
```

---

# 📸 Screenshots

## 1. Main Menu

![Main Menu](01_main_menu.png)

The application starts with a clean five-option menu.

---

## 2. Add New Entry

![Add Entry](02_add_entry.png)

The user can enter a journal entry. The program records the current date and time and saves the entry into `journal.txt`.

---

## 3. View All Entries

![View Entries](03_view_entries.png)

The View option reads the journal file and displays the stored entries.

---

## 4. Search Entry

![Search Entry](04_search_entry.png)

The Search option accepts a keyword and checks the stored journal data using a case-insensitive comparison.

---

## 5. Delete Confirmation

![Delete Confirmation](05_delete_cancel.png)

Before deleting all entries, the program asks the user for confirmation.

---

# 💾 Data Storage Format

Entries are stored in `journal.txt` in a readable format:

```text
Date: <current date and time>
Entry: <journal entry>
------------------------------
```

The program uses append mode when adding entries, so existing journal data is not overwritten.

---

# 🔍 Search Logic

The search operation works in a simple sequence:

```text
User enters keyword
        ↓
Open journal.txt
        ↓
Read complete file
        ↓
Convert keyword/data to lowercase
        ↓
Split data into lines
        ↓
Check each line
        ↓
Display matching line(s)
```

Because the program uses `.lower()`, the keyword comparison is case-insensitive.

---

# 🛡️ Error Handling

The program includes exception handling for file operations.

### `FileNotFoundError`

Used when the journal file does not exist while trying to read or search it.

### `PermissionError`

Used when the program does not have permission to access the file.

### `OSError`

Used for general file-access errors during the Add Entry operation.

### Empty Entry Validation

The program also checks whether the user entered an empty journal entry and prevents it from being saved.

---

# 📂 Project Structure

```text
Personal-Journal-Manager/
│
├── project.6.py
├── journal.txt
├── README.md
│
└── screenshots/
    ├── 01_main_menu.png
    ├── 02_add_entry.png
    ├── 03_view_entries.png
    ├── 04_search_entry.png
    └── 05_delete_cancel.png
```

> `journal.txt` is the data file used by the application and can be created/updated while the program runs.

---

# ⚙️ Requirements

### Software

- Python 3.x
- VS Code / Terminal / any Python-compatible IDE

### Python Library

The project uses Python's built-in `datetime` module.

No external package installation is required.

---

# ▶️ How to Run

### Step 1 — Open the project

Open the project folder in VS Code.

### Step 2 — Open the terminal

Run:

```bash
python3 project.6.py
```

On Windows, you can also use:

```bash
python project.6.py
```

### Step 3 — Select an option

Example:

```text
Enter your choice: 1
```

Then enter the journal entry when requested.

---

# 🧪 Example Usage

```text
==============================
Personal Journal Manager
==============================
1. Add New Entry
2. View All Entries
3. Search Entry
4. Delete All Entries
5. Exit

Enter your choice: 1
Enter your journal entry: College project journal entry
Entry added successfully.
```

---

# 📊 Feature Summary

| Category | Implementation |
|---|---|
| User Interface | Command-line menu |
| Data Input | `input()` |
| Data Storage | `journal.txt` |
| Add Data | File append mode |
| Read Data | File read mode |
| Delete Data | File write mode |
| Search | `lower()` + `split()` |
| Timestamp | `datetime.now()` |
| Validation | Empty-entry check |
| Exceptions | `try / except` |
| Program Loop | `while True` |

---

# 🎓 Learning Outcomes

After completing this project, a student can demonstrate an understanding of:

- Basic Python program structure
- Menu-driven application design
- Conditional statements
- Loops
- String processing
- File handling
- Date and time handling
- Exception handling
- User input validation
- Basic persistent data storage

---

# 🚀 Future Enhancements

Possible improvements for a future version:

- 🔐 Password protection
- 🗃️ Separate files for different users
- ✏️ Edit existing journal entries
- 📅 Search entries by date
- 🏷️ Add categories/tags
- 🎨 Build a graphical user interface
- 💾 Use SQLite instead of a text file
- 📤 Export journal entries
- 🔎 Show complete matching entries instead of matching lines only

> These are proposed future improvements and are **not part of the current implementation**.

---

# 👨‍💻 Project Information

**Project:** Personal Journal Manager  
**Language:** Python 3  
**Application Type:** Command-Line Application  
**Storage:** Text File  
**Level:** Beginner / Academic Python Project

---

## ⭐ Conclusion

**Personal Journal Manager** is a compact Python project that combines user interaction, menu-driven programming, file handling, searching, date/time functionality, and exception handling into one practical application.

It provides a strong beginner-level demonstration of how Python can be used to build a simple data-management utility.

---

<div align="center">

### 📔 Personal Journal Manager

**Built with Python • File Handling • Exception Handling**

</div>
