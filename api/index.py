import json
import base64
from flask import Request, Response
from utils.qa_engine import get_answer

def handler(request: Request) -> Response:
    if request.method != "POST":
        return Response("Only POST allowed", status=405)

    data = request.get_json()
    question = data.get("question", "")
    image = data.get("image", None)

    answer, links = get_answer(question, image=image)

    return Response(
        json.dumps({
            "answer": answer,
            "links": links
        }),
        status=200,
        mimetype="application/json"
    )
