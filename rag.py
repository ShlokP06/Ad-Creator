import os
import json
from groq import Groq
import re
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv

load_dotenv()                                                                         #loading environment variables
api = os.getenv("GROQ_API_KEY")                                                       #api key stored
def generate_ad_content_with_rag(brief, platform):                                    #function that uses RAG to generate ad campaign
  retriever = load_knowledge_base().as_retriever()

  platform_prompts = {
      "facebook" : "Create a Facebook ad campaign with engaging visual copy and clear CTA.",
      "instagram" : "Create an Instagram ad with visual-first approach and trendy, concise copy.",
      "linkedin" : "Create a professional LinkedIn ad with B2B focus and industry credibility.",
      "tiktok" : "Create a TikTok ad that's entertaining, trendy and drives engagement."
  }
  context_docs = retriever.get_relevant_documents(brief)                              #RAG data retrieved from vectorspace
  context = "\n\n".join([doc.page_content for doc in context_docs]) 
  prompt = ChatPromptTemplate.from_template(template="""                                                                                        
                                            You are an expert and very creative digital advertising specialist:
                                            {platform_prompt}
  
                                            Use the following context about effective advertising:
                                            {context}
                                            Create a {platform} ad campaign based on this brief: {input}
                                            Respond ONLY with valid JSON containing these fields:
                                            {{
                                            "campaign_name": string,
                                            "objective": string,
                                            "target_audience": string,
                                            "ad_copy": string,
                                            "headline": string,
                                            "description": string,
                                            "cta": string,
                                            "audience_interests": list,
                                            "audience_age_min": integer,
                                            "audience_age_max": integer,
                                            "suggested_budget_daily": number,
                                            "campaign_duration_days": integer,
                                            "performance_predictions":{{
                                            "click_through_rate": number,
                                            "engagement_rate": number,
                                            "conversion_rate": number
                                             }}
                                            }}
                                            Include the following sections in your response as a JSON object:
                                            - campaign_name: A catchy name for the campaign
                                            - objective: The primary objective (awareness, sales and marketing, consideration, conversion)
                                            - target_audience: A detailed description of the target audience
                                            - ad_copy: The main text for the ad, very attractive and attention capturing, (tone appropriate for {platform})
                                            - headline: A concise, attention-grabbing slogan or catchphrase
                                            - description: A brief description elaborating on the headline
                                            - cta: Call to action (Learn More, Shop Now, Sign Up, etc.)
                                            - audience_interests: List of 5-7 relevant audience interests/keywords
                                            - audience_age_min: Minimum age for targeting (e.g., 18, 25, 35)
                                            - audience_age_max: Maximum age for targeting (e.g., 35, 45, 65)
                                            - suggested_budget_daily: Suggested daily budget in USD
                                            - campaign_duration_days: Suggested campaign duration in days
                                            - performance_predictions: Predicted metrics (click-through rate, engagement rate, conversion rate)
                                            """)                                                                      #prompt template to generate the ad campaign
  llm = ChatGroq(api_key=api,
    model="meta-llama/llama-4-scout-17b-16e-instruct"                                                                 #client initialisation with LLM of our choice
  )
  document_chain = create_stuff_documents_chain(llm, prompt)
  retrieval_chain = create_retrieval_chain(retriever, document_chain)

  response = retrieval_chain.invoke({                                                                                  #llm called
      "platform_prompt" : platform_prompts.get(platform.lower(), "Vreate a compelling ad campaign."),
      "platform" : platform,
      "input" : brief})
  content = re.search(r'\{.*\}', response['answer'], re.DOTALL)                                                        #recieved data getting extracted properly
  try:
    json_content = json.loads(content.group(0))
    return json_content
  except json.JSONDecodeError:
    st.warning("Not valid json. trying to extract.")
    if isinstance(content, str):
                json_match = re.search(r'\{.*\}', content, re.DOTALL)
                if json_match:
                    return json.loads(json_match.group(0))

def load_knowledge_base():                                                                                               #function creating RAG VectorSpace
   embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
   if os.path.exists('knowledge_base'):
    return FAISS.load_local('knowledge_base', embeddings, allow_dangerous_deserialization = True)
   
   urls=[                                                                                                         #list of helpful advertisement URLs, for RAG reference
    "https://www.facebook.com/business/learn",
    "https://business.instagram.com/advertising",
    "https://business.linkedin.com/marketing-solutions/ads",
    "https://ads.tiktok.com/business/creativecenter",
    "https://blog.hubspot.com/marketing/how-to-write-an-ad",
    "https://www.wordstream.com/blog/ws/2023/05/10/how-to-write-a-marketing-brief",
    "https://www.socialmediaexaminer.com/social-media-advertising-guide/",
    "https://www.oberlo.com/blog/facebook-ad-examples",
    "https://blog.hootsuite.com/instagram-ads/",
    "https://blog.hootsuite.com/linkedin-ads/",
    "https://www.wordstream.com/blog/ws/2021/09/15/tiktok-ads",
    "https://sproutsocial.com/insights/social-media-ad-targeting/",
    "https://www.insiderintelligence.com/insights/social-media-advertising-benchmarks/",
    "https://copyblogger.com/social-media-ad-copy/",
    "https://neilpatel.com/blog/write-persuasive-ad-copy/"
    ]

   try:
    docs=[]
    for url in urls:
        loader = WebBaseLoader(url)                                                                                 #data being loaded from websites to work on
        docs.extend(loader.load())
    if not docs:
       docs = [Document(
                page_content="Advertising Best Practices:\n"
                           "- Use clear, benefit-driven headlines\n"
                           "- Include strong call-to-action\n"
                           "- Target specific audience segments\n"
                           "- Test different ad variations\n"
                           "- Align visuals with messaging",
                metadata={"source": "default"}
            )]
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap = 200)
    splits = text_splitter.split_documents(docs)
    if splits:
        vectorstore = FAISS.from_documents(splits, embeddings)
        vectorstore.save_local('knowledge_base')                                                                    #data saved in vector databased FAISS
        return vectorstore                                                                                           #vector database object returned
    else:
        return None
   except Exception as e:
      st.warningf("RAG Failed")
      return None
