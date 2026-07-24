# Technova Generative AI Task (Ignoxio Control Center)

A polished, multi-tab Generative AI web suite built with **Python** and **Streamlit**, powered directly by the **Google Gemini API**. This project fulfills all requirements for the generative AI task, integrating advanced prompt engineering methodologies, text summarization analytics, and dynamic content generation[cite: 1].

---

## 🚀 Core Features & Tasks

### 1. Task 3: AI Story & Content Generator
* **Dynamic Generation:** Create custom short stories, blog posts, or poems based on specific keywords and topics[cite: 1].
* **Tone Selection:** Choose from professional, creative, inspirational, humorous, or technical tones[cite: 1].
* **Iterative Refinement:** Includes instant regeneration options to tailor output quality.

### 2. Task 2: AI Text Summarizer
* **Executive Summaries:** Paste long-form articles, reports, or documentation to extract key insights[cite: 1].
* **Reduction Analytics:** Automatically calculates and displays performance metrics, including original word count, summary word count, and overall length reduction efficiency percentage[cite: 1].

### 3. Task 1: Prompt Engineering Showcase & Library
* **Methodology Breakdown:** Interactive documentation explaining **Zero-Shot**, **Few-Shot**, and **Chain-of-Thought (CoT)** prompting techniques[cite: 1].
* **Python Template Library:** Features a production-ready dictionary of reusable prompt templates for scalable AI development[cite: 1].

---

## 🛠️ Tech Stack
* **Frontend/UI:** Streamlit (with custom Claude-inspired styling)[cite: 1]
* **AI Model:** Google Gemini (`gemini-3.6-flash` / `gemini-3.5-flash-lite`)[cite: 1]
* **Integration:** Direct Python REST API calls (`requests`) for seamless execution without heavy SDK dependency mismatches[cite: 1].

---

## ⚙️ How to Run Locally

1. **Clone or Download** this repository to your local machine.
2. **Install Dependencies** via your terminal:
   ```bash
   pip install streamlit requests

   streamlit run app.py

   Get a free API key from Google AI Studio.

   Enter your API key securely into the interactive sidebar input field inside the Streamlit app to start running tasks[cite: 1].
