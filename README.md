# My Text Editor

A lightweight, dark-themed code editor built with Python and Tkinter, inspired by the minimalist aesthetic of Sublime Text. Designed for simplicity and focus.

---

## Features

- **Smart Auto-Indentation:** Automatically indents the next line, with an extra level of indentation after colons (`:`), making it perfect for Python and other block-based languages.
- **Dynamic Zooming:** Quickly adjust text size using keyboard shortcuts or your mouse wheel for better readability.
- **File Management:** Essential tools for creating, opening, saving, and "saving as" files.
- **Modern Aesthetic:** A sleek dark-blue interface with high-contrast white text and custom font support.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/text-editor.git
cd text_editor
```

### 2. Install dependencies
This project uses `tkextrafont` to ensure a consistent experience across different systems.
```bash
pip install -r requirements.txt
```

### 3. Font Setup
Ensure that your preferred font file (e.g., `FiraCode-Light.ttf`) is placed in the root directory alongside `text_editor.py`.

---

## Shortcuts

| Action | Shortcut |
| :--- | :--- |
| **New File** | `Ctrl + N` |
| **Open File** | `Ctrl + O` |
| **Save File** | `Ctrl + S` |
| **Zoom In** | `Ctrl + +` or `Ctrl + =` |
| **Zoom Out** | `Ctrl + -` |
| **Zoom (Mouse)** | `Ctrl + MouseWheel` |

---

## Built With

- **Python 3**
- **Tkinter** (Standard GUI Library)
- **tkextrafont** (For custom font handling)

## Future Enhancements (T.B.D)
- [ ] Syntax highlighting for Python.
- [ ] Unsaved changes indicator.
- [ ] "Save before closing" prompts.
- [ ] Customizable theme settings.
