from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles
import asyncio
import os

os.makedirs("./www", exist_ok=True)
with open("./www/index.html", mode="w", encoding="utf-8") as f:
    f.write("Hello World!!<br>This is index.html")
app = FastAPI()

@app.get("/hello_world")
def hello_world():
    return PlainTextResponse("Hello World!!")

@app.get("/async_hello_world")
async def async_hello_world():
    await asyncio.sleep(1)
    return PlainTextResponse("Async Hello World!!")

app.mount("/", StaticFiles(directory="./www", html=True), name="html")

os.system("start http://localhost:8080/")
os.system("start http://localhost:8080/hello_world")
os.system("start http://localhost:8080/async_hello_world")
