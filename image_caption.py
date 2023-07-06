from transformers import AutoProcessor, BlipForConditionalGeneration
import streamlit as st
from PIL import Image

def main():


    st.set_page_config(page_title="Image Captioning and Title")
    st.header("Image captioning and Title")

    image_upload = st.file_uploader("Upload your image", type=["jpeg", "jpg", "png"])
    if image_upload is not None:
        input_img = Image.open(image_upload)
        st.image(input_img)
        processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        inputs = processor(images=input_img, return_tensors="pt")
        pixel_values = inputs.pixel_values
        generate_id = model.generate(pixel_values=pixel_values, max_length=50)
        caption = processor.batch_decode(generate_id, skip_special_tokens=True)[0]
        
        st.write("Caption")
        st.success(caption)
        return caption

if __name__=="__main__":
    main()