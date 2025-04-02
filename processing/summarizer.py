import openai
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the prompt template for summarization
def summarize_paper(text):
    llm = OpenAI(temperature=0.7, model="gpt-3.5-turbo")
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Summarize the following research paper:\n{text}"
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    summary = chain.run(text)
    return summary