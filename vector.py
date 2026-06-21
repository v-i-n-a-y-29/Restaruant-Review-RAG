# %%
from dotenv import load_dotenv
from langchain_community.document_loaders import CSVLoader
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings


loader  = CSVLoader(file_path="realistic_restaurant_reviews.csv", encoding="utf-8")

load_dotenv()

# %%
docs = loader.load()

print(f"Loaded {len(docs)} documents from the CSV file.")

# %%
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

vector_store = Chroma(
    collection_name="restaurant_reviews",
    embedding_function=embeddings,
    persist_directory="chroma_db"
)

# %%
vector_store.add_documents(docs)

# %%
retriever = vector_store.as_retriever(search_kwargs={"k": 2})
