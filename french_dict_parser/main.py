import requests
import pandas
from bs4 import BeautifulSoup

user_word = str(input("Type your word: "))
url = requests.get(
    f"https://www.larousse.fr/dictionnaires/francais/{user_word}")

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
print(full_word_info)

data = pandas.DataFrame.from_dict(full_word_info, orient="index")
data.to_csv("D:/python/practice/new_data.csv")
print(data)
