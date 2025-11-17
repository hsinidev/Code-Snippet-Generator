import sys
import threading
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QLabel, QTextEdit, QPushButton, QComboBox, QMessageBox)
from PySide6.QtCore import QThread, Signal, Slot, Qt
import ollama
import qdarktheme # The module inside pyqtdarktheme package

# --- Configuration ---
OLLAMA_MODEL = 'llama3:8b'
DEV_INFO = "powrd by Hsini Mohame (hsini.web@gmail.com)"

# --- 1. Worker Thread Class for Ollama Call ---
class OllamaWorker(QThread):
    finished = Signal(str)
    error = Signal(str)

    def __init__(self, lang, desc):
        super().__init__()
        self.lang = lang
        self.desc = desc

    def run(self):
        """Runs the long-running Ollama API call in a separate thread."""
        system_prompt = (
            f"You are a professional software engineer specialized in {self.lang}. "
            f"Your task is to generate clean, commented, and fully runnable code based on the user's description. "
            f"Output ONLY the code block. DO NOT include any introductory or concluding text."
        )
        user_prompt = f"Generate the {self.lang} code for the following description: {self.desc}"

        try:
            # Call the Ollama API
            response = ollama.generate(
                model=OLLAMA_MODEL, 
                prompt=user_prompt,
                system=system_prompt
            )
            self.finished.emit(response['response'])
        except Exception as e:
            self.error.emit(f"Error: Ensure Ollama is running and model '{OLLAMA_MODEL}' is pulled. Detail: {e}")

# --- 2. Main Application Window ---
class CodeGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("?? Code Snippet Generator (Local)")
        self.setGeometry(100, 100, 750, 700) 

        self.setup_ui()

    def setup_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Developer Info
        self.layout.addWidget(QLabel(DEV_INFO))
        self.layout.addWidget(QLabel("---"))

        # Language Selector
        self.lang_selector = QComboBox()
        self.lang_options = ["Python", "SQL", "JavaScript", "Bash", "Java", "C++"]
        self.lang_selector.addItems(self.lang_options)
        self.layout.addWidget(QLabel("Select Language:"))
        self.layout.addWidget(self.lang_selector)

        # Description Input
        self.layout.addWidget(QLabel("Describe the function or code you need:"))
        self.desc_input = QTextEdit()
        self.desc_input.setPlaceholderText("e.g., A Python function to read a CSV file using the 'csv' module and return a list of dictionaries.")
        self.desc_input.setFixedHeight(120)
        self.layout.addWidget(self.desc_input)

        # Generate Button
        self.generate_button = QPushButton("Generate Code Snippet")
        self.generate_button.clicked.connect(self.start_generation)
        self.layout.addWidget(self.generate_button)

        # Status Label
        self.status_label = QLabel("Status: Ready. Powered by Ollama.")
        self.layout.addWidget(self.status_label)

        # Code Output
        self.layout.addWidget(QLabel("Generated Code:"))
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.layout.addWidget(self.output_text)

    @Slot()
    def start_generation(self):
        """Starts the LLM generation process in a non-blocking thread."""
        lang = self.lang_selector.currentText()
        desc = self.desc_input.toPlainText().strip()

        if not desc:
            QMessageBox.warning(self, "Input Error", "Please enter a description for the code.")
            return

        # Disable GUI elements and set status
        self.generate_button.setText("Generating... Please Wait")
        self.generate_button.setEnabled(False)
        self.output_text.setText("")
        self.status_label.setText(f"Status: Generating {lang} code...")

        # Start the worker thread
        self.worker = OllamaWorker(lang, desc)
        self.worker.finished.connect(self.handle_llm_result)
        self.worker.error.connect(self.handle_llm_error)
        self.worker.start()

    @Slot(str)
    def handle_llm_result(self, result):
        """Updates the GUI with the result from the background thread."""
        self.output_text.setText(result)
        self.reset_status()

    @Slot(str)
    def handle_llm_error(self, error_message):
        """Handles errors from the background thread."""
        QMessageBox.critical(self, "Ollama Error", error_message)
        self.reset_status()
        
    def reset_status(self):
        """Resets the UI elements after processing."""
        self.generate_button.setText("Generate Code Snippet")
        self.generate_button.setEnabled(True)
        self.status_label.setText("Status: Ready. Powered by Ollama.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # --- Apply the Dark Theme ("Dark Magic Interface") ---
    qdarktheme.setup_theme("dark") # This sets the full dark theme
    
    window = CodeGeneratorApp()
    window.show()
    sys.exit(app.exec())