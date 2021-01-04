import requests
import json
BASE_URL="http://api.mediastack.com/v1/"
ENDPOINT="news?access_key=9cde38c84a00dcb6dff4040655c635f6"

def get_news(country):
    r=requests.get(BASE_URL+ENDPOINT)
    data=r.json()
    return data
