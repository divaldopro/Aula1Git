from fastapi import FastAPI

app = FastAPI()

@app.get("/")

# 127.0.0.1:8000/
async def root():
    return {"message": "Hello World"}

# 127.0.0.1:8000/teste1
@app.get("/teste1")
async def funcaoteste():
    return {"teste": "deu certo"}

# 127.0.0.1:8000/teste2
@app.get("/teste2")
async def funcaoteste():
    return {"teste2": "deu certo o segundo"}