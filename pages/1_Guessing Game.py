import streamlit as st
import random

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

# Data for animals
tiere = [
    {"Name": "Löwe", "Art": "Säugetier", "Fell": "Ja", "Nahrung": "Fleisch", "Lebensraum": "offene Landschaft", "Lebensweise": "Gruppentier"},
    {"Name": "Tiger", "Art": "Säugetier", "Fell": "Ja", "Nahrung": "Fleisch", "Lebensraum": "Wälder", "Lebensweise": "Einzelgänger"},
    {"Name": "Bär", "Art": "Säugetier", "Fell": "Ja", "Nahrung": "Allesfresser", "Lebensraum": "Wälder", "Lebensweise": "Einzelgänger"},
    {"Name": "Wolf", "Art": "Säugetier", "Fell": "Ja", "Nahrung": "Fleisch", "Lebensraum": "Wälder", "Lebensweise": "Gruppentier"},
    {"Name": "Panda", "Art": "Säugetier", "Fell": "Ja", "Nahrung": "Pflanzen", "Lebensraum": "Berge", "Lebensweise": "Einzelgänger"},
    {"Name": "Koala", "Art": "Säugetier", "Fell": "Ja", "Nahrung": "Pflanzen", "Lebensraum": "Wälder", "Lebensweise": "Einzelgänger"},
    {"Name": "Elefant", "Art": "Säugetier", "Fell": "Nein", "Nahrung": "Pflanzen", "Lebensraum": "offene Landschaft", "Lebensweise": "Gruppentier"},
    {"Name": "Känguru", "Art": "Säugetier", "Fell": "Ja", "Nahrung": "Pflanzen", "Lebensraum": "Wüste", "Lebensweise": "Gruppentier"},
    {"Name": "Schimpanse", "Art": "Säugetier", "Fell": "Ja", "Nahrung": "Allesfresser", "Lebensraum": "Wälder", "Lebensweise": "Gruppentier"},
    {"Name": "Giraffe", "Art": "Säugetier", "Fell": "Ja", "Nahrung": "Pflanzen", "Lebensraum": "offene Landschaft", "Lebensweise": "Gruppentier"},
    {"Name": "Krokodil", "Art": "Reptil", "Fell": "Nein", "Nahrung": "Fleisch", "Lebensraum": "Gewässer", "Lebensweise": "Einzelgänger"},
    {"Name": "Boa Constrictor", "Art": "Reptil", "Fell": "Nein", "Nahrung": "Fleisch", "Lebensraum": "Wälder", "Lebensweise": "Einzelgänger"},
    {"Name": "Iguana", "Art": "Reptil", "Fell": "Nein", "Nahrung": "Pflanzen", "Lebensraum": "Wälder", "Lebensweise": "Einzelgänger"},
    {"Name": "Schildkröte", "Art": "Reptil", "Fell": "Nein", "Nahrung": "Pflanzen", "Lebensraum": "Gewässer", "Lebensweise": "Einzelgänger"},
    {"Name": "Chamäleon", "Art": "Reptil", "Fell": "Nein", "Nahrung": "Insekten", "Lebensraum": "Wälder", "Lebensweise": "Einzelgänger"},
    {"Name": "Pinguin", "Art": "Vogel", "Fell": "Nein", "Nahrung": "Fleisch", "Lebensraum": "Gewässer", "Lebensweise": "Gruppentier"},
    {"Name": "Adler", "Art": "Vogel", "Fell": "Nein", "Nahrung": "Fleisch", "Lebensraum": "Berge", "Lebensweise": "Einzelgänger"},
    {"Name": "Fuchs", "Art": "Säugetier", "Fell": "Ja", "Nahrung": "Allesfresser", "Lebensraum": "Wälder", "Lebensweise": "Einzelgänger"},
    {"Name": "Albatros", "Art": "Vogel", "Fell": "Nein", "Nahrung": "Fleisch", "Lebensraum": "Gewässer", "Lebensweise": "Wechselnd"},
    {"Name": "Zebra", "Art": "Säugetier", "Fell": "Ja", "Nahrung": "Pflanzen", "Lebensraum": "offene Landschaft", "Lebensweise": "Gruppentier"},
    {"Name": "Kuh", "Art": "Säugetier", "Fell": "Ja", "Nahrung": "Pflanzen", "Lebensraum": "offene Landschaft", "Lebensweise": "Gruppentier"},
    {"Name": "Lama", "Art": "Säugetier", "Fell": "Ja", "Nahrung": "Pflanzen", "Lebensraum": "Berge", "Lebensweise": "Gruppentier"},
    {"Name": "Papagei", "Art": "Vogel", "Fell": "Nein", "Nahrung": "Allesfresser", "Lebensraum": "Wälder", "Lebensweise": "Wechselnd"},
    {"Name": "Eule", "Art": "Vogel", "Fell": "Nein", "Nahrung": "Fleisch", "Lebensraum": "Wälder", "Lebensweise": "Einzelgänger"},
    {"Name": "Kamel", "Art": "Säugetier", "Fell": "Ja", "Nahrung": "Pflanzen", "Lebensraum": "Wüste", "Lebensweise": "Gruppentier"},
    {"Name": "Flamingo", "Art": "Vogel", "Fell": "Nein", "Nahrung": "Pflanzen", "Lebensraum": "Gewässer", "Lebensweise": "Gruppentier"},
    {"Name": "Ostrich", "Art": "Vogel", "Fell": "Nein", "Nahrung": "Allesfresser", "Lebensraum": "offene Landschaft", "Lebensweise": "Wechselnd"},
    {"Name": "Delfin", "Art": "Säugetier", "Fell": "Nein", "Nahrung": "Fleisch", "Lebensraum": "Gewässer", "Lebensweise": "Gruppentier"},
    {"Name": "Gorilla", "Art": "Säugetier", "Fell": "Ja", "Nahrung": "Allesfresser", "Lebensraum": "Wälder", "Lebensweise": "Gruppentier"},
    {"Name": "Pferd", "Art": "Säugetier", "Fell": "Ja", "Nahrung": "Pflanzen", "Lebensraum": "offene Landschaft", "Lebensweise": "Gruppentier"},
    {"Name": "Komodowaran", "Art": "Reptil", "Fell": "Nein", "Nahrung": "Fleisch", "Lebensraum": "Inseln", "Lebensweise": "Einzelgänger"}
]

