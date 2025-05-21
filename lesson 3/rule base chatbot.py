import re
import random
from colorama import Fore, init

#Initialize colorama
init(autoreset=True)

# Data structures for travel recommendations and jokes
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    #add cities
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

# Function to greet the user
def greet_user():
    print(Fore.CYAN + "Hello! I am TravelBot, your virtual travel assistant")
    name = input (Fore.YELLOW + "May I know your name?")
    print(Fore.GREEN + f"Nice tp meet you {name}, how can I assist you today?")
    return name

# Function to show help options
def show_help():
    print(Fore.MAGENTA + "\nI can assist you with the following:")
    print(Fore.GREEN + "- Provide travel recommandations")
    print(Fore.GREEN + "- Offer packing tips")
    print(Fore.GREEN + "- Tell travel jokes")
    print(Fore.CYAN + "Just ask me a question or press 'exit' to leave \n")
    
# Function to process user input
def process_input(user_input):
    #convert input to lowercase, remove leading/trailingg spaces, and replace multiple spaces with one
    user_input = user_input.strip().lower()
    user_input = re.sub(r'\s+', ' ', user_input)#replace multiple sapces with a single one
    return user_input

# Function to provide travel recommendations
def provide_recommandations():
    print(Fore.CYAN +"TravelBot: Sure! Are you interested in beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You:")
    preference = process_input(preference) #Normalize the input

    if preference in destinations :
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about visiting {suggestion}")
        print(Fore.CYAN + "TravelBot: Do you like this suggestion? (yes/no)")
        response = input(Fore.YELLOW + "You: ").strip().lower()

        if response == "yes":
            print(f"{Fore.GREEN} TravelBot: Great! ave an aaying time in {suggestion}!")
        elif response == "no":
            print(f"{Fore.RED} TravelBot: No worries! We will find another destination")
            provide_recommandations() #Recur to suggest another destination
        else:
            print(f"{Fore.RED} I didn't catch that. Let's start over.")
            provide_recommandations() #Recur to handle unexpected input
    else:
        print(f"{Fore.RED}TravelBot: Sorry, I don't have recommandation for that preference.")

    # Show the help options again
    show_help()

# Function to offer packing tips
def offer_packing_tips():
    print(f"{Fore.CYAN} TravelBot : Where are you travelling to ?")
    destination = input(f"{Fore.YELLOW} You: ")
    destination = process_input(destination)

    print(f"{Fore.CYAN}TravelBot: How many days will you be staying?")
    days = input(f"{Fore.YELLOW}You: ")

    print(f"{Fore.GREEN}TravelBot: Packing tips for {days} days in {destination}")
    print(Fore.GREEN + "- Pack versatile clothing items.")
    print(Fore.GREEN + "- Don't forget travel adapters and chargers")
    print(Fore.GREEN + "- Check the weather forecast before packing.")


# Function to tell a joke
def tell_joke():
    joke = random.choice(jokes)
    print(f"{Fore.YELLOW}TravelBot: {joke}")

# Main chat function
def chat():
    name = greet_user()
    show_help()
    while True:
        user_input = input(f"{Fore.YELLOW}{name}: ")
        processed_input = process_input(user_input)

        if "recommandation" in processed_input or "suggest" in processed_input:
            provide_recommandations()
        elif "pack" in processed_input or "packing" in processed_input:
            offer_packing_tips()
        elif "joke" in processed_input or "funny" in processed_input:
            tell_joke()
        elif "help" in processed_input:
            show_help()
        elif "exit" in processed_input or "bye" in processed_input:
            print(Fore.CYAN + "TravelBot: Safe travels! goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot:I'm sorry, I didn't quite catch that. Could you rephrase that?")

# Start the chatbot
if __name__ == "__main__":
    chat()
