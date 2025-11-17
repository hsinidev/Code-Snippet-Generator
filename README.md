# Code-Snippet-Generator
A Code Automation project demonstrating the use of a local LLM (Ollama) to generate runnable code snippets in multiple languages (Python, SQL, JavaScript) based on natural language task descriptions. This project showcases dual deployment using Streamlit and PySide6.
# 🧙 Code Snippet Generator - Local LLM Automation

[![Project Status](https://img.shields.io/badge/Status-Project%201%2F100%20Complete-green?style=for-the-badge)](<YOUR-REPOSITORY-URL>)
[![LLM Backend](https://img.shields.io/badge/LLM%20Backend-Ollama%20(Local%20AI)-000000?style=for-the-badge&logo=ollama)](https://ollama.com/)
[![Desktop GUI](https://img.shields.io/badge/Desktop%20GUI-PySide6%20%2F%20Qt-blue?style=for-the-badge&logo=qt)](https://www.qt.io/)
[![Web Frontend](https://img.shields.io/badge/Web%20Frontend-Streamlit-red?style=for-the-badge&logo=streamlit)](https://streamlit.io/)

A complete, dual-deployment application demonstrating proficiency in integrating **Local Large Language Models (LLMs)** into practical engineering tools. This project automates the generation of fully runnable code snippets across multiple programming languages.

**Developed By:** Hsini Mohame (hsini.web@gmail.com)

---

## ✨ Project Highlights (Applied AI Engineering)

This project moves beyond simple chatbot functionality to showcase critical deployment skills:

* **Local & Private AI:** The system runs entirely on your local machine using the **Ollama** service (specifically the **`llama3:8b`** model), guaranteeing speed and data privacy.
* **Non-Blocking Desktop GUI:** The PySide6 application utilizes **QThread** and **Signal/Slot** mechanisms to handle the slow LLM response asynchronously, ensuring the graphical interface never freezes during generation.
* **Dual Deployment Strategy:** The same core Python logic is exposed through two distinct frontends:
    1.  A **Web URL Interface (Streamlit)** for immediate sharing and cloud demonstration.
    2.  A **Native Desktop Window (PySide6 + Dark Theme)** for a professional, resource-efficient local user experience.
* **Prompt Engineering:** The LLM is directed via a System Prompt to strictly act as a **"Professional Software Engineer,"** ensuring clean, well-commented, and runnable code output.

---

## ⚙️ Installation & Setup

### 1. Prerequisites

Ensure your system has the following running:

* **Python 3.10+**
* **Ollama Service** (Must be running in the background/system tray).
* **Required Model:** Pull the `llama3:8b` model:
    ```bash
    ollama pull llama3:8b
    ```

### 2. Project Setup

Clone the repository and install the project dependencies via `pip`.

```bash
# Clone and enter your project folder
git clone <YOUR-REPOSITORY-URL>
cd Code-Snippet-Generator 

# Install Streamlit, Ollama client, PySide6, and the dark theme library
pip install streamlit ollama pyside6 pyqtdarktheme



