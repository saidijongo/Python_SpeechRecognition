import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

# Initialize speech recognition and text-to-speech engines
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Text-to-speech function
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Speech recognition function
def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'damin' in command:
                command = command.replace('damin', '')
                print(command)
            else:
                command = kakao_speech.recognize(voice.get_raw_data(), language='KOR')
                print(command)
    except Exception as e:
        print(e)
    return command

# Function to handle the main interactions with Damin
def run_damin():
    try:
        command = take_command()
        if not command:
            return

        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('Playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who the heck is' in command:
            person = command.replace('who the heck is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'capital city of' in command:
            countries = ['south korea', 'england', 'tanzania', 'india']
            for country in countries:
                if country in command:
                    capital = get_capital(country)
                    talk(f'The capital city of {country} is {capital}')
                    break
            else:
                talk('I am not sure about the capital of that country.')
        elif 'ceo of' in command:
            companies = ['google', 'tesla', 'apple', 'samsung electronics', 'damin robot']
            for company in companies:
                if company in command:
                    ceo = get_ceo(company)
                    talk(f'The CEO of {company} is {ceo}')
                    break
            else:
                talk('I am not sure about the CEO of that company.')
        elif 'where is damin robot located' in command:
            talk("Damin robot is located in Seoul Seocho-gu, 10 minutes away from Bangbae station.")
        elif 'ingredients of' in command:
            dish = command.replace('ingredients of', '')
            ingredients = get_recipe_ingredients(dish)
            if ingredients:
                talk(f'The ingredients of {dish} are: {", ".join(ingredients)}')
            else:
                talk('I am not sure about the ingredients of that dish.')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'close' in command or 'exit' in command:
            talk('Goodbye!')
            exit()  # Close the program
        else:
            talk('Please say the command again.')
    except KeyboardInterrupt:
        talk('Goodbye!')
        exit()

# Function to get the capital city of a country
def get_capital(country):
    capitals = {
        'south korea': 'Seoul',
        'england': 'London',
        'tanzania': 'Dodoma',
        'india': 'New Delhi'
    }
    return capitals.get(country, 'Unknown')

# Function to get the CEO of a company
def get_ceo(company):
    ceos = {
        'google': 'Sundar Pichai',
        'tesla': 'Elon Musk',
        'apple': 'Tim Cook',
        'damin robot': 'Kang Bok Hyun',
        'samsung electronics': 'Hyun Suk Kim'
    }
    return ceos.get(company, 'Unknown')

# Function to get the recipe ingredients of a dish
def get_recipe_ingredients(dish):
    recipe_ingredients = {
        'pepperoni pizza': ['dough', 'tomato sauce', 'mozzarella cheese', 'pepperoni'],
    }
    return recipe_ingredients.get(dish, [])

# Main loop
while True:
    run_damin()
