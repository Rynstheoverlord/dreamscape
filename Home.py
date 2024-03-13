import streamlit as st
import requests
from bs4 import BeautifulSoup
import time

st.markdown("""
# Dreamscape **Images**🌌
Here creativity takes shape


""")

st.page_link("Home.py", label=":blue[Go home]")

search_term = st.text_input("Search for an image")

url = rf'https://www.google.no/search?q={search_term}&client=opera&hs=cTQ&source=lnms&tbm=isch&sa=X&safe=active&ved=0ahUKEwig3LOx4PzKAhWGFywKHZyZAAgQ_AUIBygB&biw=1920&bih=982'

query = requests.get(url)

soup = BeautifulSoup(query.content, 'html.parser')

thumbnails = soup.find_all('img')

images = []
image_id = 0

for image in thumbnails:
    src = image.attrs["src"]
    if "https://" in src:
      images.append(src)
    

if st.button("search", use_container_width=True, type="primary"):
  with st.empty():
    progressbar = st.progress(0)
    for i in range(100):
      progressbar.progress(i + 1)
      time.sleep(0.02)
      
    with st.expander(f"{search_term} images:"):
      for image in images:
        image_id += 1
        st.image(image)
        st.download_button(f"Download image {image_id}📩", requests.get(image).content, "dreamscape.png", mime="image/png")
