from flask import Flask, request
import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

apiKey = os.getenv("API_KEY")

app = Flask(__name__)

@app.route("/news/news", methods=['GET'])
def news(): 
    url = f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={apiKey}'
    
    res = requests.get(url=url)
    
    if res.status_code == 200 : 
        return dict(message="success", data=res.json())
    else : 
        return dict(message="failed")    
    


@app.route("/news/news_category") 
def news_by_category() :
    
    date_year = 0
    date_month = 0
    date_day = datetime.now().day
        
    if int(datetime.now().month) == 1 :
        date_year = int(datetime.now().year - 1)
        date_month = 12
    else :
        date_year = int(datetime.now().year)
        date_month = int(datetime.now().month - 1)
        
    date_api = f"{date_year}-{int(date_month)}-{date_day}"
    
    
    slug = request.args.get('slug')
    url = f'https://newsapi.org/v2/everything?q=${slug}&language=es&from={date_api}&sortBy=publishedAt&apiKey={apiKey}'
        
    res = requests.get(url=url)
        
    if res.status_code == 200 and slug :
        return dict(message="success", data=res.json().get("articles"))
        
    else :
        return dict(message="failed") 
    