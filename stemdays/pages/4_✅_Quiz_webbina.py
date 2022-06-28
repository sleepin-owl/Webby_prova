import streamlit as st
import pandas as pd

root_path = "/Users/marianna/vscode/stemdays/img_quiz"

imagelist = ["claraimage.jpeg", 'beatriceimage.jpeg', 'giorgiaimage.jpeg', 'kikimage.jpeg', 'paolaimage.jpeg', 'jessicaimage.jpeg', 'mariannaimage.jpeg', 'silviaimage.jpeg']


def visualizza_immagini(lista_di_immagini):

    st_cols = st.columns(4)

    for index, path in enumerate(lista_di_immagini):
        with open(f"{root_path}/{path}", "rb") as photo:
            if index in [0, 4]:
                st_cols[0].image(photo.read(), caption=index + 1)
            elif index in [1, 5]:
                st_cols[1].image(photo.read(), caption=index + 1)
            elif index in [2, 6]:
                st_cols[2].image(photo.read(), caption=index + 1)
            else:
                st_cols[3].image(photo.read(), caption=index + 1)

def quiz():
    st.set_page_config(layout="wide")
    st.markdown("""
    # Quiz Stemmina ✅
    ## Find me a webbie
    #### Which member do you resemble the most? Come find out with our "oddly" specific quiz!"
    ****
    """)
    
    with st.form("my_form"):
        choices1 = ['Guardare serie tv', 'Farmi film mentali da oscar', 'Disegnare', 'Suonare', 'Leggere', 'Giocare ai videogiochi', 'Riguardare Star Wars', 'Progettare']
        answer1 = st.radio("Cosa ti piace fare nel tempo libero?", choices1)
        paolapoints = 0
        mariannapoints = 0
        jessicapoints = 0
        beatricepoints = 0
        clarapoints = 0
        kikpoints = 0
        silviapoints = 0
        giorgiapoints = 0
        if answer1 == 'Guardare serie tv':
            jessicapoints += 1
            print("You selected " + answer1)
        elif answer1 == 'Farmi film mentali da oscar':
            beatricepoints += 1
            print("You selected " + answer1)
        elif answer1 == 'Disegnare':
            clarapoints += 1
            print("You selected " + answer1)
        elif answer1 == 'Suonare':
            paolapoints += 1
            print("You selected " + answer1)
        elif answer1 == 'Leggere':
            mariannapoints += 1
            print("You selected " + answer1)
        elif answer1 == 'Giocare ai videogiochi':
            kikpoints += 1
            print("You selected " + answer1)
        elif answer1 == 'Riguardare Star Wars':
            silviapoints += 1
            print("You selected " + answer1)
        else: giorgiapoints += 1
        choices2 = ['inglese','spagnolo','giapponese','francese','lettone','napoletano','coreano','italiano']
        answer2 = st.radio("Quali tra le seguenti lingue preferisci?",choices2)
        if answer2 == 'inglese':
            silviapoints += 1
        elif answer2 == 'spagnolo':
            jessicapoints += 1
        elif answer2 == 'giapponese':
            beatricepoints += 1
        elif answer2 == 'francese':
            giorgiapoints += 1
        elif answer2 == 'lettone':
            kikpoints += 1
        elif answer2 == 'napoletano':
            paolapoints += 1
        elif answer2 == 'coreano':
            clarapoints += 1
        else:
            mariannapoints += 1
        choices3 = ["A presentare la mia mostra d'arte", "Ad Hollywood", "In mezzo ai boschi a vagare", "A casa di Taylor a scrivere canzoni con lei", "Al MIT a fare dottorato", "Con una magistrale in psicologia", "A lavorare alla Nasa", "Con una mia azienda"]
        answer3 = st.radio("Come e/o dove ti vedi tra 10 anni?", choices3)
        if answer3 == "A presentare la mia mostra d'arte":
            clarapoints += 1
        elif answer3 == "Ad Hollywood":
            jessicapoints += 1
        elif answer3 == "In mezzo ai boschi a vagare":
            beatricepoints += 1
        elif answer3 == "A casa di Taylor a scrivere canzoni con lei":
            paolapoints += 1
        elif answer3 == "Al MIT a fare dottorato":
            mariannapoints += 1
        elif answer3 == 'Con una magistrale in psicologia':
            kikpoints += 1
        elif answer3 == 'A lavorare alla Nasa':
            silviapoints += 1
        else:
            giorgiapoints += 1
        choices4 = ['Vis a Vis', 'Attack on Titan', 'Whiplash', 'Gossip girl', 'How I met your mother', 'Top gun', 'Star Wars','Domanda di riserva?']
        answer4 = st.radio("Quale tra i seguenti film/serie tv preferisci?", choices4)
        if answer4 == 'Vis a Vis':
            jessicapoints += 1
        elif answer4 == 'Attack on Titan':
            beatricepoints += 1
        elif answer4 == 'Domanda di riserva?':
            paolapoints += 1
        elif answer4 == 'Whiplash':
            clarapoints += 1
        elif answer4 == ' Gossip girl':
            giorgiapoints += 1
        elif answer4 == 'How I met your mother?':
            kikpoints += 1
        elif answer4 == 'Top gun':
            silviapoints += 1
        else:
            giorgiapoints += 1
        choices5 = ["Maggie Civantos", "Taylor Swift", "Ariana Grande", "Lauren Jauregui", "Paul McCartney", "Ranboo", "Tom Cruise", "Troppe scelte"]
        answer5 = st.radio("Quale tra le seguenti celebrità preferisci?", choices5)
        if answer5 == 'Maggie Civantos':
            jessicapoints += 1
        elif answer5 == "Taylor Swift":
            beatricepoints += 1
        elif answer5 == 'Ariana Grande':
            clarapoints += 1
        elif answer5 == 'Lauren Jauregui':
            paolapoints += 1
        elif answer5 == 'Paul McCartney':
            mariannapoints += 1
        elif answer5 == 'Ranboo':
            kikpoints += 1
        elif answer5 == 'Troppe scelte':
            giorgiapoints += 1
        else:
            silviapoints += 1
        st.write("Guarda queste immagini...")
        visualizza_immagini(imagelist)
        choices6 = ['1','2','3','4','5','6','7','8']
        answer6 = st.radio("... e scegli la moodboard che ti rappresenta", choices6)
        if answer6 == '6':
            jessicapoints += 1
        elif answer6 == "2":
            beatricepoints += 1
        elif answer6 == '1':
            clarapoints += 1
        elif answer6 == '5':
            paolapoints += 1
        elif answer6 == '7':
            mariannapoints += 1
        elif answer6 == '4':
            kikpoints += 1
        elif answer6 == '3':
            giorgiapoints += 1
        else:
            silviapoints += 1
        choices7 = ["Solo muere quién es olvidado", "Learn to live alongside cringe", "Living without passion is like being dead", "This world is cruel and merciless,but it also very beautiful", "I assure you,brother,the sun will shine on us again.", "Lassù non c’hai il tempo di pensare. Se pensi sei morto", "Panta rei", "Non lo so"]
        answer7 = st.radio("Quale tra le seguenti citazioni preferisci?", choices7)
        if answer7 == 'Solo muere quién es olvidado':
            jessicapoints = jessicapoints + 1
        elif answer7 == 'Solo muere quién es olvidado':
            paolapoints += 1
        elif answer7 == 'Living without passion is like being dead':
            clarapoints += 1
        elif answer7 == 'This world is cruel and merciless,but it also very beautiful':
            beatricepoints += 1
        elif answer7 == 'I assure you,brother,the sun will shine on us again':
            kikpoints += 1
        elif answer7 == 'Lassù non c\'hai il tempo di pensare. Se pensi sei morto':
            silviapoints += 1
        elif answer7 == 'Panta rei':
            mariannapoints += 1
        else:
            giorgiapoints += 1
            
        submitted = st.form_submit_button("Submit")

        listapunti = [clarapoints, beatricepoints, jessicapoints, silviapoints, giorgiapoints, mariannapoints, kikpoints, paolapoints]
        max_value = max(listapunti)
        if submitted:
            if max_value == clarapoints:
                st.markdown("## Congratulazioni! La tua webbina è Clara")
            elif max_value == beatricepoints:
                st.markdown("## Congratulazioni! La tua webbina è Beatrice")
            elif max_value == jessicapoints:
                st.markdown("## Congratulazioni! La tua webbina è Jessica")
            elif max_value == silviapoints:
                st.markdown("## Congratulazioni! La tua webbina è Silvia")
            elif max_value == giorgiapoints:
                st.markdown("## Congratulazioni! La tua webbina è Giorgia")
            elif max_value == mariannapoints:
                st.markdown("## Congratulazioni! La tua webbina è Marianna")
            elif max_value == kikpoints:
                st.markdown("## Congratulazioni! La tua webbina è Kik")
            elif max_value == paolapoints:
                st.markdown("## Congratulazioni! La tua webbina è Paola")
                
        key = 'FormSubmitter:my_form-Submit'

            
root_path = "/Users/marianna/vscode/stemdays/img_quiz"

lista_di_immagini = ["stanza1.jpeg", 'stanza2.jpeg', 'stanza3.jpeg', 'stanza4.jpeg', 'stanza5.jpeg',
             'stanza6.jpeg', 'stanza7.jpeg', 'stanza8.jpeg']





if __name__ == "__main__":
    quiz()
    