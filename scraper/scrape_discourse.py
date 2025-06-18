import requests
from bs4 import BeautifulSoup
import json

def scrape_discourse(start_url, max_pages=5):
    posts = []
    for page in range(max_pages):
        url = f"{start_url}?page={page+1}"
        print(f"Fetching {url}")
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        topics = soup.select("a.title")
        for t in topics:
            post_url = "https://discourse.onlinedegree.iitm.ac.in" + t['href']
            title = t.text.strip()
            posts.append({
                "url": post_url,
                "title": title,
                "text": title  # Update later with full text scraping
            })
    return posts

if __name__ == "__main__":
    posts = scrape_discourse("https://discourse.onlinedegree.iitm.ac.in/c/tds")
    with open("../embeddings/embed_store.json", "w") as f:
        json.dump(posts, f, indent=2)
