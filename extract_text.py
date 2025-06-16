import os
from mistralai import Mistral
import apiKey
import base64

def encode_pdf(pdf_path):
    """Encode the pdf to base64."""
    try:
        with open(pdf_path, "rb") as pdf_file:
            return base64.b64encode(pdf_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file {pdf_path} was not found.")
        return None
    except Exception as e:  
        print(f"Error: {e}")
        return None

# Path to pdf
pdf_path = "Input Data/Adbulla/referral_package.pdf"

# Getting the base64 string
base64_pdf = encode_pdf(pdf_path)

api_key = apiKey.MISTRAL_API_KEY
client = Mistral(api_key=api_key)

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document={
        "type": "document_url",
        "document_url": f"data:application/pdf;base64,{base64_pdf}" 
    },
    include_image_base64=True
)

print(ocr_response)
with open("ocr_output.txt", "w", encoding="utf-8") as f:
    f.write(str(ocr_response))