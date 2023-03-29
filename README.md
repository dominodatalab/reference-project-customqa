# reference-project-customqa

## Setup instructions

This project requires the following [compute environments](https://docs.dominodatalab.com/en/latest/user_guide/f51038/environments/) to be present:

### PromptEngineering
**Environment Base** 

`Domino Standard Environment Py3.9 R4.2`

**Dockerfile Instructions**

```
USER root

RUN sudo apt -y install tesseract-ocr
RUN sudo apt-get -y install libpoppler-dev
RUN sudo apt-get install poppler-utils
RUN sudo apt -y install libmagic-dev

RUN pip install pinecone-client
RUN pip install langchain
RUN pip install unstructured[local-inference]
RUN pip install poppler-utils
RUN pip install openai
RUN pip install faiss-cpu


RUN pip install "detectron2@git+https://github.com/facebookresearch/detectron2.git@v0.6#egg=detectron2"


USER ubuntu
```
