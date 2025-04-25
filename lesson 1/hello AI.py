print("Hello! I'm your friendly chatbot.")
name = input("What's your name?")

print(f"Nice to meet you {name}!")

print()

feeling = input("How are you feeling today?")

if "good" in feeling or "great" in feeling or "fine" in feeling: #positive tone
    print("I'm glad to hear that!")
elif "bad" in feeling or "sad" in feeling: #negative tone
    print("I'm sorry to hear that, hope things will get better")
else:
    print("I see. Sometimes it's hard to put feelings into words")

print()
hobby = input("What's your favorite hobby?")

print(f"Wow, {hobby} sounds fun!")
print()

print(f"it was nice chatting with you {name}, goodbye!")