from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, HTMLResponse
import io
import numpy as np

from typing import Annotated

import cv2 as cv

# /bin/python3.10 /home/ivan/project/python/test_fast_api/api_for_nn/main.py


app = FastAPI()

@app.post("/file")
async def create_files(file: bytes = File(...)):
    stream = io.BytesIO(file)
    
    nparr = np.asarray(bytearray(stream.read()), dtype="uint8")
    image = cv.imdecode(nparr, cv.IMREAD_COLOR)
    
    cv.imwrite("123.png", image)
    
    output = FileResponse(path="123.png")

    return output

@app.get("/")
async def main():
    content = """
<body>
<form action="/file/" enctype="multipart/form-data" method="post">
<input name="file" type="file" multiple>
<input type="submit">
</body>
    """
    return HTMLResponse(content=content)
