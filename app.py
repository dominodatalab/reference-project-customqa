import os
import streamlit as st
from langchain.callbacks import get_openai_callback
from langchain_openai import ChatOpenAI
from streamlit_chat import message
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain import hub
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

# Uncomment if you want to store and use the OpenAI key stored in an environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")
embeddings = None

st.set_page_config(initial_sidebar_state="expanded", layout="wide")

search_df_note = ":point_left: Make sure you've entered your OpenAI API Key. You can ask the chat assistant questions on internal documents. As a starting point, you may ask 'What questions can you help me answer?'"
st.info(search_df_note, icon="ℹ️")

# Initialise session state variables
if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
if "total_tokens" not in st.session_state:
    st.session_state["total_tokens"] = []

with st.sidebar:
    if not openai_api_key:
        openai_api_key = st.text_input(
            "Enter your OpenAI API key to get started:", type="password"
        )
        if not (openai_api_key):
            st.warning("Please enter your OpenAI API key", icon="⚠️")
        else:
            st.success("Proceed to entering your prompt message!", icon="👉")
            embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    else:
        st.success("OpenAI API Key Found!", icon="✅")
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

    model_name = st.radio("Choose a model:", ("GPT-3.5", "GPT-4"))
    clear_button = st.button("Clear Conversation", key="clear")

if clear_button:
    st.session_state["generated"] = []
    st.session_state["past"] = []
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]


def get_chat_llm(model_name, openai_api_key):

    if model_name and openai_api_key:
        if model_name and model_name == "GPT-3.5":
            llm = ChatOpenAI(
                temperature=0, openai_api_key=openai_api_key, model_name="gpt-3.5-turbo"
            )
        elif model_name and model_name == "GPT-4":
            llm = ChatOpenAI(
                temperature=0, openai_api_key=openai_api_key, model_name="gpt-4"
            )

    return llm


def get_chain(retriever, model_name, openai_api_key):

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    llm = get_chat_llm(model_name, openai_api_key)
    combine_docs_chain = create_stuff_documents_chain(llm, retrieval_qa_chat_prompt)
    retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

    return retrieval_chain


if "store" not in locals() or store is None:
    store = FAISS.load_local(
        "faiss_store", embeddings, allow_dangerous_deserialization=True
    )

if store and openai_api_key:
    retrieval_chain = get_chain(store.as_retriever(), model_name, openai_api_key)

# container for chat history
response_container = st.container()
# container for text box
container = st.container()

with container:
    with st.form(key="my_form", clear_on_submit=True):
        user_input = st.text_area("You:", key="input", height=100)
        submit_button = st.form_submit_button(label="Send")
    if submit_button and user_input and retrieval_chain and openai_api_key:
        with st.spinner("Searching for the answer..."):
            with get_openai_callback() as cb:
                result = retrieval_chain.invoke({"input": user_input})
                answer = result["answer"]

        st.session_state["total_tokens"].append(cb.total_tokens)
        answer = result["answer"]
        st.session_state["past"].append(user_input)
        st.session_state["generated"].append(answer)

    if st.session_state["generated"]:
        with response_container:
            for i in range(len(st.session_state["generated"])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
                message(st.session_state["generated"][i], key=str(i))
                # if 'total_tokens' in st.session_state and len(st.session_state['total_tokens']) > 0:
                # st.write(f"Number of tokens: {st.session_state['total_tokens'][i]}")
