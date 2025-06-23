# From using internet APIs lessons, feels important to keep this code for future reference.
import requests

API_KEY = "" # Replace with your actual API key
API_BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

def search_articles(search_term):
    params = {
        'q': search_term,
        'api-key': API_KEY
    }
    response = requests.get(API_BASE_URL, params=params)
    return response.json()

def display_results(search_results):
    docs = search_results["response"]["docs"]

    for doc in docs:
        article_web_url = doc["web_url"]
        article_headline = doc["headline"]["main"]

        print(article_headline + " (" + article_web_url + ")")

while True:
    search_term = input("Enter a search term (or 'exit' to quit): ")
    if search_term.lower() == 'exit':
        break

    search_results = search_articles(search_term)
    display_results(search_results)
    print("\n")