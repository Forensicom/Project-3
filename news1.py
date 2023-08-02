feed = feedparser.parse("https://cointelegraph.com/rss")
    feed_title = feed['feed']['title']
    feed_entries = feed.entries
    for entry in feed.entries:
       article_title = entry.title
       article_link = entry.link

    data = {}
    for entry in feed.entries:
     data.setdefault("News",[])
     data.setdefault("link",[])
     data["News"].append(entry.title)
     data["link"].append(entry.link)
    st.dataframe(data,600)
