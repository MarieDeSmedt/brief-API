from fastapi import FastAPI
import afinn

app = FastAPI()

afinn = afinn()

@app.get("/{input}")
def predict(input: str):
    score = afinn.score(input)
    return {'text': input, 'score': score}