
# atomicads-ai-engineer-assignment

AI-Powered Campaign Creator for a Social Platform using LLM and RAG techniques.

---

## 🚀 Project Overview

This tool automates the creation of social media advertisement campaigns (Meta, TikTok, LinkedIn, etc.) using:
- Prompt Engineering with LLMs
- Retrieval-Augmented Generation (RAG)
- API calls to social platforms (simulated/prototyped)

---

## 🧩 File Structure

| File Name      | Description                                                         |
|----------------|---------------------------------------------------------------------|
| `ads.py`       | Core logic for ad campaign creation using simulated API calls       |
| `markdowns.py` | Markdown formatter for campaign reports and outputs                 |
| `rag.py`       | RAG engine setup for campaign knowledge enhancement using documents |

---

## ⚙️ Setup Instructions

1. **Clone the repo**:
   ```bash
   git clone https://github.com/ShlokP06/atomicads-ai-engineer-Shlok.git
   cd atomicads-ai-engineer-Shlok
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # or venv\Scripts\activate on Windows
   ```

3. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your API credentials**:
   - Create a `.env` file or `config.json` and add credentials like:
     ```env
     GROQ_API_KEY=your_groq_api_key
     ```
---

## 🧠 How It Works

1. **User provides a campaign brief** (e.g., product, audience, goals)
2. **LLM generates ad content** using carefully engineered prompts
3. **RAG module** augments LLM with background knowledge (e.g., user docs, guidelines)
4. **Campaign is generated** using API or mocked API endpoints (prototype)
5. **Campaign Displayed** is shown on the Streamlit UI in the form of HTML
---

## 🧪 Technologies Used

- Python 3.10+
- Groq Inference Cient
- LangChain / Custom Prompt Engine
- dotenv / json for configuration

---

## 📌 Architectural Decisions

- **LLM vs Fine-Tuned Model**: We opted for prompt engineering with an existing API model for speed and flexibility.
- **RAG Usage**: Enhances the model’s understanding without retraining.
- **API Layer**: Abstracted in `ads.py` for easy switch between real and mock APIs.
1.**Modular Design**:
   Separation of Concerns: The code is split across three primary files (ads.py, rag.py, markdowns.py) to increase readability, maintainability, and testability.

   - ads.py: Manages user input, streamlit UI, campaign orchestration.
 
   - rag.py: Handles context-based content generation using Retrieval-Augmented Generation (RAG).

   - markdowns.py: Responsible for formatting output into HTML, CSV, and JSON formats.

2.**Use of RAG (Retrieval-Augmented Generation)**:

   - We opted for RAG over fine-tuning to:

   - Keep model inference cost low.

   - Avoid needing GPU access or custom model training.

   - Dynamically inject up-to-date and domain-specific context from ad-related resources via vector stores.

3.**Local Vector Database (FAISS)**:

   - FAISS is used for its performance and offline capability.

   - Allows flexible, scalable retrieval from web-scraped knowledge sources.

   - Can be extended to add user-specific corpora in the future.

4.**Streamlit UI**:

   - Chosen for rapid prototyping and seamless input/output display.

   - Allows interactive brief entry, ad preview rendering, and multi-format downloads without backend setup.

---

## 📉 Limitations & Costs

- **Token usage can be expensive** with repeated LLM calls.
- **Campaign creation is currently mocked**; integration with real APIs requires credentials and account approvals.
- **Model latency** may affect user experience for large prompts.

---

## 📸 Screenshots

*Add screenshots of campaigns from the Ad Platform UI here if available.*

---

## 📁 Deliverables Checklist

- [x] Python scripts
- [x] `.env` or `config.json`
- [x] README with setup, logic, limitations
- [ ] Campaign screenshots (optional)
- [ ] Loom or video walkthrough (optional)

---

## 👤 Author

> Your Name  
> [LinkedIn](https://linkedin.com/in/your-profile) | [GitHub](https://github.com/ShlokP06)
