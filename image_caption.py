#from transformers import AutoProcessor, BlipForConditionalGeneration
#import streamlit as st
#from PIL import Image
import requests
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = "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"
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query(data):
    response = requests.post(API_URL, headers=headers, data=data)
    print (response)
    return response.json()[0].get('generated_text')

def main(image_data):
    #st.set_page_config(page_title="Image Captioning and Title")
    #st.header("Image captioning and Title")

    #image_upload = st.file_uploader("Upload your image", type=["jpeg", "jpg", "png"])
    #if image_upload is not None:
    #image_data=image_upload.read()
    #disimg=Image.open(image_upload)
    #st.image(disimg)
    response=query(image_data)
    title= openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{
        "role": "user",
        "content": 'just give a Title of an image for which the caption is:'+response
    }])
    #st.write("Title")
    #st.success(title.choices[0].message.content)
    #st.write("Caption")
    #st.success(response)
    description= openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{
        "role": "user",
        "content": 'just give a description of an image for which the caption is:'+response
    }])
    category= openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{
        "role": "user",
        "content": 'just give a category of an image for which the caption is:'+response
    }])
    #st.write("Description")
    #st.success(description.choices[0].message.content)
    return {'title':title.choices[0].message.content,'title_token':title.usage, 'caption':response, 'description':description.choices[0].message.content, 'decription_token':description.usage, 'category':category.choices[0].message.content, 'category_token': category.usage}

if __name__=="__main__":
    main() 
