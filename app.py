from flask import Flask, render_template
import requests

app = Flask(__name__)

NEWS_API_KEY = "5f560b41e1a44e22b3f21bde982a0e72"
NEWS_API_URL = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=5f560b41e1a44e22b3f21bde982a0e72"
def fetch_news():
    response = requests.get(NEWS_API_URL)
    if response.status_code == 200:
        return response.json().get("articles", [])
    return []

@app.route("/")
def home():
    news_articles = fetch_news()
    return render_template("index.html", news=news_articles)


if __name__ == "__main__":
    app.run(debug=True)
