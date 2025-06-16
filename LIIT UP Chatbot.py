import requests

firstname = input("Enter First Name: ")
surname = input("Enter Surname: ")

print(f"\nWELCOME {firstname.upper()} {surname.upper()} to LITT-UP Assistant 🤖")
print(f"\nHi {firstname}, how are you doing today?")


user_feeling = input(f"You ({firstname}): ").lower()



if any(word in user_feeling for word in ["fine", "good", "great", "okay", "well"]):
    print(f"\nLITT-UP: I'm glad to hear that, {firstname}!")
elif any(word in user_feeling for word in ["unwanted", "bad",  "tired", "sick"]):
    print(f"\nLITT-UP: I'm sorry to hear that, {firstname}. I hope things get better soon!")
else:
    print(f"\nLITT-UP: Thanks for sharing, {firstname}!")


print("\nYou can also ask me how I'm doing!")
follow_up = input(f"You ({firstname}): ").lower()

if "how are you" in follow_up or "are you ok" in follow_up:
    print("\nLITT-UP: I'm doing great, thank you for asking! Ready to help you anytime.")

print("\nHow can I help you today?")
print("You can ask me about code, weather, countries, school advice, or real-world questions.\n")


countries = [
    {"name": "Angola", "population": 39500700, "race": "African"},
    {"name": "Botswana", "population": 44900110, "race": "African"},
    {"name": "Congo DRC", "population": 47160260, "race": "African"},
    {"name": "Egypt", "population": 76800373, "race": "African"},
    {"name": "Nigeria", "population": 172504220, "race": "African"},
    {"name": "China", "population": 345210000, "race": "Asian"},
    {"name": "Japan", "population": 210700023, "race": "Asian"},
    {"name": "India", "population": 1393409038, "race": "Asian"},
    {"name": "Russia", "population": 327509300, "race": "European"},
    {"name": "UK", "population": 310290010, "race": "European"},
    {"name": "Germany", "population": 83240525, "race": "European"},
    {"name": "France", "population": 67364357, "race": "European"}
]

def get_weather(city):
    """Fetch weather info using wttr.in."""
    try:
        response = requests.get(f"https://wttr.in/{city}?format=3")
        return f"\U0001F327 Weather in {city}: {response.text}"
    except Exception as e:
        return f"\u26A0 Error fetching weather: {str(e)}"
