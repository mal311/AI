# Import necessary libraries
from textblob import TextBlob# - TextBlob for natural language processing tasks like sentiment analysis
import colorama
from colorama import Fore, Style# - Colorama for colored terminal output
import sys   # - sys and time for animations and delays
import time

# Initialize Colorama to reset terminal colors automatically after each output
colorama.init(autoreset=True)

# Define global variables
user_name = "" # - `user_name`: To store the name of the user (Agent)
conversation_history = [] # - `conversation_history`: A list to store all user inputs
positive_count = 0
negative_count = 0
neutral_count = 0# - Sentiment counters (`positive_count`, `negative_count`, `neutral_count`) to track sentiment trends

# Define a function to simulate a processing animation
def show_processing_animation():
    print(f"{Fore.CYAN}Detecting sentiment clues",end="")# - Prints "loading dots" to make the chatbot feel interactive
    for _ in range(3):# - Use a loop to display three dots with a slight delay
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush()

# Define a function to analyze sentiment of the text
def analyze_sentiment(text):
    global positive_count, negative_count, neutral_count

    try:
        blob = TextBlob(text)# - Use TextBlob to calculate the polarity of the input text
        sentiment = blob.sentiment.polarity# - Categorize the sentiment into "Very Positive," "Positive," "Neutral," "Negative," or "Very Negative"
        conversation_history.append(text)# - Append the user input to `conversation_history`

        # - Update the sentiment counters based on the category
        if sentiment > 0.75:
            positive_count += 1
            return f"\n{Fore.GREEN}🌟 Very Positive sentiment detected, Agent {user_name}! (Score: {sentiment:.2f})"
        elif 0.25 < sentiment <= 0.75:
            positive_count +=1
            return f"\n{Fore.GREEN}😊 Positive sentiment detected, Agent {user_name}! (Score: {sentiment:.2f})"
        elif -0.25 <= sentiment <=0.25:
            neutral_count +=1
            return f"\n{Fore.YELLOW}😐 Neutral sentiment detected."
        elif -0.75 <= sentiment >= -0.25:
            negative_count +=1
            return f"\n{Fore.RED}💔 Negative sentiment detected, Agent {user_name}. (Score: {sentiment:.2f})"
        else:
            negative_count +=1 
            return f"\n{Fore.RED}💔 Very Negative sentiment detected, Agent {user_name}. (Score: {sentiment:.2f})"
        
    except Exception as e:
        # - Handle exceptions to avoid crashes
        return f"{Fore.RED} An error occured during sentiment analysis: {str(e)}"

# Define a function to handle commands
# - Handle commands like `summary`, `reset`, `history`, and `help`
def execute_command(command):
    global conversation_history, positive_count, negative_count, neutral_count

    if command == "summary":
        # - `summary`: Displays the count of positive, negative, and neutral sentiments
        return(f"{Fore.CYAN}🕵️Mission Report:\n"
               f"{Fore.GREEN}Positive messages detected:{positive_count}\n"
               f"{Fore.RED}Negative messages detected:{negative_count}\n"
               f"{Fore.YELLOW}Neutral messages detected:{neutral_count}\n")
    elif command == "reset":
        # - `reset`: Clears the conversation history and resets counters
        conversation_history.clear()
        positive_count = negative_count = neutral_count = 0
        return f"{Fore.CYAN}🕵️Mission reset! all previous data has been cleared."
    elif command == "history":
        # - `history`: Shows all previous user inputs
        return "\n".join([f"{Fore.CYAN}Message {i+1}: {msg}" for i, msg in enumerate (conversation_history)]) \
                if conversation_history else f"{Fore.YELLOW} No conversation histpry available"
    elif command == "help":
        # - `help`: Displays a list of available commands
        return (f"{Fore.CYAN}🔍 Available commands:\n"
                f"- Type any sentence to analyze its sentiment.\n"
                f"- Type 'summary' to get a mission report on analyzed sentiments.\n"
                f"- Type 'reset' to clear all mission data and start fresh.\n"
                f"- Type 'history' to view all previous messages and analyses.\n"
                f"- Type 'exit' to conclude your mission and leave the chat.")
    else:
        # - Return appropriate responses for each command
        return f"{Fore.RED}Unknown command. Type help for a list of commands."

# Define a function to validate the user's name
def get_valide_name():
    # - Continuously prompt the user for a name until they enter a valid alphabetic string
    while True:
        name = input("What's your name?").strip()# - Strip any extra spaces and ensure the input is not empty or invalid
        if name and name.isalpha():
            return name
        else:
            print(f"{Fore.RED}Please enter a valid name with only alphabetic characters.")

# Define the main function to start the chatbot
def start_sentiment_chat():
    print(f"{Fore.CYAN}{Style.BRIGHT}🕵️ Welcome to sentiment spy! Your personnal emotion detective is here!")# - Display a welcome message and introduce the Sentiment Spy activity
    # - Ask the user for their name and store it in the `user_name` variable
    global user_name
    user_name = get_valide_name()
    print(f"\n{Fore.CYAN}Nice to meet you agent{user_name} ! Type your sentences to analyse emotions. type 'help' for options")
    # - Enter an infinite loop to interact with the user:
    #   - Prompt the user to enter a sentence or command
    while True:
        #   - Check for empty input and prompt the user to enter a valid sentence
        user_input = input(f"\n{Fore.MAGENTA}{Style.BRIGHT}Agent {user_name} : {Style.RESET_ALL}").strip()
        #   - If the input matches specific commands (`exit`, `summary`, `reset`, `history`, `help`), execute the corresponding functionality
        if not user_input:
            print(f"{Fore.RED} Please enter a nonempty message or type 'help' for available commands")
            continue

        if user_input.lower() == 'exit':
            print(f"\n{Fore.BLUE}🔚 Mission complete! Exiting sentiment spy. Farewell, agent {user_name}!")
            print(execute_command("summary"))
            break
        elif user_input.lower() in ["summary", "reset", "history", "help"]:
            print(execute_command(user_input.lower()))
        #   - Otherwise, call the `analyze_sentiment` function to analyze the input text
        else:
            show_processing_animation()
            result = analyze_sentiment(user_input)
            print(result)
#   - Display the sentiment analysis result with color-coded feedback
# - Exit the loop and display a final summary when the user types `exit`

# Define the entry point for the script
# - Ensure the chatbot starts only when the script is run directly (not imported)
# - Call the `start_sentiment_chat` function to begin the activity
if __name__ == '__main__':
    start_sentiment_chat()