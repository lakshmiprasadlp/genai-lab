from langchain_community.document_loaders.text import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_text():
    file_path = "lp.txt"
    loader = TextLoader(file_path)
    documents = loader.load()
    data = ""
    for doc in documents:
        data += doc.page_content
    return data

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10, chunk_overlap=5)
    chunks = text_splitter.split_text(text)
    return chunks

# Retrieve the Google API key from environment variables
api_key = os.getenv("GOOGLE_API_KEY")
#print(f"Google API Key: {api_key}")

def get_vector_store(text_chunks):
    # Initialize embeddings using Google Generative AI's embedding model
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    # Create FAISS vector store from text chunks and embeddings
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    
    # Save the FAISS index locally for future use
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template = """
    A client has a specific disease and asks for the doctor's details based on the specialist they need.
    Provide the doctor's name, registration number, cabin number, and available time.
    """

    # Initialize the Google Generative AI model
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

    # Create a prompt template
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    # Use RunnableSequence to chain the prompt and model together
    chain = prompt | model

    return chain

# Main execution flow
if __name__ == "__main__":
    # Load and process the text data
    text_data = get_text()
    
    # Split text into manageable chunks
    text_chunks = get_text_chunks(text_data)
    
    # Generate and save FAISS vector store from text chunks
    get_vector_store(text_chunks)
    
    # Initialize the conversational chain
    conversational_chain = get_conversational_chain()
    
    # Example usage of the chain with context and a question
    context = "The patient needs to know about cardiology specialists."
    question = "Can you provide details of the available cardiologists?"

    # Run the conversational chain and get the response
    result = conversational_chain.invoke({"context": context, "question": question})
    
    # Print the generated response
    print(result['content'])  
