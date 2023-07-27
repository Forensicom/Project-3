import feedparser
import webbrowser
import streamlit as st
import pandas as pd
feed = feedparser.parse("https://cointelegraph.com/rss")
feed_title = feed["feed"]["title"]
feed_entried = feed.entries
for entry in feed.entries:
    article_title = entry.title
    article_link = entry.link
    
data = {}
for entry in feed.entries:
    data.setdefault("title",[])
    data.setdefault("link",[])
    data["title"].append(entry.title)
    data["link"].append(entry.link)

data
