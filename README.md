# Hadith Search System with LangChain, FAISS, and OpenAI

This project leverages LangChain, FAISS, and OpenAI's embeddings API to create a semantic search system for processing and querying Hadith data. It allows loading and indexing data into a FAISS vector store, embedding with OpenAI embeddings, and querying for semantic similarity.

---

## 🚀 **Features**

- **Load Hadith Data**: Parse data from `Tirmidhi.csv`.
- **FAISS Vector Store**: Index processed embeddings using FAISS for efficient search.
- **Semantic Search with OpenAI Embeddings**: Embed text using OpenAI’s `text-embedding-ada-002`.
- **Handle Rate Limits**: handling OpenAI rate-limiting errors (`429 Too Many Requests`).

---

## 📚 **Tech Stack**

1. **Python 3.8+**
2. **LangChain** - Framework for chaining together embeddings, agents, and LLMs.
3. **OpenAI API** - For generating embeddings.
4. **FAISS** - A vector store for semantic search.
5. **langchain_community** - For compatibility with OpenAI embeddings and LangChain features.
6. **tiktoken** - Tokenizer for embeddings processing.
7. **Pandas** - To handle and preprocess data.
8. **LangChain and API Rate Handling** - Designed with error handling and retries.

---

## 🛠️ **Getting Started**

### **1. Clone the Repository**

First, clone the repository to your local machine:

```bash
git clone https://github.com/AhmedNewiry/Hadith-Search-System.git
cd hadith
```


---

### **2. Set Up the Virtual Environment**

Create and activate a virtual environment for dependency management:

```bash
python -m venv .hadithVenv
```

Activate the virtual environment:

```bash
source .hadithVenv/bin/activate   # On Linux/Mac
.\hadithVenv\Scripts\activate   # On Windows
```

---

### **3. Install Required Dependencies**

Ensure you have `pip` updated and install the necessary dependencies:

```bash
pip install -U pip
pip install -r requirements.txt
```

#### If the `requirements.txt` is missing:

Install dependencies manually:

```bash
pip install langchain langchain-community openai faiss-cpu tiktoken pandas
```

---

### **4. Set OpenAI API Key**

Set your OpenAI API key to authenticate with OpenAI's API:
## Option 1: Using a `.env` File

1. Create a `.env` file in the root directory of your project.
2. Add the following:

```env
OPENAI_API_KEY=your_openai_api_key

## Option 2:
```bash
export OPENAI_API_KEY="your_openai_api_key"   # On Linux/Mac
set OPENAI_API_KEY=your_openai_api_key        # On Windows
```

> **Note**: Replace `your_openai_api_key` with your actual OpenAI API Key.

---

### **5. Prepare Your Data**

Place your `Tirmidhi.csv` file in the same directory as the script or adjust the file path accordingly.

---

### **6. Run the Project**

Start the application by running the script:

```bash
python langchain_mod.py
```

---

## 🗂️ **How It Works**

1. **Data Loading**:
   - The system loads data from `Tirmidhi.csv`.
2. **Embedding with OpenAI**:
   - Uses OpenAI's embedding API (`text-embedding-ada-002`) to compute embeddings for semantic search.
3. **FAISS Vector Store**:
   - All embeddings are indexed into a FAISS vector store for efficient semantic similarity searches.
4. **Error Handling**:
   - Handles rate limits (429 errors).

---

## ⚙️ **Configuration**

### **API Key**
Set the `OPENAI_API_KEY` environment variable as described above.

### **FAISS Index Path**
The FAISS index is created dynamically during script execution. You can save and load indices for repeated use.

---

## 📊 **Dependencies**

The following libraries are required:

```text
langchain
langchain-community
openai
faiss-cpu
tiktoken
pandas
```

Install them using:

```bash
pip install langchain langchain-community openai faiss-cpu tiktoken pandas
```

---

## 🛡️ **Error Handling**

### **Rate-Limit Errors**

OpenAI's rate limits return HTTP `429`.

---

## 🎯 **Goals & Next Steps**

1. **Enhance Query Efficiency**:
   - Add querying endpoints to interact with FAISS index directly.
2. **Error & Logging Enhancements**:
   - Improve error handling and integrate logging for diagnostics.
3. **Implement a Web Interface**:
   - Use Next.js create a frontend UI for user-friendly search.

---

## 🤝 **Contributors**

- **Ahmed Abd Alfattah**  
  Full-Stack Developer | [LinkedIn](https://www.linkedin.com/in/ahmed-abd-al-fattah-3b371b23a/) | [Email](mailto:ahmedabdalfttah@outlook.com)

---

## 📜 **License**

This project is licensed under the MIT License. You are free to use and modify this codebase for personal and educational purposes.

---

## 💬 **Support**

If you encounter any issues or have questions:

- Create an [Issue](https://github.com/AhmedNewiry/Hadith-Search-System/issues).
- Contact me via email: [ahmedabdalfttah@outlook.com](mailto:ahmedabdalfttah@outlook.com).
