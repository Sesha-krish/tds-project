import json
import openai
from sentence_transformers import SentenceTransformer, util

import os
from openai import OpenAI

openai.api_key = os.getenv("OPENAI_API_KEY")

embedder= SentenceTransformer("paraphrase-MiniLM-L3-v2")  # MUCH lighter


with open("embeddings/embed_store.json", "r") as f:
    knowledge_base = json.load(f)

corpus = [entry['text'] for entry in knowledge_base]
corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)

def get_answer(question, image=None):
    q_embed = embedder.encode(question, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(q_embed, corpus_embeddings)[0]
    top_results = scores.topk(3)

    context = ""
    links = []

    for score, idx in zip(top_results.values, top_results.indices):
        entry = knowledge_base[idx]
        context += entry['text'] + "\n"
        links.append({
            "url": entry.get("url", "#"),
            "text": entry.get("title", "Reference")
        })

    # Compose prompt
    prompt = f"""Answer the following question using the context below.

Context:
{context}

Question: {question}
Answer:"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You're a helpful teaching assistant for the TDS course."},
            {"role": "user", "content": prompt}
        ]
    )

    return response['choices'][0]['message']['content'].strip(), links
