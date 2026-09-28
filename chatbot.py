print("Namaste! welcome to your Chatbot")
print("You can ask me basic question, Type 'bye' to exit from the bot")

#Chatbot memory creation [ dictionary of responses]

responses = {
    "hello": "Hi, welcome. how can i help you?",
    "how are you": "i am very fine. Thank you",
    "who are you": "i am smart AI chatbot",
    "motivate me": "keep going. Every bug of your project makes you a better devoloper",
    "happy": "great to hear that",
}

#Method/Functions to get response of chatbot

def getResponseBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey, response in responses.items():
        if eachKey in userQuestion:
            return response
    return "Sorry, I don't understand that question. i will laern quickly"

# take user input
while True:
    userInput = input("Please ask your question: ")
    if userInput.lower() == "bye":
        print("Goodbye!")
        break
    print(getResponseBot(userInput))