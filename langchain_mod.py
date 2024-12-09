import os
import logging
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS


from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.llms import OpenAI
from langchain_openai import OpenAIEmbeddings


# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


# Load environment variables from .env
load_dotenv()

# Fetch API key securely
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    logging.error("OPENAI_API_KEY is not defined in the environment or .env file.")
    raise ValueError("OPENAI_API_KEY is required to proceed.")


def load_data(file_path):
    """
    Loads the Tirmidhi data from a CSV file.
    Args:
        file_path (str): Path to the data file.
    Returns:
        str: Contents of the CSV as a string.
    """
    if not os.path.exists(file_path):
        logging.error(f"Data file '{file_path}' does not exist.")
        raise FileNotFoundError(f"Data file '{file_path}' not found.")

    with open(file_path, 'r', encoding='utf-8') as file:
        logging.info("Loading data from the file...")
        return file.read()


def create_vectorstore(data):
    """
    Creates a FAISS vector store from text data.
    Args:
        data (str): Text data to index into FAISS vectorstore.
    Returns:
        FAISS vectorstore object.
    """
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_text(data)

    # Log embedding operation
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    logging.info("Creating FAISS vectorstore...")
    return FAISS.from_texts(texts, embeddings)


def answer_question(vectorstore, question):
    """
    Answers a question using the vectorstore.
    Args:
        vectorstore: FAISS vectorstore to query.
        question (str): Question to ask the vectorstore.
    Returns:
        str: The answer from the model.
    """
    retriever = vectorstore.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(model="text-davinci-003", openai_api_key=OPENAI_API_KEY),
        retriever=retriever
    )

    logging.info(f"Running query: '{question}'")
    return qa_chain.run(question)


if __name__ == "__main__":
    # Path to data file
    data_file = 'Tirmidhi.csv'

    try:
        # Load data
        data = load_data(data_file)

        # Create vectorstore
        vectorstore = create_vectorstore(data)

        # Ask a sample question
        question = "What did Tirmidhi say about prayer?"
        answer = answer_question(vectorstore, question)

        # Output the answer
        logging.info("Answer fetched successfully.")
        print("Answer:", answer)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
