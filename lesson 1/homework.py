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

age = input("How old are you?")
if "11" in age or "12" in age or "13" in age or "14" in age or "15" in age:
    print ("So you might be in middle school")
elif "16" in age or "17" in age or "18":
    print ("So you must be in high school!")

hobby = input("What's your favorite hobby?")

print(f"Wow, {hobby} sounds fun!")
print()

color = input("What's your favorite color?")

print(f"I also love {color}")

print(f"it was nice chatting with you {name}, goodbye!")
