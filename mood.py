import string

user_input=str(input("How are you feeling today? ")).lower().split()

happy_words=["happy","joyful","excited","content","cheerful","delighted"]
sad_words=["sad","unhappy","downcast","miserable","dejected","gloomy"]
angry_words=["angry","mad","furious","irate","annoyed","frustrated"]

if any(word in user_input for word in happy_words):
    print("I'm glad to hear that you're feeling happy! Keep smiling! 😊")
elif any(word in user_input for word in sad_words):
    print("I'm sorry to hear that you're feeling sad. Remember, after the rain comes the rainbow. 🌈")
elif any(word in user_input for word in angry_words):
    print("It's okay to feel angry sometimes. Take a deep breath and try to relax. 🧘‍♂️")
else:
    print("Sorry we are unable to analyze your emotion. Please enter in simpler words!🌟")