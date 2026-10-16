import fitz
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:3b")
client = OpenAI(api_key="ollama", base_url=OLLAMA_BASE_URL)


def extract_text_from_pdf(uploaded_file):
  """
  Extract text from pdf, upload file : path to the pdf file ,
  and return the extracted text
  """
  doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
  text=""
  for page in doc:
    text += page.get_text()
  return text 

def ask_ollama(prompt, max_tokens=500):
  # Send the prompt to the local Ollama server and return its response.
  response =client.chat.completions.create(
    model=OLLAMA_MODEL,
    messages=[{"role":"user","content":prompt}],
    temperature=0.4,
    max_tokens=max_tokens
  )

  return response.choices[0].message.content

  
