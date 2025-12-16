from xinference.client import RESTfulClient
import json

# Xinference service URL
client = RESTfulClient("") # Model URL

# Model name or UID
model = client.get_model("") # Model Name


with open("Questions.txt", "r", encoding="utf-8") as f:
    questions = [q.strip() for q in f if q.strip()]

with open("answers.jsonl", "w", encoding="utf-8") as out:
    for idx, question in enumerate(questions, 1):
        response = model.chat(
            messages=[
        {"role": "user", "content": question}
    ],
            temperature=0.9,
            max_tokens=4096 
        )

        record = {
            "id": idx,
            "question": question,
            "answer": response,
        }
        out.write(json.dumps(record, ensure_ascii=False) + "\n")
        print(f"[{idx}/{len(questions)}] done")