hilfsliste = {
    "Löwe": {"Größe": "Groß", "Hauptfarbe": "Gold", "Beine": 4},
    "Tiger": {"Größe": "Groß", "Hauptfarbe": "Orange", "Beine": 4},
    "Bär": {"Größe": "Groß", "Hauptfarbe": "Braun", "Beine": 4},
    "Wolf": {"Größe": "Mittel", "Hauptfarbe": "Grau", "Beine": 4},
    "Panda": {"Größe": "Groß", "Hauptfarbe": "Schwarz-Weiß", "Beine": 4},
    "Koala": {"Größe": "Klein", "Hauptfarbe": "Grau", "Beine": 4},
    "Elefant": {"Größe": "Sehr Groß", "Hauptfarbe": "Grau", "Beine": 4},
    "Känguru": {"Größe": "Mittel", "Hauptfarbe": "Braun", "Beine": 2},
    "Schimpanse": {"Größe": "Mittel", "Hauptfarbe": "Schwarz", "Beine": 2},
    "Giraffe": {"Größe": "Sehr Groß", "Hauptfarbe": "Gelb-Braun", "Beine": 4},
    "Krokodil": {"Größe": "Groß", "Hauptfarbe": "Grün", "Beine": 4},
    "Boa Constrictor": {"Größe": "Groß", "Hauptfarbe": "Braun", "Beine": 0},
    "Iguana": {"Größe": "Mittel", "Hauptfarbe": "Grün", "Beine": 4},
    "Schildkröte": {"Größe": "Mittel", "Hauptfarbe": "Grün", "Beine": 4},
    "Chamäleon": {"Größe": "Klein", "Hauptfarbe": "Grün", "Beine": 4},
    "Pinguin": {"Größe": "Mittel", "Hauptfarbe": "Schwarz-Weiß", "Beine": 2},
    "Adler": {"Größe": "Mittel", "Hauptfarbe": "Braun", "Beine": 2},
    "Fuchs": {"Größe": "Mittel", "Hauptfarbe": "Rotbraun", "Beine": 4},
    "Albatros": {"Größe": "Groß", "Hauptfarbe": "Weiß", "Beine": 2},
    "Zebra": {"Größe": "Groß", "Hauptfarbe": "Schwarz-Weiß", "Beine": 4},
    "Kuh": {"Größe": "Groß", "Hauptfarbe": "Braun-Weiß", "Beine": 4},
    "Lama": {"Größe": "Groß", "Hauptfarbe": "Weiß", "Beine": 4},
    "Papagei": {"Größe": "Klein", "Hauptfarbe": "Bunt", "Beine": 2},
    "Eule": {"Größe": "Klein", "Hauptfarbe": "Braun", "Beine": 2},
    "Kamel": {"Größe": "Groß", "Hauptfarbe": "Braun", "Beine": 4},
    "Flamingo": {"Größe": "Groß", "Hauptfarbe": "Pink", "Beine": 2},
    "Ostrich": {"Größe": "Sehr Groß", "Hauptfarbe": "Schwarz-Weiß", "Beine": 2},
    "Delfin": {"Größe": "Groß", "Hauptfarbe": "Grau", "Beine": 0},
    "Gorilla": {"Größe": "Groß", "Hauptfarbe": "Schwarz", "Beine": 2},
    "Pferd": {"Größe": "Groß", "Hauptfarbe": "Braun", "Beine": 4},
    "Komodowaran": {"Größe": "Groß", "Hauptfarbe": "Braun", "Beine": 4}
}
total_matched = 0
hinweis_counter = 0

