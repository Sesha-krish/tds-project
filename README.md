# TDS Virtual TA 🤖

Auto-answer student questions for the IITM Data Science "Tools in Data Science" course using scraped Discourse and course content.

### 🔧 Features
- Fast API response with GPT-3.5
- Discourse scraping included
- Vercel serverless deployment

### 🚀 Deploy
1. Clone repo
2. Run scraper: `python scraper/scrape_discourse.py`
3. Commit `embeddings/embed_store.json`
4. Deploy to Vercel (see below)

### ⚙️ Local Testing

```bash
curl -X POST https://<your-vercel-url>/api \
  -H "Content-Type: application/json" \
  -d '{"question": "Which model to use for GA5 Q8?"}'
