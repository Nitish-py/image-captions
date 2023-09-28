import image_caption
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import JSONResponse
from PIL import Image
from io import BytesIO

app=FastAPI()

@app.post("/details")
async def upload_img(file: UploadFile):
    image_data = BytesIO(await file.read())
    print (image_data)
    result=image_caption.main(image_data)
    return result