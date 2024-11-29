import streamlit as st # streamlit libary
import random # Python module for random values

background_image_url = "https://img2.wallspic.com/crops/6/6/5/3/4/143566/143566-sonnenuntergang-naturlandschaft-horizont-morgen-hirsch-2560x1440.jpg" # Set Background

def set_styles(image_url): # Applies custom CSS style to Streamlit app (background image, text style)
    st.markdown(
        f""" 
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            color: black;  
        }}
        .animal-name {{
            color: black; 
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
    {"Name": "Strauß", "Art": "Vogel", "Fell": "Nein", "Nahrung": "Allesfresser", "Lebensraum": "offene Landschaft", "Lebensweise": "Wechselnd"},
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
    "Strauß": {"Größe": "Sehr Groß", "Hauptfarbe": "Schwarz-Weiß", "Beine": 2},
    "Delfin": {"Größe": "Groß", "Hauptfarbe": "Grau", "Beine": 0},
    "Gorilla": {"Größe": "Groß", "Hauptfarbe": "Schwarz", "Beine": 2},
    "Pferd": {"Größe": "Groß", "Hauptfarbe": "Braun", "Beine": 4},
    "Komodowaran": {"Größe": "Groß", "Hauptfarbe": "Braun", "Beine": 4}
}

if "tier_gesucht" not in st.session_state: # Initializes st.session_state with default values
    st.session_state.tier_gesucht = random.choice(tiere) # Chooses a random animal for the list
    st.session_state.versuche = 0 # Counter for number of guesses
    st.session_state.verlauf = [] # Tracks the previous results
    st.session_state.verbleibende_tiere = tiere.copy() # List of animals that have not been guessed
    st.session_state.geratene_tiere = [] # List of animals guessed
    st.session_state.stats = {"games": 0, "guesses_per_game": [], "quality_scores": []} # Tracks game stats
    st.session_state.hinweise = [] # Tracks amount of hints

set_styles(background_image_url)

tier_gesucht = st.session_state.tier_gesucht
st.title("Ratespielchen")
st.write("Errate das gesuchte Tier in möglichst wenig Runden.")
st.title("Tiere Übersicht - Namen")
columns = st.columns(5) # Arranges the anmial and its attributes in a table of 5 columns
for idx, tier in enumerate(st.session_state.verbleibende_tiere): # Goes through each remaining animal in the list ( idx is the position in the list and "tier" is the information of the animal)
    col = columns[idx % 5] # Determines in which column the animal gets placed (cycling through the 5 columns using modulo)
    with col: # Ensures that the following content is inside the selected column
        col.markdown(f"<span class='animal-name'>{tier['Name']}</span>", unsafe_allow_html=True) # Displays the name of the current animal in the selected column, uses raw HTML

eingabe_text = st.text_input("Gib einen Tiernamen ein:") # User input for animal game
st.write(f"**Versuche:** {st.session_state.versuche}") # Displays number of guesses

if eingabe_text:
    eingabe_text_lower = eingabe_text.lower() # Converts the input to lowercase letters
    tiere_namen_lower = [tier["Name"].lower() for tier in tiere] # Creates a lowercase list of all animal names
    if eingabe_text_lower in tiere_namen_lower: # Confirms that the input matches one animal on the list
        if eingabe_text_lower in [tier.lower() for tier in st.session_state.geratene_tiere]: # Checks if the animal has been guessed already
            st.warning(f"Das Tier '{eingabe_text}' wurde bereits geraten. Versuche ein anderes!") # Displays a warning if that happens
        else:
            st.session_state.geratene_tiere.append(eingabe_text) # Adds guessed animals to the list of guessed animals
            index = tiere_namen_lower.index(eingabe_text_lower) # Retrieves the full details of the guessed animals and increments the guess counter
            gefundenes_tier = tiere[index]
            st.session_state.versuche += 1
            richtige_merkmale = 0 # Compares each attribute (not name) of the guessed animal with the target animal
            ergebnis = {"Name": gefundenes_tier["Name"], "Merkmale": {}}
            alle_merkmale_match = True
            for merkmal, wert in gefundenes_tier.items():
                if merkmal != "Name":
                    match = wert == tier_gesucht[merkmal]
                    ergebnis["Merkmale"][merkmal] = (wert, match)
                    if match:
                        richtige_merkmale += 1
                    else:
                        alle_merkmale_match = False
            st.session_state.verlauf.insert(0, ergebnis)
            if gefundenes_tier == tier_gesucht: # Displays a message if the guessed animal is the right/target animal
                st.success(
                    f"Richtig! Du hast das gesuchte Tier '{tier_gesucht['Name']}' in {st.session_state.versuche} Versuchen erraten!"
                )

                merkmale_pro_tier = len(tier_gesucht) - 1 # Calculates the total number of attributes (excluding Name) to determine the match score
                gesamte_versuche = len(st.session_state.geratene_tiere)

                gesamte_merkmale_session = gesamte_versuche * merkmale_pro_tier # Gets the total number of animals guessed so far in current game

                tiere_geraten = [ #matches the animal name to entry from the main list
                    next((tier for tier in tiere if tier["Name"].lower() == guessed.lower()), None) #retrieves the match
                    for guessed in st.session_state.geratene_tiere
                ]
                tiere_geraten = [animal for animal in tiere_geraten if animal is not None]

                gesamt_matches = sum( #sums together all attributes that match the wanted animals ones
                    sum(1 for k, v in tier_gesucht.items() if k != "Name" and animal.get(k) == v)
                    for animal in tiere_geraten
                )

                if gesamte_merkmale_session > 0: #if there are attributes in the session they are estimated by the correspondance to gesamt_matches
                    base_quali = (gesamt_matches / gesamte_merkmale_session) * 100
                else:
                    base_quali = 0

                if tiere_geraten: #identifying the animal with is closest matched to the wanted animal
                    merkmale_am_ehesten = max(
                        sum(1 for k, v in tier_gesucht.items() if k != "Name" and tier_1.get(k) == v)
                        for tier_1 in tiere_geraten
                        if tier_1["Name"] != tier_gesucht["Name"]  #exclude correct guess
                    )
                else:
                    merkmale_am_ehesten = 0

                if merkmale_pro_tier > 0: #computing how close the best guess to the wanted animal was. the futher away the better the bonus
                    guter_versuch = max(0, (
                            merkmale_pro_tier - merkmale_am_ehesten) / merkmale_pro_tier * 10)
                else:
                    guter_versuch = 0


                strafe_hinweis = len(st.session_state.hinweise) * 5 #applies a penelty of 5% if a hint is being displayed

                if st.session_state.versuche == 1: #first try guess = 100% quality
                    quality = 100
                elif st.session_state.versuche == 2: #second try guess 99% quality (first try is better but still very good guality for us)
                    quality = 99
                else:
                    quality = max(0, base_quali - strafe_hinweis + guter_versuch) #computes the quality the normal way

                #updates the game stats
                st.session_state.stats["games"] += 1
                st.session_state.stats["guesses_per_game"].append(st.session_state.versuche)
                st.session_state.stats["quality_scores"].append(quality)

                #resets the game stats for the next session
                st.session_state.tier_gesucht = random.choice(tiere)
                st.session_state.versuche = 0
                st.session_state.verlauf = []
                st.session_state.hinweise = []
                st.session_state.geratene_tiere = []
                gesamt_matches = 0
                hinweis_counter = 0
                st.info("Das Spiel wurde automatisch neu gestartet! Rate erneut.") #information that one can start guessing again
            else:
                if alle_merkmale_match: #failsafe so there is no confusion if the attributes match
                    st.warning("Die Merkmale stimmen überein, aber das gesuchte Tier wurde noch nicht gefunden!")
                else:
                    st.info("Falsch geraten. Versuche es erneut!") #wrong guess
    else:
        st.warning("Dieses Tier existiert nicht in der Liste.") #an input not in sync with the list

if st.session_state.versuche >= 6: # If the user has made 6 or more guesses, retrieve 'tier_name' (target animal name) and its hints from 'hilfsliste' dictionary
    tier_name = st.session_state.tier_gesucht["Name"]
    tier_hinweise = hilfsliste.get(tier_name, {}) # If the target animal is not found in 'hilfsliste' an empty dicitionary gets returned
    if st.session_state.versuche >= 6 and len(st.session_state.hinweise) < 1: # If after 6 guesses not hints have been given, add the 'size' attribute of the target animal to the hints
        st.session_state.hinweise.append(f"Größe: **{tier_hinweise.get('Größe', 'unbekannt')}**")
    if st.session_state.versuche >= 8 and len(st.session_state.hinweise) < 2: # If after 8 guesses less than 2 hints have been given, add the 'main color' attribute of the target animal to the hints
        st.session_state.hinweise.append(f"Hauptfarbe: **{tier_hinweise.get('Hauptfarbe', 'unbekannt')}**")
    if st.session_state.versuche >= 10 and len(st.session_state.hinweise) < 3: # If after 10 guesses less than 3 hints have been given, add the 'number of legs' attribute of the target animal to hints
        st.session_state.hinweise.append(f"Beine: **{tier_hinweise.get('Beine', 'unbekannt')}**")
    st.write("### Hinweise:") # Display all collected hints under " ### Hinweise:" (Hints), the hints are displayed with spaces and a custom style
    hints_str = "&nbsp;&nbsp;&nbsp;".join(st.session_state.hinweise)
    st.markdown(f"<span style='color: black;'>{hints_str}</span>", unsafe_allow_html=True)

st.write("### Verlauf:") # Adds a heading for the guess history
for eintrag in st.session_state.verlauf: # Loops through each entry ('eintrag') in the guess history ('verlauf'). For each entry a formatted string is created that inhibits the attribute ('merkmal') of the guessed animal
    merkmale = [ # Matching attributes are displayed green and not matching attributes are displayed red
        f"<b>{merkmal}</b>: <b><span style='color: {'green' if stimmt else 'red'};'>{wert}</span></b>"
        for merkmal, (wert, stimmt) in eintrag["Merkmale"].items()
    ]
    merkmale_str = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;".join(merkmale) #Puts a space between formatted attributes for readability and alignment
    st.markdown(f"<span style='color: black; font-weight: bold;'>{eintrag['Name']}</span>&nbsp;&nbsp; {merkmale_str}", unsafe_allow_html=True) # Displays the name of the guesses animal, followed by its attributes in green or red(color explained above)