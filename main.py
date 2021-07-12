import uvicorn as uvicorn
from fastapi import FastAPI


'''
python code to call api:
response = requests.get("http://127.0.0.1:8000/{}".format(search_input))
emotion = response.json()["label"]
'''

api = FastAPI()

@api.get("/{input}")
def predict(input: str):
    label1 = "wait and see"
    label2 = "again"
    return {"label1": label1, "label2":label2}




