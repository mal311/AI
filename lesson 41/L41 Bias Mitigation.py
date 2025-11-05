import os
from google import genai
from google.genai import types

#Initialize the Gemini API client
client = genai.client(api_key="AIzaSyDu0-jCuQ0OamtxxDxCR1bzEcqx1NUofU0")

def generate_response(prompt, temperature=0.3):
    """Generate a response from Gemini API"""
    try:
        contents = [types.Content(role="user", parts=[types.part.from_text(text=prompt)])]
        config_params = types.GenerateContentConfig(temperature=temperature)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=contents, config=config_params)
        return response.text
    
    except Exception as e:
        return f"Error: {str(e)}"
    
def bias_mitigation_activity():
    """Conducts the bias mitigation activity"""
    print(f"\n === BIAS MITIGATION ACTIVITY ===\n")

    #Get user input for crafting prompt
    prompt = input("Enter a prompt to explore bias (e.g, 'Describe the ideal doctor):")
    initial_response = generate_response(prompt)
    print(f"\nInitial AI Response: {initial_response}")

    #Discuss and modify prompt to reduce bias
    modified_prompt = input("Modify the prompt to make it more neutral (e.g., 'Describe the qualities of a good doctor')")
    modified_response = generate_response(modified_prompt)
    print(f"\nModified AI response (Neutral): {modified_response}")

def token_limit_activity():
    """Conducts the token limit activity"""
    print("\n === TOKEN LIMIT ACTIVITY ===\n")

    #Get user input for long and short prompts
    long_prompt = input("Enter a long prompt (more than 300 words, e.g., a detailed story or description)")
    long_response = generate_response(long_prompt)