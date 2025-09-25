# Systems Scripting – Assignment 2

This repository contains my submission for **COMP7044 – Systems Scripting, Assignment 2**, which focused on Python scripting for tasks such as a **file system automation** and a **Zoo Management System**.

---

## Overview
The assignment required creating Python scripts that make use of:
- File and folder manipulation
- Automation with the `os` and `zipfile` modules

Which build on my knowledge of python scripting.

---

## Tasks Implemented

### **Task 1 – File System Automation**  
Script to automate folder and file operations:  
- Interactively request a folder name and recreate its structure if it exists.  
- Create subfolders in a given structure
- Populate the `docs` folder with text files and varying content.  
- Rename all `.txt` files to lowercase (preserving extension).  
- Create **five zip archive backups** of the `docs` folder in `/store`.  
- Output the contents of `/store` and verify one of the archives.  

---

### **Task 2 – Zoo Management System**  
A menu-driven Python application to manage a zoo database.  
Features:  

#### **User Account Management**
- Add **admin** and **standard** user accounts.  
- Admin-only privileges for creating/managing zoo and accounts.  
- Authentication required for sensitive operations.  
- Options: `add users`, `view users`, `delete users`, `return`.  

#### **Zoo Creation & Management**
- Admin user can create, update, or delete a zoo.  
- Menu options:
- `admin zoo`
- `view settings`

#### **Zoo Administration (for admins only)**
- `add animal`: add animal name + tag (validated).  
- `query`: search animals by tag (loop until “finish” entered).  
- `delete animal`: remove animals by tag (repeatable).  
- `exit`: return to previous menu.  

#### **Zoo Viewing (Standard users)**
- Limited to `query` and `exit`.

#### **Persistence**
- All user accounts, zoo settings, and animals are retrieved from a database file which is specified when script is launched.  

