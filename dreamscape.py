import streamlit as st
import requests, time


def give_feedback():
  with open("feedback.txt", "r") as f:
    fback = f.read()
  with open("feedback.txt", "w") as fb:
    final_feedback = fback + "\n" + feedback
    fb.write(final_feedback)
  st.success("Feedback sent!", icon="✅")

st.markdown("""# DreamScape🌌
Here creativity takes shape""")


def generate_random():
  for i in range(5):
    st.image(f"https://picsum.photos/200/300?random={i}", use_column_width=True)
    st.download_button("Download📩", requests.get(f"https://picsum.photos/500/600?random={i}").content, "imaginate.png", mime="image/png", key=f"{i}")


with st.expander("Random images"):
  generate_random()
  


with st.expander("Get specific image"):
  search = st.number_input("Enter image id", min_value=1)
  
  if st.button("search", use_container_width=True):
    progressbar = st.progress(0)
    for i in range(100):
      progressbar.progress(i + 1)
      time.sleep(0.02)
    st.image(f"https://picsum.photos/id/{int(search)}/200/300", use_column_width=True)

    

    st.download_button("Download📩", requests.get(f"https://picsum.photos/id/{int(search)}/500/600").content, "imaginate.png", mime="image/png")


st.markdown("""---

**Thanks for using this program👏** 
we are consistently updating it to suit user taste.

please don't forget to give your feedback on what you would like to see added to this platform👇
""")

feedback = st.text_input("Give feedback")
st.button("Submit", type="primary", use_container_width=True, on_click=give_feedback)


st.markdown("""**Developer email:** rynstheoverlord@gmail.com✉️""")
