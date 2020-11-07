from newsapi import NewsApiClient
from flask import Flask, redirect, url_for, render_template, request
import requests
from datetime import timedelta, date

newsapi = NewsApiClient(api_key='78b9d599c4f94f8fa3afb1a5458928d6')


app = Flask(__name__)
@app.route("/")                                                                                                    # home page
def home():
    all_articles = newsapi.get_everything(q="technology OR entertainment OR sports", qintitle="technology OR entertainment OR sports", language="en", sort_by="relevancy",page_size=50, from_param=date.today()-timedelta(days=1), to=date.today())
    return render_template("index.html", articles_list=all_articles['articles'])                                       # newsApi filters everything that is not technology, sports or entertainment



@app.route("/sports/")                                                                                              #sports page
def sports():
    response = newsapi.get_top_headlines(category="sports", country="us", language="en", page_size=50)
    return render_template("index.html", articles_list=response['articles'])

@app.route("/entertainment/")                                                                                   #entertainment page
def entertainment():
    response = newsapi.get_top_headlines(category="entertainment", country="us", language="en", page_size=50)
    return render_template("index.html", articles_list=response['articles'])

@app.route("/technology/")                                                                                          #technology page
def technology():
    response = newsapi.get_top_headlines(category="technology", country="us", language="en", page_size=50)
    return render_template("index.html", articles_list=response['articles'])

@app.route("/search/", methods=["POST","GET"])                                                                            # Only vists this page if the search but has been pressed
def search():

    if request.form["nm"].lower() == "":                                                                                                    # taking user input from search bar
        return home()

    response = newsapi.get_everything(q= "technology OR entertainment OR sports AND " + request.form["nm"],                                 # filtering technology entertainment and sports with user input
                                          qintitle="technology OR entertainment OR sports AND " + request.form["nm"], language="en",
                                          sort_by="relevancy", page_size=50,
                                          from_param=date.today() - timedelta(days=1), to=date.today())
    if response['totalResults'] == 0 or response['status'] != 'ok':                                                                        # checking that search results are valid
        return render_template("zero_results.html")

    return render_template("index.html", articles_list=response['articles'])



if __name__ == "__main__":
    app.run(debug=True)