from newsapi import NewsApiClient
from flask import Flask, redirect, url_for, render_template, request
import requests
from datetime import timedelta, date

newsapi = NewsApiClient(api_key='579c378a51e64237a1a1ad13d9069103')


app = Flask(__name__)
@app.route("/")
def home():
    all_articles = newsapi.get_everything(q="technology OR entertainment OR sports", qintitle="technology OR entertainment OR sports", language="en", sort_by="relevancy",page_size=40, from_param=date.today()-timedelta(days=1), to=date.today())
    return render_template("index.html", articles_list=all_articles['articles'])



@app.route("/sports/")
def sports():
    url = ('https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=579c378a51e64237a1a1ad13d9069103')
    response = requests.get(url).json()
    return render_template("index.html", articles_list=response['articles'])

@app.route("/entertainment/")
def entertainment():
    url = ('https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=579c378a51e64237a1a1ad13d9069103')
    response = requests.get(url).json()
    return render_template("index.html", articles_list=response['articles'])

@app.route("/technology/")
def technology():
    url = 'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=579c378a51e64237a1a1ad13d9069103'
    response = requests.get(url).json()
    return render_template("index.html", articles_list=response['articles'])

@app.route("/search/", methods=["POST", "GET"])
def search():
    url = ('https://newsapi.org/v2/top-headlines?q=' + request.form["nm"] + '&country=us&category=entertainment&category=sports&category=technology&apiKey=579c378a51e64237a1a1ad13d9069103')
    response = requests.get(url).json()
    return render_template("index.html", articles_list=response['articles'])


if __name__ == "__main__":
    app.run(debug=True)