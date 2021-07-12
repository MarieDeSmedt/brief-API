import streamlit as st
import requests

from page import Page

# ############################################################################################


def display_detector():
    search_input = st.text_input('Tell me something...', '')
    if len(search_input) > 0:
        response = requests.get("https://lit-spire-48980.herokuapp.com/{}".format(search_input))
        emotion = response.json()["emotion"]
        st.write(emotion)
        response = requests.get(
            "https://api.giphy.com/v1/gifs/random?api_key=u5zI8PiTKx0y7b6Csh5GmUdhgD0hZ315&tag={}&rating=g".format(
                emotion))
        image_url = response.json()["data"]["image_original_url"]
        st.image(image_url)


# ##########################################################################################
st.sidebar.markdown("### test d'API")
app = Page()
app.add_page("Detector", display_detector)
app.run()