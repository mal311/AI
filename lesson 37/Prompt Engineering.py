from google import genai # Use this for Google Gemini

#Initialize the AI client with the API key from config.py
client = genai.Client(api_key="AIzaSyD2V26IDVoO7UJxo36pfyFHLcCDO0XvvHw")

#Function to generate AI responses
def generate_response(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash", #Or replace with OpenAI's GPT model if using GPT
        contents = prompt
    )

    return response.text

#Function to interactively guide the user in creating specific prompts
def silly_prompt():
    print("Welcome to the AI Prompt Engineering Tutorial!")
    print("In this activity, we will learn about **Clarity and Specifity** and **Contextual Information** in crafting prompts for AI")

    print()

    print("Let's start by crafting a vague prompt, making it more specific, and then adding context")

    print()

    #Step1: vague propmt creation
    print("Please enter a vague prompt (e.g., 'Tell me about technology'): ")
    vague_prompt = input()

    #Generate prompt for vague prompt
    print()
    print(f"Your vague prompt: {vague_prompt}")
    vague_response = generate_response(vague_prompt)

    print()

    print("AI's response to the vague prompt:")
    print(vague_response)

    #Step 2: Make the Prompt Clear and specific
    print()
    print("Now, make the prompt more specific (e.g., 'Explain how AI works in self-driving cars:)")
    specific_prompt = input() 

    #Generate response for specific prompt
    print()
    print(f"Your specific prompt: {specific_prompt}")
    specific_response = generate_response(specific_prompt)

    print()

    print("AI's response to the specific prompt: ")
    print(specific_response)

    #Step 3: Add Context to the Prompt
    print()
    print("Now, add context to your specific prompt (e.g., 'Given the advancement in autonomous vehicles, explain how AI is used in self-driving cars to make real-time driving decisions')")
    contextual_prompt = input()

    #Generate response for Contextual Prompt
    print()
    print(f"Your Contextual Prompt: {contextual_prompt}")
    contextual_response = generate_response(contextual_prompt)

    print()