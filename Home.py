import streamlit as st
import requests, time
import json
import smtplib


def feedback_message():
  st.success("Feedback sent!", icon="✅")
  

st.markdown("""# DreamScape🌌
Here creativity takes shape



""")


st.page_link("pages/Images.py", label=":blue[click here to search for a specific image here]🖼️")


def generate_random():
  for i in range(5):
    st.image(f"https://picsum.photos/200/300?random={i}", use_column_width=True)

    # download button
    st.download_button("Download📩", requests.get(f"https://picsum.photos/500/600?random={i}").content, "dreamscape.png", mime="image/png", key=f"{i}")


# expander for random images
with st.expander("Random images"):
  generate_random()
  

# expander for getting a particular image

with st.expander("Get specific image"):
  search = st.number_input("Enter image id", min_value=1)
  
  if st.button("search", use_container_width=True):
    with st.empty():
      progressbar = st.progress(0)
      for i in range(100):
        progressbar.progress(i + 1)
        time.sleep(0.02)
      st.write("image:")
    st.image(f"https://picsum.photos/id/{int(search)}/200/300", use_column_width=True)
