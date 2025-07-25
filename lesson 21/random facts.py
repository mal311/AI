import requests

#Random facts API endpoint
url = "https://uselessfacts.jsph.pl/random.json?language=en"

#Function to fetch and display a random fact
def get_random_fact():
    response = requests.get(url)
    

    if response .status_code == 200:
        fact_data = response.json()
        print(f"Did you know?{fact_data['text']}")
        print("\n")
    else:
        print("Failed to fetch fact")

#Main loop to interact with the user
while True:
    key = input("Press enter to get a random fact or type 'q' to quit: ")

    if key.lower() == 'q':
        break

    get_random_fact()