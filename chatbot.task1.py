import datetime

def greeting():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<=12:
        print("ChatBot: Good morning!")
    elif hour>12 and hour<=17:
        print("ChatBot: Good afternoon!")
    else:
        print("ChatBot: Good evening!")

    print("ChatBot: Welcome to Terminals, I'm here to assist you.")

def get_user_input(prompt):
    return input(f"ChatBot: {prompt}\nHuman: ").lower()

def ask():
    q1=input("ChatBot: how are you?\nHuman: ")
    if 'good' in q1 or 'fine' in q1 or 'great' in q1:
        print("ChatBot: That's good to hear!")
    elif "bad" in q1 or "sad" in q1:
        print("ChatBot: I'll try to make it better")

def terminal():
    flight = input("ChatBot: Please enter your flight number: ").lower()
    if any(char in flight for char in ['a', 'b', 'c']):
        print(f"ChatBot: Please go to terminal number 2. Your flight {flight} is waiting for you. Happy journey!")
    elif any(char in flight for char in ['d', 'e', 'f']):
        print(f"ChatBot: Please go to terminal number 13. Your flight {flight} is waiting for you. Happy journey!")
    else:
        print(f"ChatBot: Please go to terminal number 44. Your flight {flight} is waiting for you. Happy journey!")

def eating():
    food = get_user_input("What would you like to eat?")
    if any(word in food for word in ['pastries', 'cake', 'sweets', 'chocolate', 'ice cream']):
        print("ChatBot: Please go to the premium stores on your right. They offer tasty sweets, cakes, chocolates, and more. Have fun!")
    elif any(word in food for word in ['kebab', 'biryani', 'fish fry', 'meal', 'vegetarian', 'non veg']):
        print("ChatBot: Please go to the second floor and take the first left. You'll find various shops offering delicious meals and all types of food.")

def airport():
    user_input = get_user_input("How may I help you?")
    if "terminal" in user_input:
        terminal()
    elif any(word in user_input for word in ['collect','luggage']):
        print("ChatBot: You can collect your luggage on the ground floor near terminal 1. Hope you had a good flight!")
    elif "check in" in user_input:
        print("ChatBot: The check-in counter is just a few meters from here. Keep going straight and then take a left. You'll find it. Happy journey!")
    elif any(word in user_input for word in ['eat', 'lunch', 'dinner', 'breakfast', 'hungry', 'food']):
        eating()
    elif any(word in user_input for word in ['gift', 'present','gifts','presents']):
        print("ChatBot: If you go to the 3rd floor, you'll find various shops full of gifting items. You can choose the ideal gift for your loved ones!")
    elif any(word in user_input for word in ['washroom', 'toilet','restroom', "men's restroom", "women's restroom"]):
        print("ChatBot: Please go to the first right and then take a left.")
    else:
        print("ChatBot: I didn't get that. Could you please repeat?")

    response = get_user_input("Anything else I may help you with? (yes/no)")
    return response.lower() not in ['no', 'nope', 'nah']

def main():
    greeting()
    ask()
    while True:
        if not airport():
            break
    print('ChatBot: It was great talking to you!')

main()
