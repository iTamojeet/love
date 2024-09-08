import streamlit as st
from datetime import datetime

st.set_page_config(layout="wide")

st.title("A Special App Just for YOU 💕")

st.header("A little surprise for my favorite person ~~~ 😍")

input_container = st.container()
with input_container:
    her_name = st.text_input("Enter your first name please: ").title()

    if her_name():
        st.subheader(f"Hello {her_name}, you light up my world! You're the BEST 💫")
    else:
        st.subheader(f"Hello {her_name}, this Dino doesn't like strangers. Sorry! 😊")

reasons_container = st.container()
with reasons_container:
    num_reasons = st.slider("How many reasons do you want to hear?", 1, 16)

    reasons = [
        "You have the most beautiful smile shorty 😊",
        "You make me laugh even on bad days 😂",
        "You're so intelligent and kind 💡",
        "I admire your passion and strength 💪",
        "You're my fav dno and the love of my life ❤️",
        "Your sense of humor brightens every moment 😆",
        "You're an incredible listener and supporter 🤗",
        "You inspire me to be the best version of myself 🌟",
        "You just ignore me sometimes babes 😜",
        "Your creativity always amazes me 🎨",
        "You have a heart of gold and care deeply for others ❤️",
        "I love how you make every day feel special 🌞",
        "You're adventurous and open to trying new things 🌟",
        "Your confidence is inspiring and attractive 💃",
        "You have a unique and wonderful way of looking at life 🌈",
        "You make even the smallest moments unforgettable 💭"
    ]

    st.write(f"Here are {num_reasons} reasons why I love *YOU* alot:")
    for i in range(num_reasons):
        st.write(f"{i + 1}. {reasons[i]}")

date_container = st.container()
with date_container:
    st.write(f"Today's date is: {datetime.now().strftime('%A, %d %B %Y')}")

surprise_container = st.container()
with surprise_container:
    if st.button("Click for a special message sweetheart.."):
        st.balloons()
        st.success("You're truly amazing, I would love to know if I can make you mine!? Respectfully... 💕")

st.write("Made with ❤️ just for you my dear.")

st.write("")
st.write("")
st.write("")

st.write("I hope you enjoyed this silly app made just for you! 😘")