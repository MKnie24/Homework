import streamlit as st

background_image_url = "https://img2.wallspic.com/crops/6/6/5/3/4/143566/143566-sonnenuntergang-naturlandschaft-horizont-morgen-hirsch-2560x1440.jpg"

def set_styles(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            color: black;  /* Set default text color to black */
        }}
        .animal-name {{
            color: black;  /* Change the color of the names list */
            font-weight: bold;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.title("Willkommen zum Ratespielchen!")
st.write(
    "Dies ist ein einfaches Ratespiel. Wähle in der Seitenleiste zwischen **Spiel** und **Statistik**."
)
st.write("Viel Spaß!")