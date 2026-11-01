# Heisenbug_agent
1st Hackathon Project (17th Oct 2026 - Semester 1)

 HEISENBUG AI

 THE PROBLEM
Engineering students heavily rely on poorly scanned textbook PDFs and lecture notes that suffer from severe OCR (Optical Character Recognition) degradation.
Blurred scans introduce critical syntax errors in code snippets:
1. Semicolons ⁠;⁠ become colons ⁠:⁠
2. Curly braces ⁠{}⁠ become parenthesis ⁠()⁠ or pipes ⁠|⁠
3. Indentations vanish, breaking Python logic
4. Ctrl+F⁠ searchability is destroyed.
Existing AI tools remain passive chatbots that require continuous manual prompting rather than autonomously triaging, repairing, and restructuring chaotic study materials into high-yield, verified notes.

 THE SOLUTION
Heisenbug AI is a multimodal Agentic AI pipeline. You don't ask it questions; you give it a task.
1. Upload: User drops a chaotic, low-quality scanned PDF page.
2. Ingestion: Bypassing traditional buggy OCR, the agent passes the raw file bytes directly to a multimodal vision LLM.
3. Autonomous Triage: The agent classifies extracted elements into theory, formulas, and programming syntax.
4. Syntax Healing: It autonomously repairs OCR-corrupted punctuation and broken boilerplate code.
5. Output: Generates a clean, searchable, dark-mode Markdown cheat sheet with copy-ready code blocks.

 TECH STACK

￼ Frontend UI: Streamlit (Python) - Custom styled with a brutalist/Nothing OS aesthetic.
￼ Agent Intelligence: Google Gemini 3.8 Flash API (Multimodal capabilities).

￼ Environment: GitHub Codespaces & Gitpod.

￼ File Processing: ⁠google.genai.types.Part.from_bytes⁠ (Direct memory ingestion for faster processing).
 
 HOW TO RUN LOCALLY (FOR JUDGES)
To run this agent on your own local machine or cloud environment:
1. Clone the repository
2. Install dependencies
3. Set up the API Key
You will need a free Google Gemini API key from Google AI Studio.
You can input this securely directly in the web UI when the app launches.
4. Run the Agent
The app will launch locally at ⁠http://localhost:8501⁠
 
 HACKATHON CONTEXT

Built for the National-Level Agentic AI Hackathon 2026 hosted by Ziro.Digital.
Track: Open Innovation / Student Builder Challenge
We are first-year CSE AI/ML students who went from zero cloud experience to deploying a multimodal Agentic AI pipeline in 4 days entirely on an iPad using cloud environments and gemini prompting.

 
￼ Shashwat Tripathi - First Developer
￼ 
⁠
