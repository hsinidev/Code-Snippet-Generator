import streamlit as st
import ollama

# --- Configuration ---
OLLAMA_MODEL = 'llama3:8b'
DEV_INFO = "powrd by Hsini Mohame (hsini.web@gmail.com)"

# Fix: Removed 'theme' argument to support older Streamlit versions.
# This must be the very first Streamlit command.
st.set_page_config(
    page_title="Code Snippet Generator",
    layout="wide",
)

st.title("🧙 Code Snippet Generator")
st.markdown("---")

# 1. User Inputs
language_options = ["Python", "SQL", "JavaScript", "Bash", "Java", "C++"]
selected_language = st.selectbox("Select Language:", options=language_options, index=0)

description = st.text_area(
    "Describe the function or code you need:",
    placeholder=f"e.g., A {selected_language} function to read a file line by line."
)

# --- Code Generation Logic ---

def generate_code(lang, desc):
    # This System Prompt is the key to forcing the LLM's behavior
    system_prompt = (
        f"You are a professional software engineer specialized in {lang}. "
        f"Your task is to generate clean, commented, and fully runnable code based on the user's description. "
        f"Output ONLY the code block. DO NOT include any introductory or concluding text."
    )
    
    user_prompt = f"Generate the {lang} code for the following description: {desc}"
    
    try:
        # Streamlit is single-threaded, but the server handles the responsiveness
        response = ollama.generate(
            model=OLLAMA_MODEL, 
            prompt=user_prompt,
            system=system_prompt
        )
        return response['response']
        
    except Exception as e:
        return f"Error connecting to Ollama: {e}. Ensure the service is running and model '{OLLAMA_MODEL}' is pulled."


if st.button("Generate Code Snippet", type="primary"):
    if description:
        with st.spinner(f"Generating {selected_language} code with {OLLAMA_MODEL}..."):
            code_output = generate_code(selected_language, description)
            
        st.subheader(f"Generated {selected_language} Code:")
        
        # Display the code in a code block with the correct language highlighting
        st.code(code_output, language=selected_language.lower())
    else:
        st.error("Please enter a description to generate code.")

st.markdown("---")
st.caption(DEV_INFO)