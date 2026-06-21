from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI 
import time
from vector import retriever

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

prompt = ChatPromptTemplate.from_template(
    """
    You are an exeprt in answering questions about a pizza restaurant

    Here are some relevant reviews: {reviews}

    Here is the question to answer: {question}
    """
)

chain = prompt | llm 

# response = chain.invoke({"question":"What is the dynamic programming  explain in detail?"})

while True:
    print("\n---------------------------------------------------------------------------------")
    print("Enter your question (or 'q' to quit): ", end="")
    user_input = input()
    if user_input.lower() == 'q':
        break

    # Get relevant documents
    relevant_docs = retriever.invoke(user_input)

    # Format the reviews for the prompt
    reviews = [doc.page_content for doc in relevant_docs]

    for chunk in chain.stream({"reviews": reviews, "question": user_input}):
        for ch in chunk.content:
            print(ch, end="", flush=True)
            time.sleep(0.01)

     
