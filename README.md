## License
This template is licensed under Apache 2.0 and contains the following components: 
* Langchain [MIT](https://github.com/langchain-ai/langchain/blob/master/LICENSE)
* Pinecone [EULA](https://www.pinecone.io/thin-client-user-agreement/)
* [OpenAI](https://openai.com/policies/terms-of-use)
* [FAISS](https://github.com/facebookresearch/faiss/blob/main/LICENSE)

# OpenAI custom Q&A Reference Project

This reference project shows how to use OpenAI's LLM to do Q&A over information that OpenAI's models have not been trained on and will not be able to provide answers out of the box. The way this works is to create embeddings of the document(s) that you want to query, run a semantic search to return information that can be provided as context/information along with the user's query as a prompt to the LLM and get results back. The project has the following files 

* OpenAI_QA_Pinecone.ipynb : This file loads a PDF,converts it to embeddings, stores the embeddings in Pinecone, runs the semantic search against the embeddings, constructs a prompt and calls OpenAI's models to get a response. You will need your OpenAPI and Pinecone keys to be set in the environment for this example. To work with OpenAI, set up your Pinecone index to have 1536 dimensions.

* OpenAI_QA_FAISS.ipynb : This file loads a PDF, converts it to embeddings, stores the embeddings locally using a FAISS index, runs the semantic search against the embeddings, constructs a prompt and calls OpenAI's models to get a response. You will need your OpenAPI key to be set in the environment for this example.

* app.sh : The shell script needed to run the chat app

* app.py : Streamlit app code for the Q&A chatbot. This app uses ```index.pkl``` in the ```faiss_store``` folder for the embeddings

* Select_Global_Value_Fund.pdf : A report that can be used as an example for the flow that has been described above in case you want to compute embeddings on a fresh document

* Solution_Overview.pdf : A diagram that depicts the different components and the flow of information between them


## Setup instructions

This project requires the following [compute environments](https://docs.dominodatalab.com/en/latest/user_guide/f51038/environments/) to be present. Please ensure the "Automatically make compatible with Domino" checkbox is selected while creating the environment.

Please don't forget to set your ```OPENAI_API_KEY``` key as an environment variable before spinning up your workspace. If you're using Pinecone, you'll need to set the ```PINECONE_API_KEY``` key as well.


### Environment Requirements

The necessary packages and versions can be found in the requirements.txt file. Ensure these packages are installed in a custom Domino Environment. Please find the docker instructions below:

Step 1
Use the ecosystem compute environment `Ecosystem-Template-Domino-Standard-Environment-with-Python-3.9` that's automatically built for you when you clone the AI Hub template

Step 2
Under dockerfile instructions use the instructions provided below to install the python packages into a new environment:

```
 RUN pip install \
    langchain==0.2.0 \
    langchain_community==0.2.0 \
    langchain_openai==0.1.7 \
    langchain_text_splitters==0.2.0 \
    --user
 
```

### Hardware Requirements
Utilize small hardware tier
