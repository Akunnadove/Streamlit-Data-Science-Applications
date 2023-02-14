# Import Libraries
import time
import base64
import numpy as np
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import tensorflow_hub as hub
import tensorflow as tf
from PIL import Image
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras import preprocessing

fig = plt.figure()

# Connect to external styling
with open("C:/Users/Akunna Anyamkpa/paga.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Background image variable
img = get_img_as_base64("C:/Users/Akunna Anyamkpa/Downloads/ROR/IMG.png")

# Internal css
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://photos.google.com/search/_tra_/photo/AF1QipMCdsOALI3rVXbXEJSHHkybs76QKApMhawMi5TR");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

# Connect markdown to internal styling
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Let's check!")

st.sidebar.header("Dashboard")


with st.container():
    st.header("Image Classification Project")
    st.markdown("""
    Welcome to this application that classifies the termers into classes respectively.
    - Abyssinia
    - Burma
    - Dalet
    - Mogadishu
    """)

# Main function 
def main():
    # Upload image 
    file_uploaded = st.file_uploader("Select Image", type=["png","jpg","jpeg"])
    if file_uploaded is not None:    
        image = Image.open(file_uploaded)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
    # Process button    
    class_btn = st.button("Process")
    if class_btn:
        if file_uploaded is None:
            st.write("Invalid command, please upload an image")
        else:
            with st.spinner('Model working....'):
                plt.imshow(image)
                plt.axis("off")
                predictions = predict(image)
                time.sleep(1)
                st.success('Classified')
                st.write(predictions)
                st.pyplot(fig)
                
# Connect to model to the app
def predict(image):
    classifier_model = "C:/Users/Akunna Anyamkpa/modela.h5"
    IMAGE_SHAPE = (224, 224,3)
    model = load_model(classifier_model, compile=False, custom_objects={'KerasLayer': hub.KerasLayer})
    test_image = image.resize((224,224))
    test_image = preprocessing.image.img_to_array(test_image)
    test_image = test_image / 255.0
    test_image = np.expand_dims(test_image, axis=0)
    class_names = [
          'Abyssinia termer 1',
          'Abyssinia termer 2',
          'Abyssinia termer 3',
          'Abyssinia termer 4',
          'Abyssinia termer 5',
          'Burma termer 1',
          'Burma termer 2',
          'Burma termer 3',
          'Burma termer 4',
          'Burma termer 5',
          'Dalet termer 1',
          'Dalet termer 2',
          'Dalet termer 3',
          'Dalet termer 4',
          'Dalet termer 5',
          'Mogadishu termer 1',
          'Mogadishu termer 2',
          'Mogadishu termer 3',
          'Mogadishu termer 4',
          'Mogadishu termer 5']
    predictions = model.predict(test_image)
    scores = tf.nn.softmax(predictions[0])
    scores = scores.numpy()
    results = {
          'Abyssinia termer 1': 0,
          'Abyssinia termer 2': 0,
          'Abyssinia termer 3': 0,
          'Abyssinia termer 4': 0,
          'Abyssinia termer 5': 0,
          'Burma termer 1': 0,
          'Burma termer 2': 0,
          'Burma termer 3': 0,
          'Burma termer 4': 0,
          'Burma termer 5': 0,
          'Dalet termer 1': 0,
          'Dalet termer 2': 0,
          'Dalet termer 3': 0,
          'Dalet termer 4': 0,
          'Dalet termer 5': 0,
          'Mogadishu termer 1': 0,
          'Mogadishu termer 2': 0,
          'Mogadishu termer 3': 0,
          'Mogadishu termer 4': 0,
          'Mogadishu termer 5': 0
}

    
    result = f"{class_names[np.argmax(scores)]} with a { (100 * np.max(scores)).round(2) } % confidence." 
    return result


if __name__ == "__main__":
    main()