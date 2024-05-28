from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles
import asyncio
import os

count = 0

app = FastAPI()

@app.get("/hello_world")
def hello_world():
    return PlainTextResponse("Hello World!!")

@app.get("/async_hello_world")
async def async_hello_world():
    await asyncio.sleep(1)
    return PlainTextResponse("Async Hello World!!")

@app.get("/api/count")
async def counter():
    global count
    count += 1
    return PlainTextResponse(str(count))

app.mount("/", StaticFiles(directory="./www", html=True), name="html")

os.system("start http://localhost:8080/")
os.system("start http://localhost:8080/hello_world")
os.system("start http://localhost:8080/async_hello_world")