if "tier_gesucht" not in st.session_state:
    st.session_state.tier_gesucht = random.choice(tiere)
    st.session_state.versuche = 0
    st.session_state.verlauf = []
    st.session_state.verbleibende_tiere = tiere.copy()
    st.session_state.geratene_tiere = []
    st.session_state.stats = {"games": 0, "guesses_per_game": [], "quality_scores": []}
    st.session_state.hinweise = []
    total_matched = 0
    hinweis_counter = 0

set_styles(background_image_url)

tier_gesucht = st.session_state.tier_gesucht
st.title("Ratespielchen")
st.write("Errate das gesuchte Tier in möglichst wenig Runden.")
st.title("Tiere Übersicht - Namen")
columns = st.columns(5)
for idx, tier in enumerate(st.session_state.verbleibende_tiere):
    col = columns[idx % 5]
    with col:
        col.markdown(f"<span class='animal-name'>{tier['Name']}</span>", unsafe_allow_html=True)

eingabe_text = st.text_input("Gib einen Tiernamen ein:")
st.write(f"**Versuche:** {st.session_state.versuche}")

if eingabe_text:
    eingabe_text_lower = eingabe_text.lower()
    tiere_namen_lower = [tier["Name"].lower() for tier in tiere]
    if eingabe_text_lower in tiere_namen_lower:
        if eingabe_text_lower in [tier.lower() for tier in st.session_state.geratene_tiere]:
            st.warning(f"Das Tier '{eingabe_text}' wurde bereits geraten. Versuche ein anderes!")
        else:
            st.session_state.geratene_tiere.append(eingabe_text)
            index = tiere_namen_lower.index(eingabe_text_lower)
            gefundenes_tier = tiere[index]
            st.session_state.versuche += 1
            correct_attributes = 0
            total_attributes = len(tier_gesucht) - 1
            ergebnis = {"Name": gefundenes_tier["Name"], "Merkmale": {}}
            all_attributes_match = True
            for merkmal, wert in gefundenes_tier.items():
                if merkmal != "Name":
                    match = wert == tier_gesucht[merkmal]
                    ergebnis["Merkmale"][merkmal] = (wert, match)
                    if match:
                        correct_attributes += 1
                    else:
                        all_attributes_match = False
            st.session_state.verlauf.insert(0, ergebnis)
            if gefundenes_tier == tier_gesucht:
                st.success(
                    f"Richtig! Du hast das gesuchte Tier '{tier_gesucht['Name']}' in {st.session_state.versuche} Versuchen erraten!"
                )

                total_attributes_per_animal = len(tier_gesucht) - 1
                total_guesses = len(st.session_state.geratene_tiere)

                total_attributes_in_session = total_guesses * total_attributes_per_animal

                if total_attributes_in_session > 0:
                    base_score = (total_matched / total_attributes_in_session) * 100
                else:
                    base_score = 0

                total_attributes_per_animal = len(tier_gesucht) - 1  # Exclude "Name"

                guessed_animals = [
                    next((tier for tier in tiere if tier["Name"].lower() == guessed.lower()), None)
                    for guessed in st.session_state.geratene_tiere
                ]
                guessed_animals = [animal for animal in guessed_animals if animal is not None]

                total_matched = sum(
                    sum(1 for k, v in tier_gesucht.items() if k != "Name" and animal.get(k) == v)
                    for animal in guessed_animals
                )

                if total_attributes_in_session > 0:
                    base_score = (total_matched / total_attributes_in_session) * 100
                else:
                    base_score = 0

                if guessed_animals:
                    closest_match_attributes = max(
                        sum(1 for k, v in tier_gesucht.items() if k != "Name" and animal.get(k) == v)
                        for animal in guessed_animals
                        if animal["Name"] != tier_gesucht["Name"]  # Exclude correct guess
                    )
                else:
                    closest_match_attributes = 0

                if total_attributes_per_animal > 0:
                    closeness_score = max(0, (
                                total_attributes_per_animal - closest_match_attributes) / total_attributes_per_animal * 10)
                else:
                    closeness_score = 0


                hints_penalty = len(st.session_state.hinweise) * 5

                if st.session_state.versuche == 1:
                    quality_score = 100
                elif st.session_state.versuche == 2:
                    quality_score = 99
                else:
                    quality_score = max(0,
                                base_score - hints_penalty + closeness_score)

                st.session_state.stats["games"] += 1
                st.session_state.stats["guesses_per_game"].append(st.session_state.versuche)
                st.session_state.stats["quality_scores"].append(quality_score)

                st.session_state.tier_gesucht = random.choice(tiere)
                st.session_state.versuche = 0
                st.session_state.verlauf = []
                st.session_state.hinweise = []
                st.session_state.geratene_tiere = []
                total_matched = 0
                hinweis_counter = 0
                st.info("Das Spiel wurde automatisch neu gestartet! Rate erneut.")
            else:
                if all_attributes_match:
                    st.warning("Die Merkmale stimmen überein, aber das gesuchte Tier wurde noch nicht gefunden!")
                else:
                    st.info("Falsch geraten. Versuche es erneut!")
    else:
        st.warning("Dieses Tier existiert nicht in der Liste.")

