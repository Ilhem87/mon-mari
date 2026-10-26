import os
from datetime import date
import streamlit as st

st.set_page_config(
    page_title="Joyeux Anniversaire à l'homme de ma vie, SAMI ❤️",
    page_icon="🎂",
    layout="wide"
)

# ---------- Style ----------
hearts = "".join(
    f"<span class='fh' style='left:{l}%;animation-duration:{d}s;animation-delay:{dl}s;font-size:{s}px'>{e}</span>"
    for l, d, dl, s, e in [
        (5, 12, 0, 22, "❤️"), (15, 15, 3, 16, "💖"), (27, 11, 6, 26, "❤️"),
        (38, 14, 1, 18, "💕"), (50, 13, 4, 24, "❤️"), (62, 16, 2, 20, "💖"),
        (73, 12, 7, 16, "💕"), (84, 15, 5, 26, "❤️"), (93, 13, 8, 20, "💖"),
    ]
)

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Dancing+Script:wght@600;700&display=swap');

html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }

.stApp {
    background: linear-gradient(135deg, #1b1035 0%, #3a1c5a 45%, #7a2a5e 100%);
    background-attachment: fixed;
    color: #ffffff;
}
header[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }
.block-container { padding-top: 1.5rem; max-width: 1100px; }

/* Cœurs flottants */
.fh { position: fixed; bottom: -40px; opacity: 0; z-index: 0; pointer-events: none;
      animation-name: floatup; animation-iteration-count: infinite; animation-timing-function: linear; }
@keyframes floatup {
    0%   { transform: translateY(0) rotate(0deg); opacity: 0; }
    10%  { opacity: .7; }
    90%  { opacity: .5; }
    100% { transform: translateY(-110vh) rotate(25deg); opacity: 0; }
}

.hero { text-align: center; padding: 1.5rem 1rem .5rem 1rem; position: relative; z-index: 1; }
.hero h1 {
    font-family: 'Dancing Script', cursive; font-size: 4rem; font-weight: 700; margin: 0;
    background: linear-gradient(90deg, #ff9a9e, #fad0c4, #ffd86f);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.hero p { color: #e6d9f5; font-size: 1.1rem; margin-top: .2rem; }

.card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 20px; padding: 1.4rem 1.6rem;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
    position: relative; z-index: 1;
}
.card h3 { margin-top: 0; font-weight: 600; color: #ffd6e0; }
.card p { color: #f1e8fb; line-height: 1.8; }

.kpi { text-align: center; }
.kpi .num { font-size: 2.3rem; font-weight: 700; color: #ffd86f; line-height: 1.1; }
.kpi .lbl { font-size: .9rem; color: #e6d9f5; margin-top: .3rem; }

.timeline-item { display: flex; gap: 1rem; margin-bottom: 1.3rem; }
.dot { min-width: 14px; height: 14px; border-radius: 50%; background: #ff6b8b; margin-top: .45rem;
       box-shadow: 0 0 0 5px rgba(255,107,139,0.25); }
.timeline-item .date { font-weight: 600; color: #ffd86f; }
.timeline-item .txt { color: #f1e8fb; }

.wish { text-align: center; padding: 1.2rem .6rem; background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.14); border-radius: 18px; transition: transform .2s; }
.wish:hover { transform: translateY(-6px); background: rgba(255,255,255,0.13); }
.wish .ico { font-size: 2rem; }
.wish .t { font-weight: 500; margin-top: .3rem; }

.letter {
    font-family: 'Dancing Script', cursive; font-size: 1.7rem; line-height: 1.7;
    color: #fff0f5; background: rgba(255,255,255,0.06);
    border-left: 4px solid #ff6b8b; border-radius: 16px; padding: 1.6rem 2rem;
    position: relative; z-index: 1;
}
.letter .sig { text-align: right; color: #ffd86f; margin-top: 1rem; }

.final { text-align: center; margin: 1.5rem 0; font-family: 'Dancing Script', cursive;
         font-size: 2.6rem; font-weight: 700; color: #ffb3c6; position: relative; z-index: 1; }
.final small { display: block; font-family: 'Poppins', sans-serif; font-size: 1rem;
               color: #e6d9f5; font-weight: 400; margin-top: .4rem; }

div.stButton > button {
    background: linear-gradient(90deg, #ff6b8b, #ff9a5a); color: white; border: none;
    border-radius: 999px; padding: .75rem 1.5rem; font-weight: 600; font-size: 1.05rem;
    box-shadow: 0 6px 20px rgba(255,107,139,0.4);
}
div.stButton > button:hover { transform: translateY(-2px); color: white; }

button[data-baseweb="tab"] { font-size: 1.05rem; color: #e6d9f5; }
button[data-baseweb="tab"][aria-selected="true"] { color: #ffb3c6; }
div[data-testid="stExpander"] { background: rgba(255,255,255,0.07); border-radius: 14px;
                                border: 1px solid rgba(255,255,255,0.14); }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)
st.markdown(hearts, unsafe_allow_html=True)

# ---------- Données ----------
today = date.today()
rencontre = date(2022, 12, 14)
mariage = date(2023, 5, 26)
jours_rencontre = (today - rencontre).days
jours_mariage = (today - mariage).days
annees = round(jours_rencontre / 365.25, 1)
heures = jours_rencontre * 24


def fmt(n):
    return f"{n:,}".replace(",", " ")


# ---------- En-tête ----------
st.markdown(
    "<div class='hero'><h1>Joyeux Anniversaire<br>à l'homme de ma vie, SAMI 🎂</h1>"
    "<p>Une journée spéciale pour la personne la plus spéciale ❤️</p></div>",
    unsafe_allow_html=True
)

# Musique (optionnelle) : mets un fichier musique.mp3 à côté de app.py
if os.path.exists("musique.mp3"):
    st.audio("musique.mp3", loop=True)

tab1, tab2, tab3, tab4 = st.tabs(
    ["🏠 Accueil", "✨ Notre histoire", "💌 Ma lettre", "🎁 Surprise"]
)

# ---------- Accueil ----------
with tab1:
    k1, k2, k3, k4 = st.columns(4)
    kpis = [
        (fmt(jours_rencontre), "jours depuis notre rencontre"),
        (fmt(jours_mariage), "jours depuis notre contrat de mariage"),
        (str(annees), "années d'amour"),
        (fmt(heures), "heures avec toi"),
    ]
    for col, (num, lbl) in zip((k1, k2, k3, k4), kpis):
        with col:
            st.markdown(
                f"<div class='card kpi'><div class='num'>{num}</div><div class='lbl'>{lbl}</div></div>",
                unsafe_allow_html=True
            )

    st.write("")
    if True:
        st.markdown(
            "<div class='card'><h3>💌 À mon cher Sami</h3>"
            "<p>Aujourd'hui est un jour très spécial, car nous célébrons ton anniversaire.</p>"
            "<p>Merci pour ton amour, ta patience, ton soutien et tous les magnifiques "
            "moments que nous partageons. Chaque jour passé à tes côtés est un cadeau précieux.</p>"
            "<p>Que tous tes rêves se réalisent et que notre bonheur continue de grandir chaque jour.</p>"
            "</div>",
            unsafe_allow_html=True
        )

    st.write("")
    st.markdown("### 🎁 Mes vœux pour toi")
    voeux = [
        ("❤️", "Beaucoup d'amour"),
        ("😊", "Beaucoup de bonheur"),
        ("🌟", "Beaucoup de réussite"),
        ("💪", "Une excellente santé"),
        ("🎉", "Une année de belles surprises"),
    ]
    for col, (ico, txt) in zip(st.columns(len(voeux)), voeux):
        with col:
            st.markdown(
                f"<div class='wish'><div class='ico'>{ico}</div><div class='t'>{txt}</div></div>",
                unsafe_allow_html=True
            )

# ---------- Notre histoire ----------
with tab2:
    st.markdown(
        "<div class='card'><h3>✨ Notre histoire</h3>"
        "<div class='timeline-item'><div class='dot'></div><div>"
        "<div class='date'>14 décembre 2022</div>"
        "<div class='txt'>Le jour de notre première rencontre. Ma vie a pris une nouvelle direction "
        "et c'est le début de notre belle histoire.</div></div></div>"
        "<div class='timeline-item'><div class='dot'></div><div>"
        "<div class='date'>22 mars 2023</div>"
        "<div class='txt'>Nos fiançailles : le jour où nous nous sommes promis "
        "de nous choisir pour la vie.</div></div></div>"
        "<div class='timeline-item'><div class='dot'></div><div>"
        "<div class='date'>26 mai 2023</div>"
        "<div class='txt'>Le plus beau jour de ma vie : la signature de notre contrat de mariage "
        "et la décision de construire notre avenir ensemble.</div></div></div>"
        "<div class='timeline-item'><div class='dot'></div><div>"
        "<div class='date'>4 février 2024</div>"
        "<div class='txt'>Notre mariage : le jour où nous avons célébré notre amour "
        "devant nos proches.</div></div></div>"
        "<div class='timeline-item'><div class='dot'></div><div>"
        "<div class='date'>Aujourd'hui</div>"
        "<div class='txt'>Et ce n'est que le début de nos plus beaux souvenirs.</div></div></div>"
        "</div>",
        unsafe_allow_html=True
    )
    st.write("")
    st.markdown("### 💖 Les raisons pour lesquelles je t'aime")
    st.caption("Clique sur chaque carte pour la découvrir")
    # Modifie ces phrases pour les rendre encore plus personnelles
    raisons = [
        ("Ton sourire", "Il illumine mes journées, même les plus grises."),
        ("Ta patience", "Tu sais toujours rester calme et m'écouter."),
        ("Ton soutien", "Tu crois en moi même quand je doute."),
        ("Ton cœur", "Tu es la personne la plus généreuse que je connaisse."),
        ("Nous deux", "Avec toi, tout devient plus simple et plus beau."),
    ]
    for titre, texte in raisons:
        with st.expander(f"❤️ {titre}"):
            st.write(texte)

# ---------- Lettre ----------
with tab3:
    st.markdown(
        "<div class='letter'>"
        "Mon cher Sami,<br><br>"
        "Depuis le 14 décembre 2022, ma vie n'est plus la même. "
        "Le 26 mai 2023, nous avons choisi de construire notre avenir ensemble, "
        "et c'est le plus beau choix que j'aie fait.<br><br>"
        "Merci d'être à mes côtés, aujourd'hui et chaque jour.<br><br>"
        "Je t'aime aujourd'hui, demain et pour toujours."
        "<div class='sig'>Ta femme qui t'aime ❤️</div>"
        "</div>",
        unsafe_allow_html=True
    )

# ---------- Surprise ----------
with tab4:
    st.write("")
    b1, b2, b3 = st.columns([1, 1, 1])
    with b2:
        ouvrir = st.button("🎁 Ouvrir ma surprise", use_container_width=True)
    if ouvrir:
        st.balloons()
        st.markdown(
            "<div class='final'>Joyeux Anniversaire Mon Amour ❤️"
            "<small>Je t'aime aujourd'hui, demain et pour toujours.</small></div>",
            unsafe_allow_html=True
        )
        st.markdown("<div class='final' style='font-size:1.6rem'>🎶 Une chanson pour toi</div>", unsafe_allow_html=True)
        v1, v2, v3 = st.columns([1, 2, 1])
        with v2:
            st.video("https://www.youtube.com/watch?v=futLvLgEPvw")
            st.link_button(
                "▶️ Écouter sur YouTube",
                "https://www.youtube.com/watch?v=futLvLgEPvw",
                use_container_width=True
            )
        if os.path.exists("video.mp4"):
            st.video("video.mp4")
