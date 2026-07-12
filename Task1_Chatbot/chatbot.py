from datetime import datetime
def welcome():
    print("=" * 60)
    print("🤖        Welcome to Rule-Based Chatbot")
    print("=" * 60)

    name = input("Enter your name: ")

    print(f"\nHello, {name}! 👋")
    print("I'm your AI Chatbot.")
    print("\nYou can ask me:")

    print("""
    • hello
    • hi
    • how are you
    • your name
    • what is python
    • what is ai
    • who created python
    • what can you do
    • date
    • time  
    • bye
    """)

    return name


def get_response(user_input):

    responses = {
        "hello": "Hello! 😊 How can I help you?",
        "hi": "Hi! Nice to meet you.",
        "how are you": "I'm doing great. Thanks for asking!",
        "your name": "I'm a Rule-Based Chatbot.",
        "what is python": "Python is a popular programming language.",
        "what is ai": "AI stands for Artificial Intelligence.",
        "who created python": "Python was created by Guido van Rossum.",
        "what can you do": "I can answer basic predefined questions and chat with you."
    }

    return responses.get(
        user_input,
        "Sorry, I don't understand that question."
    )


def chatbot():
    name = welcome()

    while True:

        user_input = input(f"\n{name}: ").lower().strip()

        if user_input == "bye":
            print("\nChatbot: Goodbye! 👋 Have a wonderful day.")
            break

        elif user_input == "date":
            today = datetime.now().strftime("%d-%m-%Y")
            print("Chatbot: Today's date is", today)
            continue

        elif user_input == "time":
            current_time = datetime.now().strftime("%H:%M:%S")
            print("Chatbot: Current time is", current_time)
            continue

        response = get_response(user_input)

        print("Chatbot:", response)


chatbot()

