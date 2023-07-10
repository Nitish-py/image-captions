#from transformers import AutoProcessor, BlipForConditionalGeneration
import streamlit as st
from PIL import Image
import requests

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query(data):
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()[0].get('generated_text')
def main():
    st.set_page_config(page_title="Image Captioning and Title")
    st.header("Image captioning and Title")

    image_upload = st.file_uploader("Upload your image", type=["jpeg", "jpg", "png"])
    if image_upload is not None:
        image_data=image_upload.read()
        disimg=Image.open(image_upload)
        st.image(disimg)
        response=query(image_data)
        st.write("Caption")
        st.success(response)
        return response

if __name__=="__main__":
    main()