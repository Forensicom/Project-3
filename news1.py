{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "225ff2f5-9ebb-423d-b426-992b52695b48",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Brazil’s Citrosuco Threatens Force Majeure on Some Orange Juice Supplies[https://www.bloomberg.com/news/articles/2023-07-24/brazil-s-citrosuco-threatens-force-majeure-on-some-juice-supply]\n"
     ]
    }
   ],
   "source": [
    "import feedparser\n",
    "import webbrowser\n",
    "\n",
    "feed = feedparser.parse(\"https://feeds.bloomberg.com/markets/news.rss\")\n",
    "feed_title = feed['feed']['title']\n",
    "feed_entried = feed.entries\n",
    "for entry in feed.entries:\n",
    "    article_title = entry.title\n",
    "    article_link = entry.link\n",
    "    \n",
    "print (\"{}[{}]\".format(article_title, article_link))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0d6deb18-e20c-4441-bde0-f29ddbf8e30d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
