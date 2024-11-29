import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# URL of the background image (choose something relaxing!)
background_image_url = (
    "https://external-preview.redd.it/sodaIMFrnWuB5EZe-_xW6uOls9AXbGi6GBpPqIPf6xM.jpg"
    "?width=1080&crop=smart&auto=webp&s=d5a47ba6e939bd6c79a094129e712220c364188c"
)

# Function to set styles for the app (adds background image and text color)
def set_styles(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            color: #C9C9C9; /* Light gray text for readability */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Apply background image
set_styles(background_image_url)

# Initialize session state for statistics
if "stats" not in st.session_state:
    st.session_state.stats = {"games": 0, "guesses_per_game": [], "quality_scores": []}

# App title
st.title("Spielstatistik")

# Explanation of quality scoring
st.markdown("""
### Wie wird die Qualität bewertet?
Die **Qualitätsbewertung** gibt an, wie effizient du das Spiel gelöst hast.

- **Maximal 100%**: Errate das richtige Tier im ersten Versuch.
- **Weniger Punkte für mehr Versuche**: Je mehr Versuche benötigt werden, desto niedriger die Punktzahl.
- **Hinweise reduzieren die Punktzahl**: Jeder Hinweis reduziert die Punktzahl um **5%**.
- **Bonus für gute Vermutungen**: Je besser deine Vermutungen die Merkmale des gesuchten Tieres treffen, desto größer wird der Bonus.
""", unsafe_allow_html=True)

# Display number of games played
games_played = st.session_state.stats["games"]
st.write(f"**Anzahl der gespielten Spiele:** {games_played}")

# If games have been played, show detailed stats
if games_played > 0:
    # Calculate average guesses per game
    total_guesses = sum(st.session_state.stats["guesses_per_game"])
    avg_guesses = total_guesses / games_played
    st.write(f"**Durchschnittliche Anzahl der Versuche pro Spiel:** {avg_guesses:.2f}")

    # Create a DataFrame for detailed statistics
    df = pd.DataFrame({
        "Spiel": range(1, games_played + 1),
        "Versuche": st.session_state.stats["guesses_per_game"],
        "Qualität (%)": [f"{q:.1f}" for q in st.session_state.stats["quality_scores"]]
    })

    # Plot attempts vs. quality score
    st.write("### Versuche und Qualitätsbewertungen pro Spiel:")
    fig, ax = plt.subplots()
    ax.bar(df["Spiel"], df["Versuche"], label="Versuche", color="#4A90E2")  # Softer blue
    ax.set_xlabel("Spiel")
    ax.set_ylabel("Anzahl der Versuche")
    ax.set_title("Versuche und Qualitätsbewertungen pro Spiel")
    ax.set_xticks(df["Spiel"])
    ax.set_xticklabels(df["Spiel"])
    ax.legend()
    st.pyplot(fig)

    # Show quality scores in a table
    st.write("### Qualitätsbewertung:")
    st.dataframe(df[["Spiel", "Qualität (%)"]], height=150)

else:
    # No data to display
    st.info("Noch keine Daten verfügbar. Spiele ein Spiel, um Statistiken zu sehen!")

# Option to reset statistics
st.write("### Statistiken zurücksetzen")
confirm_reset = st.checkbox("Ich möchte die Statistiken zurücksetzen.")

# Provide feedback for reset action
if confirm_reset:
    if st.button("Statistiken zurücksetzen"):
        st.session_state.stats = {"games": 0, "guesses_per_game": [], "quality_scores": []}
        st.success("Statistiken wurden erfolgreich zurückgesetzt.")
    else:
        st.warning("Klicke auf die Schaltfläche, um den Vorgang abzuschließen.")
