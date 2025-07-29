import requests
from config import HF_API_KEY

def classify_text(text):
    API_URL = "https://api-inference.huggingface.co/models/distillbert-base-uncased-finetuned-sst-2-english"

    headers = {"Autorization": f"Bearer{HF_API_KEY}"}
    payload = {"inputs": text}

    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

if __name__ == "__main__":
    sample_text = "I love using Hungging Face APIs!"

    result  = classify_text(sample_text)
    print(result)