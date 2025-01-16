import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Configure the Llama 3.2 model
llm = ChatOllama(model="llama3.2:3b", temperature=0.7, base_url="http://localhost:11434")

# Initialize the web search tool
search_tool = DuckDuckGoSearchAPIWrapper(max_results=5)

# Define the prompt template
prompt_template = PromptTemplate(
    template="""
    You are an AI assistant that provides accurate and concise answers based on web search results.
    Question: {question}
    Web Search Context: {context}
    Answer:
    """,
    input_variables=["question", "context"],
)

# Define the response generation chain
response_chain = prompt_template | llm | StrOutputParser()

# Streamlit UI
st.title("Internet Search Assistant with Llama 3.2")
user_query = st.text_input("Enter your question:")

if st.button("Search and Answer"):
    if user_query:
        # Perform web search
        search_results = search_tool.run(user_query)
        # Generate response
        response = response_chain.invoke({"question": user_query, "context": search_results})
        st.write(response)
    else:
        st.warning("Please enter a question.")
