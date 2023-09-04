from fastapi import FastAPI
import socket
import os

app = FastAPI()

@app.get("/hostname")
def get_hostname():
    return {"hostname": socket.gethostname()}

@app.get("/author")
def get_author():
    author = os.getenv("AUTHOR", "Author not set. ")
    return {"author": author}

@app.get("/id")
def get_id():
    uuid = os.getenv("UUID", "UUID not set. ")
    return {"id": uuid}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
