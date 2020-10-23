from newsapi import NewsApiClient
from flask import Flask, redirect, url_for, render_template
import requests

newsapi = NewsApiClient(api_key='579c378a51e64237a1a1ad13d9069103')
url = ('https://newsapi.org/v2/top-headlines?country=us&category=entertainment&category=sports&category=technology&apiKey=579c378a51e64237a1a1ad13d9069103')
response = requests.get(url).json()


app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html", articles_list=response['articles'])


if __name__ == "__main__":
    app.run(debug=True)