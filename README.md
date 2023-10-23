## License
This template is licensed to Customer subject to the terms of the license agreement between Domino and the Customer on file.

# OpenAI custom Q&A Reference Project

This reference project shows how to use OpenAI's LLM to do Q&A over information that OpenAI's models have not been trained on and will not be able to provide answers out of the box. The way this works is to create embeddings of the document(s) that you want to query, run a semantic search to return information that can be provided as context/information along with the user's query as a prompt to the LLM and get results back. The project has the following files 

* OpenAI_QA_Pinecone.ipynb : This file loads a PDF,converts it to embeddings, stores the embeddings in Pinecone, runs the semantic search against the embeddings, constructs a prompt and calls OpenAI's models to get a response. You will need your OpenAPI and Pinecone keys to be set in the environment for this example. To work with OpenAI, set up your Pinecone index to have 1536 dimensions.

* OpenAI_QA_FAISS.ipynb : This file loads a PDF, converts it to embeddings, stores the embeddings locally using a FAISS index, runs the semantic search against the embeddings, constructs a prompt and calls OpenAI's models to get a response. You will need your OpenAPI key to be set in the environment for this example.

* faiss_ddl_doc_store.pkl : This file contains the FAISS embeddings of Domino's documentation . You can use this if you don't want to (re)compute embeddings of Select_Global_Value_Fund.pdf again

* app.sh : The shell script needed to run the chat app

* app.py : Streamlit app code for the Q&A chatbot. This app uses ```faiss_ddl_doc_store.pkl``` for the embeddings

* Select_Global_Value_Fund.pdf : A report that can be used as an example for the flow that has been described above in case you want to compute embeddings on a fresh document

* Solution_Overview.pdf : A diagram that depicts the different components and the flow of information between them


## Setup instructions

This project requires the following [compute environments](https://docs.dominodatalab.com/en/latest/user_guide/f51038/environments/) to be present. Please ensure the "Automatically make compatible with Domino" checkbox is selected while creating the environment.

Please don't forget to set your OpenAI key as an environment variable before spinning up your workspace.


**Environment Base** 

`quay.io/domino/pre-release-environments:project-hub-gpu.main.latest`

**Pluggable Workspace Tools** 
```
jupyterlab:
  title: "JupyterLab"
  iconUrl: "/assets/images/workspace-logos/jupyterlab.svg"
  start: [ "/opt/domino/workspaces/jupyterlab/start" ]
  httpProxy:
    internalPath: "/{{ownerUsername}}/{{projectName}}/{{sessionPathComponent}}/{{runId}}/{{#if pathToOpen}}tree/{{pathToOpen}}{{/if}}"
    port: 8888
    rewrite: false
    requireSubdomain: false
vscode:
 title: "vscode"
 iconUrl: "/assets/images/workspace-logos/vscode.svg"
 start: [ "/opt/domino/workspaces/vscode/start" ]
 httpProxy:
    port: 8888
    requireSubdomain: false
```

Please change the value in `start` according to your Domino version.