if st.session_state.versuche >= 6:
    tier_name = st.session_state.tier_gesucht["Name"]
    tier_hinweise = hilfsliste.get(tier_name, {})
    if st.session_state.versuche >= 6 and len(st.session_state.hinweise) < 1:
        st.session_state.hinweise.append(f"Größe: **{tier_hinweise.get('Größe', 'unbekannt')}**")
    if st.session_state.versuche >= 8 and len(st.session_state.hinweise) < 2:
        st.session_state.hinweise.append(f"Hauptfarbe: **{tier_hinweise.get('Hauptfarbe', 'unbekannt')}**")
    if st.session_state.versuche >= 10 and len(st.session_state.hinweise) < 3:
        st.session_state.hinweise.append(f"Beine: **{tier_hinweise.get('Beine', 'unbekannt')}**")
    st.write("### Hinweise:")
    hints_str = "&nbsp;&nbsp;&nbsp;".join(st.session_state.hinweise)
    st.markdown(f"<span style='color: black;'>{hints_str}</span>", unsafe_allow_html=True)

st.write("### Verlauf:")
for eintrag in st.session_state.verlauf:
    attributes = [
        f"<b>{merkmal}</b>: <b><span style='color: {'green' if stimmt else 'red'};'>{wert}</span></b>"
        for merkmal, (wert, stimmt) in eintrag["Merkmale"].items()
    ]
    attributes_str = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;".join(attributes)
    st.markdown(f"<span style='color: black; font-weight: bold;'>{eintrag['Name']}</span>&nbsp;&nbsp; {attributes_str}", unsafe_allow_html=True)