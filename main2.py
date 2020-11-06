from newsapi import NewsApiClient
from flask import Flask, redirect, url_for, render_template, request
import requests
from datetime import timedelta, date

newsapi = NewsApiClient(api_key='579c378a51e64237a1a1ad13d9069103')

hashSet = set()
all_articles = newsapi.get_sources(category="technology", country="us", language="en") #newsapi.get_everything(q="technology OR entertainment OR sports", qintitle="technology OR entertainment OR sports AND bitcoin", language="en", sort_by="relevancy",page_size=40, from_param=date.today()-timedelta(days=1), to=date.today())


print(all_articles)
# for i in range(len(all_articles['articles'])):
#     hashSet.add(all_articles['articles'][i]['source']['name'])
#
# print(len(hashSet))