import requests
import pandas
from bs4 import BeautifulSoup

is_asking = True
number_of_words = 0
words_list = []

while is_asking:
    user_word = str(input("Type your word: "))
    if user_word != "" and user_word != "s":
        url = requests.get(f"https://www.larousse.fr/dictionnaires/francais/{user_word}")
        french_dictionary = url.text
        soup = BeautifulSoup(french_dictionary, "html.parser")
        
        info_word = soup.find(name="h2", class_="AdresseDefinition")
        word = info_word.get_text().split("")[1].strip()
        type_of_word = soup.find(name="p", class_="CatgramDefinition").get_text()
        meaning_of_word = soup.find(name="li", class_="DivisionDefinition").get_text()
        full_word_info = {
            "Word: ": word,
            "Type: ": type_of_word,
            "Meaning: ": meaning_of_word
        }
    
    if user_word not in full_word_info:
        word_dict = {key: value for (key, value) in full_word_info.items()}
        words_list.append(word_dict)
        print(words_list)
        data = pandas.DataFrame(words_list)
        data.to_csv("learned_words.csv")

print(data)



