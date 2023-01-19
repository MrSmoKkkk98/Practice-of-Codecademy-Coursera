import requests
import pandas
from bs4 import BeautifulSoup

is_asking = True
number_of_words = 0
dict = {}
while is_asking:
    user_word = str(input("Type your word: "))
    number_of_words += 1
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
        
        for _ in range(number_of_words):
            dict = {key: value for (key, value) in full_word_info.items()}
            print(dict)
        # dict = {key: value for (key, value) in full_word_info.items()}
        # print(dict)
        # for _ in range(number_of_words):
        #     print(full_word_info)
        #     all_words = {key: value for (key, value) in full_word_info.items()}
        #     print(all_words)
        # data = pandas.DataFrame.from_dict(all_words, orient="index")
        # data.to_csv("french_dict_parser/new_data.csv")
    # print(data)
else:
    pass


