import streamlit as st
import requests
import pycountry


def news_page():
    st.title("News")
    
    
    
    url = f"https://newsapi.org/v2/top-headlines?q=tesla&from=2025-04-13&sortBy=publishedAt&apiKey=c26cf665c11b4d488eec82f902266818"

    r = requests.get(url)
    r = r.json()
    articles = r['articles']
    for article in articles:
        st.header(article['title'])
        st.write(article['publishedAt'])
        if article['author']:
            st.write(article['author'])
        st.write(article['source']['name'])
        if article['urlToImage']:
            st.image(article["urlToImage"])
        st.write(article['description'])
        if article["url"]:
            st.write(article['url'])

