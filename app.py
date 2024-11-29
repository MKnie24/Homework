import streamlit as st

st.title("Willkommen zum Ratespielchen!")

st.write("Dies ist ein einfaches Ratespiel. Wähle in der Seitenleiste zwischen **Spiel** und **Statistik**.")

st.markdown(
    """
    Dieses Rate Spiel zeigt dir zu Beginn die möglichen erratbaren Tiere.  
    Du kannst dann direkt anfangen, die Tiere zu erraten.  
    Nach jedem Versuch bekommst du Feedback, wo du erfährst, wo dein geratenes Tier mit dem gesuchten übereinstimmt.  
    Solltest du nach einigen Versuchen immer noch nicht vorwärts kommen, wird das Spiel dir weitere Hinweise geben.  
    Hast du das gesuchte Tier erraten, wird dir die Qualität deines Versuchs auf der **Game Stats**-Seite angezeigt.
    """
)

st.write("Viel Spaß beim Spiel!")