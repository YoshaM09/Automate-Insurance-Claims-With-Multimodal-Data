import os
from mistralai import Mistral
import apiKey

# Retrieve the API key
api_key = apiKey.MISTRAL_API_KEY

# Specify model
model = "mistral-small-latest"

# Initialize the Mistral client
client = Mistral(api_key=api_key)

#upload local document and retrieve the signed url
uploaded_pdf = client.files.upload(
    file={
        "file_name": "uploaded_file.pdf",
        "content": open("Input Data/Adbulla/referral_package.pdf", "rb"),
    },
    purpose="ocr"
)
signed_url = client.files.get_signed_url(file_id=uploaded_pdf.id)

# Define the messages for the chat
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Extract text content while maintaining document structure and hierarchy"
            },
            {
                "type": "document_url",
                #"document_url": "https://arxiv.org/pdf/1805.04770"
                "document_url": signed_url.url
            }
        ]
    }
]

# Get the chat response
chat_response = client.chat.complete(
    model=model,
    messages=messages
)

# Print the content of the response
print(chat_response.choices[0].message.content)

# Store the content of the response in text file
with open("pdf_ocr_output.txt", "w", encoding="utf-8") as f:
    f.write(str(chat_response.choices[0].message.content))
