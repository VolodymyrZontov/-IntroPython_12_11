import requests


url = "http://api.forismatic.com/api/1.0/"

for idx in range(20):
    params = {"method": "getQuote",
              "format": "json",
              "lang": "ru",
              "key": idx}

    response = requests.get(url, params=params)
    response = response.json()
    print(response['quoteText'], response["quoteAuthor"])