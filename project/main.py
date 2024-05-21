from fastapi import FastAPI

app = FastAPI()

@app.post("/hello")
async def hello(int:int, str:str):
    return{"ola":str, "number":int}