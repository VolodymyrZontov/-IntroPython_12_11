import requests
from requests_oauthlib import OAuth1
import os
from dotenv import load_dotenv

load_dotenv()

auth = OAuth1(os.getenv('KEY'), os.getenv('SECRET'))
endpoint = "http://api.thenounproject.com/icon/1"

response = requests.get(endpoint, auth=auth)
print(response.content)


