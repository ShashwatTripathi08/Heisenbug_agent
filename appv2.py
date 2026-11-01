import streamlit as st
from google import genai
import time

# 1. Setup the Webpage UI
st.set_page_config(page_title="Heisenbug AI", page_icon="🐛")
st.title("Heisenbug AI: PDF Syntax Healer")
st.write("Upload a messy programming PDF. The AI will extract, clean, and fix the code.")

# 2. API Key Input
api_key = st.text_input("Enter Gemini API Key:", type="password")

# 3. The File Upload Button
uploaded_file = st.file_uploader("Upload Scanned PDF", type=["pdf"])

# 4. The Core Agent Logic
if st.button("Clean Document") and uploaded_file and api_key:
    with st.spinner("Agent is reading the PDF and healing syntax..."):
        try:
            # Initialize the Google AI client
            client = genai.Client(api_key=api_key)
            
            # Save the uploaded file temporarily
            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.read())
            
            # Upload the file to Google's servers
            ai_file = client.files.upload(file="temp.pdf")
            
            # Wait for 5 seconds to let Google process the PDF visuals
            time.sleep(5)
            
            # THE PROMPT
            prompt = """
            You are an academic syntax healer. Read this scanned programming document.
            1. Extract the theoretical definitions into bullet points.
            2. Find all C or Java code snippets.
            3. Fix any OCR punctuation errors (e.g., colons instead of semicolons, broken braces).
            4. Output everything in clean Markdown format with proper code blocks.
            """
            
            # Generate the response using the latest Gemini 2.0 Flash model
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[prompt, ai_file]
            )
            
            # 5. Display the final output
            st.success("Analysis Complete!")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
