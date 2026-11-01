import streamlit as st
from google import genai
from google.genai import types
import time

# Page Configuration
st.set_page_config(page_title="HEISENBUG AI", page_icon="🖥️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;500;700&display=swap');
    
    /* Base Font */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Headers - Nothing Monospace Style */
    h1, h2, h3 {
        font-family: 'Space Mono', monospace !important;
        text-transform: uppercase;
        letter-spacing: -1px;
    }
    
    /* Custom Widget Buttons (Nothing Red Accent) */
    .stButton>button {
        border: 2px solid #ff0000 !important;
        border-radius: 8px !important;
        background-color: transparent !important;
        color: #ff0000 !important;
        font-family: 'Space Mono', monospace !important;
        font-weight: bold;
        transition: 0.3s ease;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #ff0000 !important;
        color: #ffffff !important;
        box-shadow: 4px 4px 0px rgba(255,0,0,0.3);
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        border-right: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation & Socials
st.sidebar.title("HEISENBUG_OS")
st.sidebar.markdown("`v1.0.0 // STATUS: ONLINE`")
st.sidebar.markdown("---")

# Navigation Menu
page = st.sidebar.radio(
    "SYSTEM_MENU",
    ["[01] THE HEALER", "[02] ABOUT_US", "[03] ORIGIN_STORY"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### CONNECT_")
st.sidebar.markdown("🔴 [Instagram](https://instagram.com/Shashwat.tripathi.18)")
st.sidebar.markdown("🔴 [LinkedIn](https://linkedin.com/in/shashwat-tripathi)")
st.sidebar.markdown("🔴 [GitHub](https://github.com/ShashwatTripathi08)")

# PAGE 1: THE MAIN TOOL
if page == "[01] THE HEALER":
    st.title("Syntax Healer_")
    st.markdown("**No more crying over semicolons ruined by bad library scanners.** Upload your chaotic textbook PDF, and let the agent extract and repair the logic.")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### INITIALIZE_")
        api_key = st.text_input("ENTER_GEMINI_KEY", type="password", placeholder="AQ.xxx...")
        uploaded_file = st.file_uploader("DROP_FILE_HERE", type=["pdf"])
        
    with col2:
        st.markdown("### TERMINAL_OUTPUT")
        if st.button("EXECUTE_REPAIR_SEQUENCE"):
            if not api_key or not uploaded_file:
                st.warning("SYSTEM ERROR: Awaiting API Key and PDF file.")
            else:
                with st.spinner("Compiling logic... healing syntax..."):
                    try:
                        client = genai.Client(api_key=api_key)
                        
                        pdf_bytes = uploaded_file.read()
                        pdf_part = types.Part.from_bytes(
                            data=pdf_bytes,
                            mime_type="application/pdf"
                        )
                        
                        prompt = """
                        You are an academic syntax healer. Read this scanned programming document.
                        1. Extract the theoretical definitions into bullet points.
                        2. Find all C or Java code snippets.
                        3. Fix any OCR punctuation errors (e.g., colons instead of semicolons, broken braces).
                        4. Output everything in clean Markdown format with proper code blocks.
                        """
                        
                        response = client.models.generate_content(
                            model="gemini-3.8-flash",
                            contents=[prompt, pdf_part]
                        )
                        
                        st.success("SEQUENCE_COMPLETE")
                        st.markdown("---")
                        st.markdown(response.text)
                        
                    except Exception as e:
                        st.error(f"FATAL_ERROR: {e}")

# PAGE 2: ABOUT US
elif page == "[02] ABOUT_US":
    st.title("Who We Are_")
    st.markdown("### The Builders")
    st.markdown("""
    We are a couple of first-year CSE AI/ML students navigating the chaos of Mumbai commutes, engineering mechanics, and endless lab assignments. 
    
    **Shashwat Tripathi**  
    *Co-Founder & Logic Wrangler*  
    
    **Gautam Verma**  
    *Co-Founder & System Architect*  
    
    We built this because we were tired of staring at blurry PDFs trying to figure out if it was a pointer asterisk or just a smudge on the scanner.
    """)

# PAGE 3: ORIGIN STORY
elif page == "[03] ORIGIN_STORY":
    st.title("Project: Genesis_") 
    st.markdown("""
    ### The Ziro Digital Hackathon 2026
    
    This whole thing started as a challenge. Our programming skills teacher told us to register for the **National-Level Agentic AI Hackathon** hosted by Ziro.Digital just for the "experience." We barely knew how to write a boilerplate Java function, let alone build an AI agent.
    
    But Ziro.Digital's mandate was clear: *Build AI agents that solve real problems. Move beyond prompts and build multi-step work.*
    
    So, instead of building a generic chatbot, we built a **Healer**. We took the absolute worst part of our daily academic life—studying coding from terribly scanned local textbooks—and engineered an agent to fix it. 
    
    We went from zero cloud experience to deploying a multimodal Agentic AI pipeline in 4 days. 
    """)
