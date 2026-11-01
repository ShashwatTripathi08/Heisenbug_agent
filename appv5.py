import streamlit as st
from google import genai
from google.genai import types
import time

# 1. Page Configuration
st.set_page_config(page_title="HEISENBUG // AI", page_icon="🔴", layout="wide")

# 2. Complete Nothing OS Theme & Alive Animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DotGothic16&family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;500;700&display=swap');
    
    .stApp {
        background-color: #000000;
        background-image: radial-gradient(#1A1A1A 1px, transparent 0);
        background-size: 20px 20px; 
    }
    
    html, body, [class*="css"], p, li { 
        font-family: 'Inter', sans-serif; 
        color: #FFFFFF;
    }
    
    h1, h2, h3 { 
        font-family: 'DotGothic16', sans-serif !important; 
        text-transform: uppercase; 
        letter-spacing: 2px;
        color: #FFFFFF !important;
    }
    
    /* Blinking Terminal Cursor */
    .live-title::after {
        content: '_';
        color: #E51010;
        animation: blink 1s step-end infinite;
    }
    @keyframes blink { 50% { opacity: 0; } }

    /* Breathing/Pulsing Wireframe Widget Boxes */
    .wireframe-box {
        background-color: #0F0F0F;
        border: 1px solid #333333;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 24px;
        animation: pulse 4s infinite alternate;
    }
    @keyframes pulse {
        0% { box-shadow: 0px 0px 0px rgba(229, 16, 16, 0); }
        100% { box-shadow: 0px 0px 15px rgba(229, 16, 16, 0.12); }
    }
    
    /* Tactile Nothing OS Pill Button */
    .stButton>button {
        border: 2px solid #E51010 !important;
        border-radius: 30px !important;
        background-color: transparent !important;
        color: #E51010 !important;
        font-family: 'Space Mono', monospace !important;
        font-weight: bold;
        text-transform: uppercase;
        transition: all 0.2s ease-in-out;
        width: 100%;
        box-shadow: 4px 4px 0px #E51010; 
    }
    .stButton>button:hover { 
        background-color: #E51010 !important; 
        color: #000000 !important; 
        box-shadow: 0px 0px 0px #E51010; 
        transform: translate(4px, 4px);
    }

    section[data-testid="stSidebar"] {
        border-right: 1px solid #222222;
        background-color: #050505;
    }
    
    .footer { 
        font-family: 'Space Mono', monospace; 
        font-size: 0.75rem; 
        color: #808080; 
        text-align: center; 
        padding-top: 30px; 
        text-transform: uppercase; 
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar: Table of Content & Live Socials
st.sidebar.title("HEISENBUG_OS")
st.sidebar.markdown("`v1.0.0 // STATUS: ONLINE`")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "TABLE_OF_CONTENTS",
    ["[01] THE HEALER", "[02] ABOUT_US", "[03] ORIGIN_STORY"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### CONNECT_")
st.sidebar.markdown("🔴 [Instagram](https://instagram.com/shashwat.tripathi18)")
st.sidebar.markdown("🔴 [LinkedIn](https://linkedin.com/in/shashwat-tripathi)")
st.sidebar.markdown("🔴 [GitHub](https://github.com/shashwattripathi08)")

# Streaming generator for live typewriter effect
def stream_data(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.03)

# ==========================================
# PAGE 1: THE CORE TOOL (Matches your sketch)
# ==========================================
if page == "[01] THE HEALER":
    header_left, header_right = st.columns([3, 1])
    with header_left:
        st.markdown('<h1 class="live-title">HEISENBUG // AI</h1>', unsafe_allow_html=True)
        st.markdown("**No more crying over semicolons ruined by bad scanners.** Autonomously extract, clean, and heal broken code.")
    with header_right:
        st.write("")
        st.markdown("`SYSTEM STATUS: READY`")
        st.markdown("[Documentation](#) | [Report Bug](#)")

    st.markdown("---")

    # INPUT CONTAINER (From your wireframe)
    st.markdown('<div class="wireframe-box">', unsafe_allow_html=True)
    st.markdown("### INPUT_PARAMETERS")
    api_key = st.text_input("ENTER_GEMINI_KEY", type="password", placeholder="AQ.xxx...")
    uploaded_file = st.file_uploader("DROP_SCANNED_PDF_HERE", type=["pdf"])
    execute_run = st.button("EXECUTE_REPAIR_SEQUENCE")
    st.markdown('</div>', unsafe_allow_html=True)

    # OUTPUT CONTAINER (From your wireframe)
    if execute_run:
        if not api_key or not uploaded_file:
            st.warning("SYSTEM FAULT: Awaiting both Gemini API Key and Scanned PDF.")
        else:
            st.markdown('<div class="wireframe-box">', unsafe_allow_html=True)
            st.markdown("### TERMINAL_OUTPUT")
            
            with st.status("[SYS] Ingesting document & scanning for syntax flaws...", expanded=True) as status:
                try:
                    client = genai.Client(api_key=api_key)
                    pdf_bytes = uploaded_file.read()
                    pdf_part = types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf")
                    
                    prompt = """
                    You are an academic syntax healer. Read this scanned programming document.
                    1. Extract the theoretical definitions into bullet points.
                    2. Find all C or Java code snippets.
                    3. Fix any OCR punctuation errors (e.g., colons instead of semicolons, broken braces).
                    4. Output everything in clean Markdown format with proper code blocks.
                    """
                    
                    status.update(label="[AI] Reconstructing logic and repairing code...", state="running")
                    
                    response = client.models.generate_content(
                        model="gemini-3.8-flash",
                        contents=[prompt, pdf_part]
                    )
                    
                    status.update(label="[SYS] SEQUENCE COMPLETE.", state="complete")
                    
                    st.markdown("---")
                    st.write_stream(stream_data(response.text))
                    
                except Exception as e:
                    status.update(label=f"FATAL_ERROR: {e}", state="error")
            st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# PAGE 2: ABOUT US (Detailed profiles)
# ==========================================
elif page == "[02] ABOUT_US":
    st.markdown('<h1 class="live-title">WHO WE ARE_</h1>', unsafe_allow_html=True)
    st.markdown("### The Builders")
    st.markdown("""
    We are first-year CSE AI/ML students navigating Mumbai commutes, engineering mechanics, and endless lab submissions.
    
    **Shashwat Tripathi**  
    *Co-Founder & Logic Wrangler*  
    Surviving on C programming, GitHub Codespaces on an iPad, and keeping the ping stable on CODM over Wi-Fi.
    
    **[Teammate's Name]**  
    *Co-Founder & System Architect*  
    [Add a witty one-liner about your teammate here, e.g., "The one actually typing on a laptop."]
    
    ---
    ### Why We Built This
    We were tired of staring at blurry, crooked textbook scans trying to figure out if that dot on the screen was a pointer asterisk or just a smudge on the college scanner.
    """)

# ==========================================
# PAGE 3: ORIGIN STORY (Ziro Hackathon)
# ==========================================
elif page == "[03] ORIGIN_STORY":
    st.markdown('<h1 class="live-title">PROJECT: GENESIS_</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    ### The Ziro Digital Hackathon 2026
    This project started as an unexpected challenge. Our programming skills teacher told us to register for the **National-Level Agentic AI Hackathon 2026** hosted by Ziro.Digital just for the "experience." We had barely completed a month of curriculum and knew only the bare basics of C and Java.
    
    The mandate was clear: *Build AI agents that move beyond passive question answering into multi-step, autonomous execution.*
    
    Rather than building another generic chatbot wrapper, we focused on our real daily pain point—corrupted syntax in academic PDFs. In 4 days, we went from zero cloud development knowledge to deploying an end-to-end multimodal agent on GitHub Codespaces and Streamlit.
    """)

# 4. Footer (From your wireframe sketch)
st.markdown("---")
st.markdown('<p class="footer">Heisenbug AI v1.0 | Developed by Shashwat Tripathi & Team | Ziro Digital Hackathon 2026</p>', unsafe_allow_html=True)
