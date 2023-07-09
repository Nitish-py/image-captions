#from transformers import AutoProcessor, BlipForConditionalGeneration
import streamlit as st
from PIL import Image
import requests

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query(data):
    response = requests.post(API_URL, headers=headers, data=data)
    return response.content
def main():
    st.set_page_config(page_title="Image Captioning and Title")
    st.header("Image captioning and Title")

    image_upload = st.file_uploader("Upload your image", type=["jpeg", "jpg", "png"])
    if image_upload is not None:
        image_data=image_upload.read()
        #img = Image.open(io.BytesIO(image_data))
        disimg=Image.open(image_upload)
        st.image(disimg)
        response=query(image_data)
        '''processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
        inputs = processor(images=input_img, return_tensors="pt")
        pixel_values = inputs.pixel_values
        generate_id = model.generate(pixel_values=pixel_values, max_length=50)
        caption = processor.batch_decode(generate_id, skip_special_tokens=True)[0]
        '''
        st.write("Caption")
        st.success(response)
        return response

if __name__=="__main__":
    main()