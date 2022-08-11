from fastapi import FastAPI
app = FastAPI()

@app.get("/kindle")
def hello(url: str):
  return 'Hello ' + name + '!'
