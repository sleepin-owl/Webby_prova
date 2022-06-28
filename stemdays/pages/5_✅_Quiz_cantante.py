import streamlit as st
import pandas as pd

def quiz():
    with open('statics.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    st.markdown("""
    # Quiz Cantanti :microphone:
    ## Celebrity Trivia
    #### How much do you know about your favorite celebrity?
    ****
    ### *Taylor Swift*
    """)
    
    with st.form("my_form"):
        artistpointslist= {"taylor" : 0, "ed sheeran" : 0, "Maneskin" : 0, "Blackpink" : 0}
        choices1tay = ['Andrea', 'Betty', 'Inez', 'Alison']
        answer1tay = st.radio("Qual è il secondo nome di Taylor?", choices1tay)
        if answer1tay == "Alison":
            artistpointslist["taylor"] += 1
        choices2tay = ["No, non è un'attrice", "Si, in pretty little liars", "Si, in new girl", "No, ma ha partecipato nella realizzazione di una colonna sonora di una serie"]
        answer2tay = st.radio("Ha mai fatto un'apparizione in una serie tv?", choices2tay)
        if answer2tay == "Si, in new girl":
            artistpointslist["taylor"] += 1
        choices3tay = ["Laurea in psicologia", "Si è fermata alle superiori", "Ha studiato come Homeschooler", "Dottorato in belle arti"]
        answer3tay = st.radio("Qual è il suo titolo di studio?", choices3tay)
        if answer3tay == "Dottorato in belle arti":
            artistpointslist["taylor"] += 1
        choices4tay = ["7", "22", "13", "15"]
        answer4tay = st.radio("Qual è il suo numero fortunato?", choices4tay)
        if answer4tay == "13":
            artistpointslist["taylor"] += 1
        choices5tay = ["Sagittario,Cancro,Scorpione", "Aquario,Toro,Vergine", "Pesci,Scorpione,Gemelli", "Sagittario,Ariete,Bilancia"]
        answer5tay = st.radio("Quali sono i suoi big three (sole,luna,ascendente)?", choices5tay)
        if answer5tay == "Sagittario,Cancro,Scorpione":
            artistpointslist["taylor"] += 1
        st.markdown("""
            ### *Ed Sheeran*
            """)
        choices1ed = ["In un bar", "Ad un suo concerto", "Al liceo", "A Tenerife"]
        answer1ed = st.radio("Dove ha conosciuto sua moglie?", choices1ed)
        if answer1ed == "Al liceo":
            artistpointslist["ed sheeran"] += 1
        choices2ed = ["+", ":", "X", "-"]
        answer2ed = st.radio("Come si chiama il suo primo album?", choices2ed)
        if answer2ed == "+":
            artistpointslist["ed sheeran"] += 1
        choices3ed = ["Eddine", "Bimbe di ed", "Sheeranne", "Sheerers"]
        answer3ed = st.radio("Come si chiamano le sue fan?", choices3ed)
        if answer3ed == "Sheerers":
            artistpointslist["ed sheeran"] += 1
        choices4ed = ["+", ":", "X", "-"]
        answer4ed = st.radio("Qual è il segno che non dà il titolo a uno dei suoi album?",choices4ed)
        if answer4ed == "-":
            artistpointslist["ed sheeran"] += 1
        answer5ed = st.text_input("Con chi ha collaborato per scrivere “South of the Border”?")
        if answer5ed == "Camila Cabello" or "Cardi B":
            artistpointslist["ed sheeran"] += 1
        st.markdown("""
                ### *Måneskin*
                """)
        choices1ma = ["Xfactor", "Italia's got talent", "Tù si que vales", "The voice"]
        answer1ma = st.radio("In quale talent show hanno partecipato?", choices1ma)
        if answer1ma == "Xfactor":
            artistpointslist["Maneskin"] += 1
        choices2ma = ["Giorgia Soleri", "Vittorio Sgarbi", "Taylor Swift", "Orietta Berti"]
        answer2ma = st.radio('A chi è dedicata "Coraline"?', choices2ma)
        if answer2ma == "Giorgia Soleri":
            artistpointslist["Maneskin"] += 1
        choices3ma = ["Thomas", "Victoria", "Domiano", "Ethan"]
        answer3ma = st.radio("Come si chiama il/la batterista?", choices3ma)
        if answer3ma == "Ethan":
            artistpointslist["Maneskin"] += 1
        choices4ma = ["Assumere droga", "Plagio", "Diffamazione", "Aggressione"]
        answer4ma = st.radio("Di cosa sono stati accusati all'Eurovision 2021",choices4ma)
        if answer4ma == "Assumere droga":
            artistpointslist["Maneskin"] += 1
        choices5ma = ["Thomas", "Victoria", "Damiano", "Ethan"]
        answer5ma = st.radio("Chi è il più giovane tra i quattro?",choices5ma)
        if answer5ma == "Thomas":
            artistpointslist["Maneskin"] += 1
        st.markdown("""
                    ### *Blackpink*
                    """)
        choices1bp = ["Lisa", "Jennie","Rosè", "Jisoo"]
        answer1bp = st.radio("Qual è stato il primo membro a debuttare come solista?", choices1bp)
        if answer1bp == "Jennie":
            artistpointslist["Blackpink"] += 1
        choices2bp = ["Blackpink everywhere", "Blackpink in your area", "Blackpink in your heart", "Pink is the new Black"]
        answer2bp = st.radio("Qual è il loro slogan?",choices2bp)
        if answer2bp  == "Blackpink in your area":
            artistpointslist["Blackpink"] += 1
        choices3bp = ["Lisa", "Jennie","Rosè", "Jisoo"]
        answer3bp = st.radio("Quale membro ha recitato in un kdrama?", choices3bp)
        if answer3bp == "Jisoo":
            artistpointslist["Blackpink"] += 1
        choices4bp = ["Lisa", "Jennie","Rosè", "Jisoo"]
        answer4bp = st.radio("Chi ha partecipato al met gala 2022?",choices4bp)
        if answer4bp == "Rosè":
            artistpointslist["Blackpink"] += 1
        choices5bp = ["Nokia", "Xiaomi", "Samsung", "Huawei"]
        answer5bp = st.radio("Qual è il loro sponsor?",choices5bp)
        if answer5bp == "Samsung":
            artistpointslist["Blackpink"] += 1
        max_value = max(artistpointslist, key=artistpointslist.get)
        
        submitted = st.form_submit_button("Submit")

        if submitted:
            if max_value == "taylor":
                st.markdown("## Congratulazioni! Conosci di più Taylor Swift")
            elif max_value == "ed sheeran":
                st.markdown("## Congratulazioni! Conosci di più Ed Sheeran")
            elif max_value == "Maneskin":
                st.markdown("## Congratulazioni! Conosci di più i Måneskin")
            elif max_value == "Blackpink":
                st.markdown("## Congratulazioni! Conosci di più le Blackpink")

        key = 'FormSubmitter:my_form-Submit'
       

if __name__ == "__main__":
    quiz()