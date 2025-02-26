from flask import Flask 
# from datetime import datetime
from dotenv import load_dotenv

import requests
import os


load_dotenv()

apiKey = os.getenv("API_KEY")

app = Flask(__name__)

base_url = "https://newsapi.org/v2"

@app.route("/api/v1/news", methods=['GET'])
def news(): 
    url = f'{base_url}/top-headlines?sources=bbc-news&sortBy=publishedAt&apiKey={apiKey}'
    
    res = requests.get(url=url)
    
    if res.status_code == 200 : 
        return dict(status = res.status_code, data = res.json())
    else : 
        return dict(status = res.status_code, message = res.json())    
    


@app.route("/api/v1/news/<query>", methods=['GET']) 
def news_query(query) :
    url = f'{base_url}/everything?q={query}&sortBy=publishedAt&apiKey={apiKey}'
        
    res = requests.get(url=url)
        
    if res.status_code == 200 :
        return dict(status = res.status_code, data = res.json().get("articles"))
        
    else :
        return dict(status = res.status_code, message = res.json())    
    