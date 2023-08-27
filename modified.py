
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'damin' in command:
                command = command.replace('damin', '')
                print(command)
    except Exception as e:
        print(e)
    return command

def run_damin():
    command = take_command()
    if not command:
        return

    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        #pywhatkit.playonyt(song)
        #webbrowser.get('chrome').open(url)
        #webbrowser.open_new(url)
        webbrowser.open_new(pywhatkit.playonyt(song))
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
    else:
        talk('Please say the command again.')

def get_capital(country):
    capitals = {
        'south korea': 'Seoul',
        'england': 'London',
        'tanzania': 'Dodoma',
        'india': 'New Delhi'
    }
    return capitals.get(country, 'Unknown')

def get_ceo(company):
    ceos = {
        'google': 'Sundar Pichai',
        'tesla': 'Elon Musk',
        'yonsei': 'Kim Jongo ㅋ'
        'apple': 'Tim Cook',
        'damin robot': 'Kang Bok Hyun',
        'samsung electronics': 'Hyun Suk Kim'
    }
    return ceos.get(company, 'Unknown')

def get_recipe_ingredients(dish):
    recipe_ingredients = {
        'pepperoni pizza': ['dough', 'tomato sauce', 'mozzarella cheese', 'pepperoni']
    }
    return recipe_ingredients.get(dish, [])

# Additional questions and answers
additional_questions = {
    'what is kimchi': "Kimchi is a traditional Korean side dish made from fermented vegetables, usually napa cabbage and Korean radishes, with a variety of seasonings.",
    'what is bibimbap': "Bibimbap is a popular Korean dish that consists of rice, mixed vegetables, meat, and a spicy sauce.",
}

while True:
    run_damin()

