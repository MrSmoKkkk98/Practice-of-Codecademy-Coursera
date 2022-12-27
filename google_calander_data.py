from bs4 import BeautifulSoup
import requests

url = requests.get("https://calendar.google.com/calendar/u/0/r")

google_calendar = url.text
soup = BeautifulSoup(google_calendar, "html.parser")

title = soup.find(string=True)
print(title)