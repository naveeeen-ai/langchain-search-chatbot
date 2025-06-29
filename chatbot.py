from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.tools import  DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

def summary_with_search(question):
    search = DuckDuckGoSearchRun()
    
    tools = [search]
    
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )
    
    enhanced_question = f"""
    Please answer the following question. If you need current information,
    use web search to get the latest data.
    
    Question: {question}
    """
    
    try:
        result = agent.run(enhanced_question)
        return result
    except Exception as e:
        return f"Search error: {str(e)}"

def summary_basic(question):
    prompt = PromptTemplate(
        input_variables=["question"],
        template="Question : {question} \n Answer : ",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.invoke(question)
    return result["text"]

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

st.title("ChatBOT with Web Search")
st.write("Enter your question (web search will be used for current information):")
question = st.text_input("Question")

search_enabled = st.checkbox("Enable Web Search", value=True)

if st.button("Generate Answer"):
    if question:
        with st.spinner("Searching and generating answer..."):
            if search_enabled:
                answer = summary_with_search(question)
                st.write("**Answer with Web Search:**")
                st.write(answer)
            else:
                answer = summary_basic(question)
                st.write("**Basic Answer (No Web Search):**")
                st.write(answer)
    else:
        st.warning("Please enter a question!")


