import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")



def presentation():
    with open('statics.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st_search, buzz1, st_analitycs, buzz2,  st_quiz= st.columns([10,1,10,1,10])

    with st_search:
        st.markdown("<h1 streamlit run class='title';'> Search 🔍</h1>", unsafe_allow_html=True)
        st.markdown("<p class='site-description';>Ricerca i tuoi brani preferiti. Una volta scelta la canzone, il testo e il suo video su YouTube sarà a tua disposizione per cantarla a squarciagola e dare sfogo alle tue emozioni</p>", unsafe_allow_html=True)

    with st_analitycs:
    
        st.markdown("<h1 class='title';'> Analytics 📊</h1>", unsafe_allow_html=True)
        st.markdown("<p class='site-description';'>Statistiche, paragoni e approfondimenti sulle canzoni più belle del nostro database. Divertiti a confrontarle e scopri di più su tutte loro!</p>", unsafe_allow_html=True)


    with st_quiz:
        st.markdown("<h1 class='title';'> Quiz ✅</h1>", unsafe_allow_html=True)
        st.markdown("<p class='site-description';'>A meno che tu non sia un alieno malvagio, anche a tu fai i quiz per sapere che verdura sei (ammettilo), quindi perché non dai un'occhiata ai nostri?</p>", unsafe_allow_html=True)


def main ():
    st.title('Welcome! 👋')
    st.markdown("<p class='welcome-caption';'> Benvenutə su Rhythmized, il miglior sito - così dicono -, per analizzare la musica in maniera intelligente! La sua realizzazione è stata possibile all'interno dell'iniziativa StemDays 2022. </p>", unsafe_allow_html=True)
    st.markdown('**** ****')
    st.header('*Il nostro progetto e il team (migliore)*')
    with st.container():
        st.markdown("<p class='intro-par';'> A cosa serviamo? Non a molto, in realtà, ma siamo simpatiche. Il nostro sito ti permette di trovare le tue canzoni preferite e ascoltarle, confrontarle e conoscerle più a fondo. Se sei unə d'altri tempi e suoni uno o più strumenti, troverai gli spartiti per i brani classici che ti piacciono di più. Non sai quale sia il genere che fa per te o la canzone che rispecchia il tuo mood giornaliero? Divertiti con i nostri quiz e scopri nuovi capolavori. E se vuoi conoscerci meglio (te lo sconsigliamo), visita la sezione about us. Troverai una playlist con i brani che ci rappresentano!</p>", unsafe_allow_html=True)
    
    presentation()
    

def dataframe():
    url = "https://raw.githubusercontent.com/AleCioc/STEMdays/master/10k_random_tracks.csv"
    tracks_data = pd.read_csv(url)
    
if __name__ == '__main__':
    main()
