import streamlit as st                                                                  
import os
import json
from groq import Groq
import csv
import re
from datetime import datetime, timedelta
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
from rag import load_knowledge_base, generate_ad_content_with_rag                   #functions being imported from other files
from markdowns import generate_ad, convert_to_csv                                   #stored them seperately to increase documentability and readability
from dotenv import load_dotenv

load_dotenv()                                                                       #loaded environment variables   
api = os.getenv("GROQ_API_KEY")                                                     #groq api key stored
groq_client = Groq(api_key=api)                                                     #groq client initialised

def render_ad_preview(ad_content, platform, company_name):        #function uses inputs to create ad campaign data and convert them to html docs that can be displayed on streamlit screen, as well as downloaded and stored
    html_content = generate_ad(ad_content, platform, company_name)              #calls generate_ad function that calls the llm to generate campaign data                  
    body_start = html_content.find('<body>') + 6                                
    body_end = html_content.find('</body>')
    body_content = html_content[body_start:body_end].strip()                    #strips the whole markup script to extract part that goes into streamlit
    st.markdown(body_content, unsafe_allow_html =True)                          #campaign data being displayed

st.set_page_config(page_title="AI Ad Campaign Generator", page_icon="📈", layout="wide")                    #Homepage intialised using streamlit
with st.sidebar:                                                                                             #Sidebar that handles settings
    st.title("Settings")       
    platforms = st.multiselect(                                                                              #dropdown list to select platform
        "Select Platforms",
        ["Facebook", "Instagram", "LinkedIn", "TikTok"],
        default = ["Facebook"]
    )
       
    st.markdown("---")
    st.markdown("### Example Briefs")                                                                       #some default campaigns i used for testing
    if st.button("Eco-Friendly Water Bottle"):
        st.session_state.company_name = "Ocean Beverages"
        st.session_state.product_name = "EcoVibe Water Bottle"
        st.session_state.product_description = "Sustainable, leak-proof water bottle made from recycled materials"
        st.session_state.target_audience = "Eco-conscious millennials and Gen Z, fitness enthusiasts"
        st.session_state.key_value_proposition = "Sustainable, Durable, Stylish, Affordable"
        
    if st.button("Premium Coffee Subscription"):
        st.session_state.company_name = "Nescafe"
        st.session_state.product_name = "Morning Brew Club"
        st.session_state.product_description = "Monthly subscription of artisan coffee beans from around the world"
        st.session_state.target_audience = "Coffee lovers, professionals, ages 25-45"
        st.session_state.key_value_proposition = "Convenience, Quality, Discovery, Freshness"

    if st.button("Puma Max Shoes"):
        st.session_state.company_name = "Puma Shoes"
        st.session_state.product_name = "Puma Max"
        st.session_state.product_description = "A lightweight, high-performance shoe with a stylish blend of sleek design and superior comfort, perfect for both everyday wear and active use."
        st.session_state.target_audience = "Sports and Athletics Enthusiasts"
        st.session_state.key_value_proposition = "Comfort, Durability, Performance, Attractive Design"

st.title("AI-Powered Ad Campaign Generator")                                                                #main screen
    
with st.expander("📝 Campaign Brief", expanded=True):                                                       #input area
    col1, col2 = st.columns(2)                                                                              #inputs in two columns
       
    with col1:
        company_name = st.text_input(
            "Company/Enterprise Name",
            value = st.session_state.get("company_name",""),
            key = "company_name"
        )
        product_name = st.text_input(
            "Product/Service Name",
            value=st.session_state.get("product_name", ""),
            key="product_name"
        )
        product_description = st.text_area(
            "Product/Service Description",
            value=st.session_state.get("product_description", ""),
            key="product_description"
        )
       
    with col2:
        target_audience = st.text_input(
            "Target Audience",
            value=st.session_state.get("target_audience", ""),
            key="target_audience"
        )
        key_value_proposition = st.text_input(                                                             #features and qualities of the product
            "Key Value Proposition (comma separated)",
            value=st.session_state.get("key_value_proposition", ""),
            key="key_value_proposition"
        )
    
if st.button("Generate Ad Campaigns", type="primary"):
    if not product_name or not product_description:
        st.error("Please fill in at least Product Name and Description")
        st.stop()
            
    brief = f"""
    Create an ad campaign for:
    Product/Service: {product_name}
    Description: {product_description}
    Target Audience: {target_audience}
    Value Proposition: {key_value_proposition}
    """                                                                                                 #campaign input data created as brief
       
    with st.spinner("Generating campaigns..."):
        campaigns = {}
        for platform in platforms:
            campaign = generate_ad_content_with_rag(brief, platform)                                    #function call to generate campaigns
            if campaign:
                campaigns[platform] = campaign                                              #campaigns for different platforms being generated and stored one by one

        if campaigns:
            st.session_state.campaigns = campaigns
            st.success(f"Successfully generated {len(campaigns)} campaign(s)!")
        else:
            st.error("Failed to generate any campaigns. Please try again.")
            if "campaigns" in st.session_state:
                del st.session_state.campaigns
   

if "campaigns" in st.session_state and st.session_state.campaigns:                      #campaigns being displayed
    st.markdown("---")
    st.header("Generated Campaigns")
    tabs = st.tabs([f"📱 {platform}" for platform in st.session_state.campaigns.keys()])
        
    for tab, (platform, campaign) in zip(tabs, st.session_state.campaigns.items()):
        with tab:
            col1, col2 = st.columns([1, 2])
             
            with col1:
                st.expander("Campaign Details",expanded = False)
                st.json(campaign)
                
                st.download_button(                                                        #button to download generated campaign data as JSON
                    label="Download JSON",  
                    data=json.dumps(campaign, indent=2),
                    file_name=f"{platform}_campaign.json",
                    mime="application/json"
                )
                   
                csv_data = convert_to_csv(campaign, platform)                               #as csv
                st.download_button(
                    label="Download CSV",
                    data=csv_data,
                    file_name=f"{platform}_campaign.csv",
                    mime="text/csv"
                )

                html_data = generate_ad(campaign, platform, company_name)                   #button to download an html file that emulates the platform ad structure
                st.download_button(
                    label="Download HTML",
                    data = html_data,
                    file_name = f"{platform}_ad_preview.html",
                    mime="text/html"
                )            
                
            with col2:
                st.subheader("Ad Preview")
                render_ad_preview(campaign, platform, company_name)
                st.subheader("Performance Predictions")
                if "performance_predictions" in campaign:
                    metrics = campaign["performance_predictions"]
                    if isinstance(metrics, dict):
                        cols = st.columns(3)
                        cols[0].metric("CTR", f"{metrics.get('click_through_rate', 'N/A')}%")                           #metrics being displayed
                        cols[1].metric("Engagement", f"{metrics.get('engagement_rate', 'N/A')}%")
                        cols[2].metric("Conversion", f"{metrics.get('conversion_rate', 'N/A')}%")
                    else:
                        st.warning("Unexpected performance predictions format")
                else:
                    st.warning("No performance predictions available")
else:
    st.info("No campaigns generated yet. Fill out the form and click 'Generate'.")
