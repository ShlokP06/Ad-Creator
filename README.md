
# atomicads-ai-engineer-assignment

AI-Powered Campaign Creator for a Social Platform using LLM and RAG techniques.

As Ad platform APIs such as LinkedIn Ads API and Meta Ads API require bussiness accounts and approval, hence I adapted to not using them, rather generated HTML templates simulating the original platforms.

The project follows the following algorithm:
- Input Data is taken from the Streamlit UI.
- The data is passed through the script, and RAG framework is implemented on it, and thus an LLM generates a creative ad campaign following the instructions passed to it via the prompt.
- The created JSON file is then processed, to extract information.
- It is then sent to the UI through the html markdown text, and made available on the interface.
- Buttons are available, to download the required JSON, CSV and HTML files.
- Some "Model" campaigns are also provided in the interface. These are the trial data I tested my project on...


Hope you guys like it!!!
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
   venv\Scripts\activate 
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

5. **Start the Application**:
   - Run the following in the command prompt window inside the virtual environment
   ```bash
   python -m streamlit run ads.py
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

   Separation of Contents: The code is split across three primary files (ads.py, rag.py, markdowns.py) to increase readability, maintainability, and testability.

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
## Why this LLM: llama-4-scout
1. Instruction-Tuned:

- The llama-4-scout variant is fine-tuned for instruction following, making it highly compatible with structured prompts like ad briefs.

- Provides coherent and format-specific outputs, which is essential when extracting strict JSON payloads for campaign APIs.

2. Balance of Performance & Cost:

- Larger than lightweight models (e.g., Mistral-7B), yet smaller than massive models like GPT-4.

- Offers a middle ground: high accuracy and creativity at reasonable inference latency and cost.

3. Compatibility with RAG:

- Integrates well with LangChain's ChatGroq wrapper and retrieval pipelines.

- Able to contextualize from custom vector sources and produce targeted ad content.

4. Flexibility Across Platforms:

- The same LLM handles tone/style shifts required for different platforms:

- E.g., professional tone for LinkedIn vs trendy tone for TikTok.



## 📉 Limitations & Costs

- **Token usage can be expensive** with repeated LLM calls.
- **Campaign creation is currently mocked**; integration with real APIs requires credentials and account approvals.
- **Model latency** may affect user experience for large prompts.

---

## 📸 Visuals

### Video Preview
![Video](https://github.com/ShlokP06/atomicads-ai-engineer-Shlok/blob/main/Visuals/Screenshot%202025-05-10%20201750.png)
[Watch the video](https://drive.google.com/file/d/10cn2nQyhd2Dz67653bJeyDDLVALyIyeZ/view?usp=drive_link)

---
## Future Updates
- **API Integration** with platforms such as Meta Ads API, LinkedIn Ads API.
- **Visual Quality** Allowing users to add images and videos to the add campaigns.
---

## 📁 Deliverables Checklist

- [x] Python scripts
- [x] `.env` or `config.json`
- [x] README with setup, logic, limitations
- [x] Video

---

## 👤 Author

> Your Name  
> [LinkedIn](https://www.linkedin.com/in/shlok-parikh-370773335/) | [GitHub](https://github.com/ShlokP06)
