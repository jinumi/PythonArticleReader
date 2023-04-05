import requests
from bs4 import BeautifulSoup
import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Prompt the user to enter the URL of the article
url = input("Enter the URL of the article: ")

# Send an HTTP GET request to the specified URL
res = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(res.text, 'html.parser')

# Find the <article> element on the page
article_element = soup.find('article')

# If the <article> element was not found, print an error message and exit the program
if article_element is None:
    print("Error: no article found on the page")
    exit()

# Extract the text content of the article from the <article> element
article = article_element.getText().strip()

# Set the rate and volume of the text-to-speech engine
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# Speak the article aloud using the pyttsx3 engine
engine.say(article)
engine.runAndWait()