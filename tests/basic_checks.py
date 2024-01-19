import unittest
import os
import importlib.util

class TestOpenAIQA(unittest.TestCase):

    def test_library_langchain_installed(self):
        """ Test if langchain library is installed """
        langchain_installed = importlib.util.find_spec("langchain") is not None
        self.assertTrue(langchain_installed, "langchain library is not installed")
        
    # def test_library_detectron2_installed(self):
    #     """ Test if detectron2 library is installed """
    #     detectron2_installed = importlib.util.find_spec("detectron2") is not None
    #     self.assertTrue(detectron2_installed, "detectron2 library is not installed")
        
    def test_library_faiss_installed(self):
        """ Test if faiss library is installed """
        faiss_installed = importlib.util.find_spec("faiss") is not None
        self.assertTrue(faiss_installed, "faiss library is not installed")
        
    def test_library_pinecone_installed(self):
        """ Test if pinecone library is installed """
        pinecone_installed = importlib.util.find_spec("pinecone") is not None
        self.assertTrue(pinecone_installed, "pinecone library is not installed")
        
    def test_library_pypdf_installed(self):
        """ Test if pypdf library is installed """
        pypdf_installed = importlib.util.find_spec("pypdf") is not None
        self.assertTrue(pypdf_installed, "pypdf library is not installed")
        
    def test_library_streamlit_installed(self):
        """ Test if streamlit library is installed """
        streamlit_installed = importlib.util.find_spec("streamlit") is not None
        self.assertTrue(streamlit_installed, "streamlit library is not installed")
        
    def test_library_streamlit_chat_installed(self):
        """ Test if streamlit_chat library is installed """
        streamlit_chat_installed = importlib.util.find_spec("streamlit_chat") is not None
        self.assertTrue(streamlit_chat_installed, "streamlit_chat library is not installed")

    def test_pdf_file_exists(self):
        """ Test if the Northwind Healthcare PDF exists """
        pdf_file_path = '/mnt/code/data/Northwind_Health_Plus_Benefits_Details.pdf'
        self.assertTrue(os.path.isfile(pdf_file_path), "Northwind_Health_Plus_Benefits_Details.pdf does not exist")

if __name__ == '__main__':
    unittest.main()