while True:
    user_input = input("You: ").lower()

    if "african" in user_input and "population" in user_input:
        print("\nLITT-UP: Here are African countries with population over 10 million:\n")
        print("Country        Population     Race")
        print("---------------------------------------------")
        for country in countries:
            if country["race"] == "African" and country["population"] > 10000000:
                print(f"{country['name']:15} {country['population']:<15,} {country['race']}")
        print()

    elif "asian" in user_input and "population" in user_input:
        print("\nLITT-UP: Here are Asian countries with population over 10 million:\n")
        print("Country        Population     Race")
        print("---------------------------------------------")
        for country in countries:
            if country["race"] == "Asian" and country["population"] > 10000000:
                print(f"{country['name']:15} {country['population']:<15,} {country['race']}")
        print()

    elif "european" in user_input and "population" in user_input:
        print("\nLITT-UP: Here are European countries with population over 10 million:\n")
        print("Country        Population     Race")
        print("---------------------------------------------")
        for country in countries:
            if country["race"] == "European" and country["population"] > 10000000:
                print(f"{country['name']:15} {country['population']:<15,} {country['race']}")
        print()

    elif "president of zimbabwe" in user_input:
        print("\nLITT-UP: As of 2025, the president of Zimbabwe is Emmerson Mnangagwa.\n")
        
    elif "president of america" in user_input:
        print("\nLITT-UP: As of 2025, the president of America is Donald Trump.\n")
        
    elif any(word in user_input for word in ["i am sad and need some advice on feeling better", "how to feel better", "sad", "i need advice"]):
 
        print("\nI'm really sorry you're feeling this way. You're not alone—even if it feels like it right now—and it can get better. Let’s take this one step at a time.\n Here are a few ideas that might help ease the heaviness:\n")
        print("\n🧠 First, name it to tame it.\n")
        print("\nSometimes just saying what’s wrong can help. If you want, tell me what’s on your mind—no judgment, no pressure. I'm here to listen.\n")
       
        print("\n💨 Breathe. Literally.\n")
        
        print("\n Try this right now: \n")
        
        print("\n- Inhale for 4 seconds \n")
        print("\n- Hold it for 4 seconds \n")
        print("\n- Exhale for 6 seconds \n")
        print("\n- Repeat a few times \n")
        print("\n- It calms your nervous system and helps you feel a bit more grounded. \n")
        
        print("\n 💡 Small actions can shift big feelings.\n")
        
        print("\n Even if it’s just:\n")
        
        print("\n- Taking a walk\n")
        print("\n- Drinking a glass of water \n")
        print("\n- Listening to a favorite song or something comforting \n")
        print("\n- Stepping outside for a few minutes of sunlight \n")
        print("\n- These things don't solve everything—but they do help your body support your brain. \n")
        
        print("\n 🤝 Talk to someone you trust.\n")
        print("\n - Whether it’s a friend, family member, or therapist—sharing what you’re going through is powerful. You don’t have to carry it alone.\n")

        print("\n✍️ Try writing.\n")
        
        print("\nYou could jot down:\n")
        print("\n- What you’re feeling\n")
        print("\n- What you wish you were feeling\n")
        print("\n- Something you’re grateful for, even if it’s tiny (like, “I liked my coffee this morning.”)\n")
        print("\n- It rewires the brain over time to be more resilient.\n")
        print("\n- If you’d like to talk about what’s making you sad, I’m here to listen and support you. No pressure—just whatever feels okay for you right now.\n")
        print("\nYou’re not in this alone, Takunda. You're doing better than you think. ❤️\n")   
   

    elif "how can i focus on school" in user_input or "how can i focus on education" in user_input:
        print("\nLITT-UP: Here are tips to stay focused on your education:\n")
        print("- Create a daily study routine")
        print("- Avoid distractions like too much phone time")
        print("- Set small goals and reward yourself")
        print("- Stay around motivated people\n")

    elif "ecocash code" in user_input or "money transfer code" in user_input:
        print("\nLITT-UP: Here's a sample Ecocash code you can use in your own project:")
        print('''
phone = str(input("Run Ecocash code : "))
code = "*151#"

print("Please select your currency")
print("1. Zimbabwe Gold ZWG")
print("2. United States USD")

opt = int(input("Enter your option: "))

if opt == 2:
    print("Welcome to Ecocash USD Wallet.")
    pin = int(input("Please enter your pin to proceed: "))

    if pin == 1976:
        print("1. Send Money")
        print("2. Make Payment")
        print("3. Cash Out")
        print("4. Airtime & Bundles")
        print("5. Financial Services")
        print("6. Wallet Services")
        print("7. Banking Services")
        
        opt = int(input("Enter your option: "))
        if opt == 1:
            number = input("Enter Subscriber number: ")
            amount = input("Enter Amount: ")
            print(f"Sending USD {amount} to {number}")
            print("1. Confirm")
            print("2. Cancel")

            opt = int(input("Enter your option: "))
            if opt == 1:
                print(f"You have successfully sent USD {amount} to {number}")
                print("Thank you for choosing Ecocash!")
    else:
        print("PIN entered is incorrect")
        ''')
        print()
        
    elif "weather" in user_input:
        city = input("Enter city name: ")
        print(get_weather(city))

    elif "thank you" in user_input or "ok that's all for today" in user_input:
        print(f"\nLITT-UP: Goodbye {firstname}! Keep shining ✨\n")
        break

    else:
        print("\nLITT-UP: Sorry, I don’t understand that yet. Try asking something else.\n")