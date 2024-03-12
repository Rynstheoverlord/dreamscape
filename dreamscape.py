import streamlit as st
import requests, time
import json
import smtplib


def feedback_message():
  st.success("Feedback sent!", icon="✅")
  

st.markdown("""# DreamScape✨
Here creativity takes shape""")


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

    

    st.download_button("Download📩", requests.get(f"https://picsum.photos/id/{int(search)}/500/600").content, "dreamscape.png", mime="image/png")


# expandable for dogs
with st.expander("Find dog media here"):
  if st.button("Generate media", use_container_width=True):
    with st.empty():
      progressbar = st.progress(0)
      for i in range(100):
        progressbar.progress(i + 1)
        time.sleep(0.02)
      st.write("Dog stuff🐕:")
    url = "https://random.dog/woof.json?ref=apilist.fun"
    query = requests.get(url)
    response = json.loads(query.content.decode('utf-8'))
    if response["url"].split(".")[-1] == "mp4":
      st.video(requests.get(response["url"]).content, format="video/mp4")
      
    else:
      st.image(response["url"])
      st.download_button("Download📩", requests.get(response['url']).content, "dreamscape.png", mime="image/png")


# the final markdown
st.markdown("""---

**Thanks for using this program👏** 
we are consistently updating it to suit user taste.

please don't forget to give your feedback on what you would like to see added to this platform👇
""")

feedback = st.text_input("Give feedback")

if st.button("Submit", type="primary", use_container_width=True):
    # creates SMTP session
  
  print(feedback)
  
  s = smtplib.SMTP('smtp.gmail.com', 587)
  # start TLS for security
  s.starttls()
  # Authentication
  
  s.login("thecodegeniedev@gmail.com", "lqgl hmlm gzzq yyxy")
  # message to be sent
  
  message = f"""\
  Subject: feedback from DreamScape.


  Message:
  {feedback}"""
  # sending the mail
  
  s.sendmail("thecodegeniedev@gmail.com", "rynstheoverlord@gmail.com", message)
  # terminating the session
  s.quit()
  feedback_message()
  


st.markdown("""**Developer email:** rynstheoverlord@gmail.com✉️""")
