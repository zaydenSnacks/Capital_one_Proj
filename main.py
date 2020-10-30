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
    response = newsapi.get_top_headlines(category="sports", country="us", language="en", page_size=50)
    return render_template("index.html", articles_list=response['articles'])

@app.route("/entertainment/")
def entertainment():
    response = newsapi.get_top_headlines(category="entertainment", country="us", language="en", page_size=50)
    return render_template("index.html", articles_list=response['articles'])

@app.route("/technology/")
def technology():
    response = newsapi.get_top_headlines(category="technology", country="us", language="en", page_size=50)
    return render_template("index.html", articles_list=response['articles'])

@app.route("/search/", methods=["POST", "GET"])
def search():

    if request.form["nm"] == "":
        return home()

    response = newsapi.get_everything(q= "technology OR entertainment OR sports AND " + request.form["nm"] + " NOT politics",
                                          qintitle="technology OR entertainment OR sports AND " + request.form["nm"], language="en",
                                          sort_by="relevancy", page_size=40,
                                          from_param=date.today() - timedelta(days=1), to=date.today())
    if response['totalResults'] == 0:
        return render_template("zero_results.html")

    return render_template("index.html", articles_list=response['articles'])



if __name__ == "__main__":
    app.run(debug=True)