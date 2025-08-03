from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

load_dotenv
# Konfigurasi API Key OpenAI
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Prompt Template untuk validasi
validator_prompt = PromptTemplate(
    input_variables=["question"],
    template=(
        "Apakah pertanyaan berikut berkaitan dengan topik perikanan? "
        "Jawab hanya dengan 'ya' atau 'tidak'.\n\n"
        "Pertanyaan: {question}\n"
    ),
)

# Integrasi LLM untuk validasi
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0)
validator_chain = LLMChain(llm=llm, prompt=validator_prompt)

# Fungsi Validator
def fisheries_validator(question):
    response = validator_chain.run(question=question).strip().lower()
    return response == "ya"
