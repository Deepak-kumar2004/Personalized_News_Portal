from flask import Flask, render_template, request
import requests

app = Flask(__name__)

NEWS_API_KEY = "5f560b41e1a44e22b3f21bde982a0e72"
BASE_NEWS_API_URL = "https://newsapi.org/v2/everything"

def format_query(query):
    # Replace spaces with hyphens and 'and' with '&'
    query = query.replace(" ", "-").replace("and", "&")
    return query

def fetch_news(query="Students"):
    formatted_query = format_query(query)
    api_url = f"{BASE_NEWS_API_URL}?q={formatted_query}&apiKey={NEWS_API_KEY}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json().get("articles", [])
    return []

@app.route("/", methods=["GET"])
def home():
    search_query = request.args.get("q", "Students")  # Default query
    news_articles = fetch_news(search_query)
    return render_template("index.html", news=news_articles, search_query=search_query)

if __name__ == "__main__":
    app.run(debug=True)
