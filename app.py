import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="Ignoxio | Gemini AI Suite",
    page_icon="✦",
    layout="wide"
)

# Claude-inspired custom styling
st.markdown("""
    <style>
    .stApp { background-color: #faf9f5; color: #1a1a1a; }
    [data-testid="stSidebar"] { background-color: #f3f1ea; border-right: 1px solid #e6e2d3; }
    .stButton button { border-radius: 8px; font-weight: 500; border: 1px solid #dcd7cc; background-color: #ffffff; color: #333333; }
    .stButton button:hover { background-color: #f0ece1; border-color: #cc785c; color: #cc785c; }
    </style>
""", unsafe_allow_html=True)

# Sidebar Configuration for Gemini API Key
st.sidebar.title("✦ Ignoxio Control Center")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password", help="Get your free API key from Google AI Studio.")
model_choice = st.sidebar.selectbox("Select Gemini Model", ["gemini-1.5-flash", "gemini-1.5-pro"])
temperature = st.sidebar.slider("Creativity (Temperature)", 0.0, 1.0, 0.7, 0.05)

st.sidebar.markdown("---")
if api_key:
    genai.configure(api_key=api_key)
    st.sidebar.success("Gemini API Key Configured")
else:
    st.sidebar.warning("Please enter your Gemini API key to run tasks.")

# Main Navigation Tabs
tab1, tab2, tab3 = st.tabs([
    "🚀 Task 3: Content & Story Generator", 
    "📝 Task 2: AI Text Summarizer", 
    "🧠 Task 1: Prompt Engineering Showcase"
])

# Helper function to call Gemini safely
def call_gemini(prompt_text, temp):
    if not api_key:
        return "⚠️ Error: Please enter your Gemini API Key in the sidebar."
    try:
        model = genai.GenerativeModel(model_choice)
        response = model.generate_content(
            prompt_text,
            generation_config=genai.types.GenerationConfig(temperature=temp)
        )
        return response.text
    except Exception as e:
        return f"❌ API Error: {e}"

# ==========================================
# TAB 1: TASK 3 - AI STORY / CONTENT GENERATOR
# ==========================================
with tab1:
    st.header("Task 3: AI Story & Content Generator")
    st.markdown("Generate custom short stories, blog posts, or poems using the Gemini API based on keywords and selected tones.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        content_topic = st.text_input("Enter Topic or Keywords", placeholder="e.g., Artificial intelligence in sustainable architecture")
        content_type = st.selectbox("Content Format", ["Short Story", "Blog Post", "Poem"])
    with col_b:
        content_tone = st.selectbox("Tone & Genre", ["Professional & Authoritative", "Creative & Cinematic", "Inspirational", "Humorous", "Technical & Precise"])

    if "generated_content" not in st.session_state:
        st.session_state.generated_content = ""

    col_btn1, col_btn2 = st.columns([1, 1])
    with col_btn1:
        generate_clicked = st.button("✨ Generate Content", use_container_width=True)
    with col_btn2:
        regenerate_clicked = st.button("🔄 Regenerate Output", use_container_width=True)

    if generate_clicked or regenerate_clicked:
        if not content_topic:
            st.warning("Please enter a topic or keywords first.")
        elif not api_key:
            st.warning("Please provide your Gemini API key in the sidebar.")
        else:
            with st.spinner("Generating content via Gemini API..."):
                prompt = (
                    f"Write a {content_type.lower()} about '{content_topic}' "
                    f"using a {content_tone.lower()} tone. Make it engaging, structured, and high quality."
                )
                st.session_state.generated_content = call_gemini(prompt, temperature)

    if st.session_state.generated_content:
        st.markdown("### Result:")
        st.markdown(st.session_state.generated_content)


# ==========================================
# TAB 2: TASK 2 - AI TEXT SUMMARIZER
# ==========================================
with tab2:
    st.header("Task 2: AI Text Summarizer")
    st.markdown("Paste long-form text below to generate a concise summary using Gemini and analyze length reduction metrics.")

    long_text = st.text_area("Paste Long-Form Text Here", height=200, placeholder="Paste your article, report, or document text here...")
    
    if st.button("📊 Summarize Text", use_container_width=True):
        if not long_text.strip():
            st.warning("Please enter some text to summarize.")
        elif not api_key:
            st.warning("Please provide your Gemini API key in the sidebar.")
        else:
            with st.spinner("Summarizing text via Gemini API..."):
                prompt = f"Summarize the following text concisely while retaining key insights:\n\n{long_text}"
                summary = call_gemini(prompt, temp=0.3)
                
                # Metrics Calculation
                orig_words = len(long_text.split())
                summ_words = len(summary.split())
                reduction = round((1 - (summ_words / orig_words)) * 100, 1) if orig_words > 0 else 0
                
                st.markdown("### Summary Result:")
                st.info(summary)
                
                st.markdown("### 📈 Length Metrics Comparison")
                m1, m2, m3 = st.columns(3)
                m1.metric("Original Word Count", f"{orig_words} words")
                m2.metric("Summary Word Count", f"{summ_words} words")
                m3.metric("Reduction Efficiency", f"{reduction}%")


# ==========================================
# TAB 3: TASK 1 - PROMPT ENGINEERING SHOWCASE
# ==========================================
with tab3:
    st.header("Task 1: Prompt Engineering Showcase & Library")
    st.markdown("Explore structured prompt styles, comparison analyses, and a Python prompt template library.")

    st.subheader("1. Prompt Engineering Methodologies Documented")
    
    with st.expander("📌 Zero-Shot Prompting Example"):
        st.markdown("**Prompt:** `Classify the sentiment of this review as Positive or Negative: 'The user interface is sleek and lightning fast.'`")
        st.markdown("**Output Analysis:** The model directly provides the classification ('Positive') without prior examples.")

    with st.expander("📌 Few-Shot Prompting Example"):
        st.markdown("""**Prompt:** 
- Input: "Great battery life!" -> Sentiment: Positive
- Input: "App crashes on startup." -> Sentiment: Negative
- Input: "The new design is acceptable." -> Sentiment: """)
        st.markdown("**Output Analysis:** By providing examples, the model matches the formatting pattern precisely ('Neutral').")

    with st.expander("📌 Chain-of-Thought (CoT) Prompting Example"):
        st.markdown("**Prompt:** `A digital agency manages 3 ad campaigns. Campaign A generates 120 leads, Campaign B generates 50% more than A, and Campaign C generates half of B. Step-by-step, calculate total leads.`")
        st.markdown("**Output Analysis:** Forces intermediate reasoning steps before arriving at the final correct total (360 leads).")

    st.markdown("---")
    st.subheader("2. Python Prompt Template Library")
    st.markdown("Below is the production-ready Python dictionary library used for managing templates across tasks:")

    code_snippet = '''
# prompt_library.py
PROMPT_TEMPLATES = {
    "zero_shot_classification": "Classify the following text into [Category A, Category B]: {input_text}",
    "few_shot_extraction": "Extract entities using this format:\\nText: {ex1_text}\\nEntities: {ex1_ent}\\n\\nText: {target_text}\\nEntities:",
    "chain_of_thought_solver": "Solve this problem step-by-step:\\nProblem: {problem_statement}\\nReasoning Steps:",
    "content_generator": "Write a {format} about {topic} in a {tone} tone."
}
    '''
    st.code(code_snippet, language="python")