# Restaurant Reviews RAG

A beginner-friendly retrieval-augmented generation (RAG) application that answers questions about a pizza restaurant using customer reviews from a CSV file.

The project uses LangChain, Google Gemini, and Chroma. Relevant reviews are retrieved from a local vector database and supplied to Gemini as context before it generates an answer.

## Requirements

- Python 3.10 or later
- A Google Gemini API key

## Setup

1. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install the dependencies:

   ```powershell
   pip install langchain langchain-google-genai python-dotenv langchain-chroma langchain-community
   ```

3. Copy the environment template and add your API key:

   ```powershell
   Copy-Item .env.example .env
   ```

4. Ensure `realistic_restaurant_reviews.csv` is present in the project root.

## Run

```powershell
python main.py
```

Enter a question about the restaurant when prompted. Enter `q` to quit.

## How it works

1. `vector.py` loads the restaurant reviews from the CSV file.
2. Gemini's `gemini-embedding-001` model converts the reviews into embeddings.
3. Chroma stores the embeddings locally in `chroma_db/` and retrieves the two most relevant reviews for each question.
4. `main.py` sends the retrieved reviews and the question to `gemini-2.5-flash`, then streams the answer in the terminal.

## Project structure

```text
.
|-- main.py                          # Interactive question-answering application
|-- vector.py                        # CSV loading, embeddings, and retrieval
|-- realistic_restaurant_reviews.csv # Source review data
|-- requirements.txt                 # Python dependencies
|-- .env.example                     # Environment variable template
`-- chroma_db/                       # Generated local vector database
```

## Environment variables

| Variable | Description |
| --- | --- |
| `GOOGLE_API_KEY` | API key used by the Gemini chat and embedding models |

Keep `.env` private and never commit a real API key to version control.
