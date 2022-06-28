import streamlit as st

root_path = "/Users/marianna/vscode/stemdays/img_quiz"

lista_di_immagini = ["stanza1.jpeg", 'stanza2.jpeg', 'stanza3.jpeg', 'stanza4.jpeg', 'stanza5.jpeg',
             'stanza6.jpeg', 'stanza7.jpeg', 'stanza8.jpeg']
st.set_page_config(layout="wide")


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


def quiz_uno():
    with open('statics.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    with st.form("my_form"):
        st.markdown("<h1 style='text-align: center; color:#87CEEB'>QUIZ </h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color:#FFFACD'>Your daily tune</h2>", unsafe_allow_html=True)

        st.markdown(
            "<h3 style='text-align: center; color:light blue'>Based on your answer we will give you the perfect "
            "song to go along with your day</h3>", unsafe_allow_html=True)

        umore = st.select_slider("Come stai?", options=["feeling low", "could be better", "I'm ok", "I'm doing good",
                                                        "feeling blessed"])
        rappoints = 0
        indiepoints = 0
        rockpoints = 0
        classicapoints = 0
        poppoints = 0
        countrypoints = 0
        edmpoints = 0
        regaettonpoints = 0

        if umore == "feeling low":

            indiepoints = indiepoints + 1
            rockpoints = rockpoints + 1
        elif umore == "could be better":

            indiepoints = indiepoints + 1
            classicapoints = classicapoints + 1

        elif umore == "I'm ok":

            poppoints = poppoints + 1
            rappoints = rappoints + 1
        elif umore == "I'm doing good":

            countrypoints = countrypoints + 1
            poppoints = poppoints + 1

        else:

            regaettonpoints = regaettonpoints + 1
            edmpoints = edmpoints + 1

        stagione = st.radio("Qual è la tua stagione preferita?", ("Summer", "Fall", "Winter", "Spring"))

        if stagione == "Summer":

            regaettonpoints = regaettonpoints + 1
            edmpoints += 1

        elif stagione == "Fall":

            indiepoints += 1
            classicapoints += 1
        elif stagione == "Winter":

            rappoints += 1
            rockpoints += 1

        else:

            poppoints += 1
            countrypoints += 1

        posto = st.radio(
            "Dove preferiresti vivere?", ("Mare", "Città", "Montagna", "Campagna"))

        if posto == "Mare":

            regaettonpoints += 1
            edmpoints += 1

        elif posto == "Montagna":

            indiepoints += 1
            classicapoints += 1
        elif posto == "Città":

            rappoints += 1
            poppoints += 1


        else:

            rockpoints += 1
            indiepoints += 1

        sabato = st.radio("Come passeresti il tuo sabato sera?",
                          ("A leggere e scrivere", "In discoteca", "In casa con gli amici", "A guardare serie tv"))

        if sabato == "In discoteca":

            regaettonpoints += 1
            edmpoints += 1

        elif sabato == "A leggere e scrivere":

            indiepoints = indiepoints + 1
            classicapoints = classicapoints + 1
        elif sabato == "In casa con gli amici":

            rappoints = rappoints + 1
            rockpoints = rockpoints + 1

        else:

            poppoints = poppoints + 1
            countrypoints = countrypoints + 1

        tv = st.radio("Cosa preferisci guardare in tv?", ("Film", "Serie tv", "Anime",
                                                          "Reality show trash"))

        if tv == "Reality show trash":

            regaettonpoints = regaettonpoints + 1
            edmpoints = edmpoints + 1

        elif tv == "Film":

            rappoints = rappoints + 1
            classicapoints = classicapoints + 1
        elif tv == "Indie":

            indiepoints = indiepoints + 1
            rockpoints = rockpoints + 1

        else:

            poppoints = poppoints + 1
            countrypoints = countrypoints + 1

        st.write("Guarda queste immagini...")
        visualizza_immagini(lista_di_immagini)
        stanze = st.radio(
            "Quale tra le seguenti stanze preferisci?", ("1", "2", "3", "4", "5", "6", "7", "8"))

        if stanze == "1":

            indiepoints = indiepoints + 1

        elif stanze == "2":

            rockpoints = rockpoints + 1
        elif stanze == "3":

            countrypoints = countrypoints + 1
        elif stanze == "4":

            regaettonpoints = regaettonpoints + 1
        elif stanze == "5":

            edmpoints = edmpoints + 1
        elif stanze == "6":

            rappoints = rappoints + 1
        elif stanze == "7":

            classicapoints = classicapoints + 1

        else:

            poppoints = poppoints + 1

        cantanti = st.radio(
            "Quale tra i seguenti artisti preferisci?", ("Taylor Swift-Shawn Mendes", "Nirvana-Guns 'n' Roses",
                                                         "Vivaldi-Mozart", "Ariete-Gazzelle", "Maluma-Rosalia",
                                                         "Carrie Underwood-Tim McGraw",
                                                         "Martin Garrix-Avicii", "Mostro-Eminem"))

        if cantanti == "Taylor Swift-Shawn Mendes":

            poppoints = poppoints + 1

        elif cantanti == "Nirvana-Guns 'n' Roses":

            rockpoints = rockpoints + 1
        elif cantanti == "Vivaldi-Mozart":

            classicapoints = classicapoints + 1
        elif cantanti == "Ariete-Gazzelle":

            indiepoints = indiepoints + 1
        elif cantanti == "Maluma-Rosalia":

            regaettonpoints = regaettonpoints + 1
        elif cantanti == "Carrie Underwood-Tim McGraw":

            countrypoints += 1
        elif cantanti == "Martin Garrix-Avicii":

            edmpoints = edmpoints + 1

        else:
            
            rappoints = rappoints + 1

        submitted = st.form_submit_button("Submit")

        lista_punti = [rappoints, rockpoints, edmpoints, classicapoints, indiepoints, countrypoints, poppoints,
                       regaettonpoints]
        max_value = max(lista_punti)
        if submitted:
            if max_value == rappoints:

                st.write("Sei rap!")
            elif max_value == rockpoints:

                st.write("Sei rock!")
            elif max_value == edmpoints:
                
                st.markdown("""<h2>SEI EDM!</h2>""", unsafe_allow_html=True)
                st.markdown("""<p class='site-description';> La discoteca è la tua casa e sicuramente sai come divertirti! I tuoi amici potrebbero lamentarsi e dire che sei troppo rumorosə, ma sei solo estroversə. Attenzione: nel giro di un paio d'anni potresti aver bisogno di un apparecchio acustico, quindi inizia a mettere da parte un po' di soldi. </p>""", unsafe_allow_html=True)
                st.markdown("""<p class='recommended-song';> Canzone consigliata: Avicii - The nights</p>""", unsafe_allow_html=True)
                
            elif max_value == regaettonpoints:
                
                st.markdown("""<h2>SEI REGAETTON!</h2>""", unsafe_allow_html=True)
                st.markdown("""<p class='site-description';> È da settembre che aspetti giugno per andare in spiaggia e ballare hit estive. Se ci sei tu sicuramente non ci si annoia (magari esci con EDM) e si balla! In pochi ti sopportano per la tua estroversione, ma è tutta invidia: sei l'anima della festa.</p>""", unsafe_allow_html=True)
                st.markdown("""<p class='recommended-song';> Canzone consigliata: Lauren Jauregui, Tainy - Lento</p>""", unsafe_allow_html=True)
                
            elif max_value == poppoints:

                st.markdown("""<h2>SEI POP!</h2>""", unsafe_allow_html=True)
                st.markdown("""<p class='site-description';>La socialità è il tuo forte, e anche la tua capacità di memorizzare testi. Sei ossessionatə da almeno un cantante iperfamoso (riferimenti a Taylor Swift puramente casuali) e, se qualcuno ti ritiene mainstream e noiosə, in realtà è così. Un pizzico di originalità, amicə.</p>""", unsafe_allow_html=True)
                st.markdown("""<p class='recommended-song';>Canzone consigliata: tutto l'album 1989, ma aspetta che esca la Taylor's Version </p>""", unsafe_allow_html=True)
                
            
            elif max_value == indiepoints:
                
                st.markdown("""<h2>SEI INDIE!</h2>""", unsafe_allow_html=True)
                st.markdown("""<p class='site-description';>Chill è la tua parola d'ordine, e noi approviamo. Ti piace essere alternativə, ma spoiler: non lo sei. Ascolti uno dei generi più ingiustamente bullizzati della storia della musica. </p>""", unsafe_allow_html=True)
                st.markdown("""<p class='recommended-song';>ARIETE - Spifferi (ma anche august di Taylor Swift merita di essere ascoltata)</p>""", unsafe_allow_html=True)
                

            elif max_value == classicapoints:

                st.markdown("""<h2>SEI CLASSICA!</h2>""", unsafe_allow_html=True)
                st.markdown("""<p class='site-description';>La tua vita è un quadro ricco di sfumature estremamente diverse fra loro. L'introspezione regna sovrana, ma al suo cospetto vivono sentimenti e caratteristiche contrastanti. La musica classica è il genere più sottovalutato in assoluto, ma tu hai saputo coglierne il valore. Avrei voluto insultare anche te ma se ascolti classica ti voglio bene in automatico. Complimenti per i gusti.</p>""", unsafe_allow_html=True)
                st.markdown("""<p class='recommended-song';>Brano consigliato: Taylor S- ehm volevo dire, Wolfgang Amadeus Mozart - Sinfonia No. 40 (K550)</p>""", unsafe_allow_html=True)
            
            elif max_value == countrypoints:

                st.markdown("""<h2>SEI COUNTRY!</h2>""", unsafe_allow_html=True)
                st.markdown("""<p class='site-description';>Stivali di pelle, cavalli e pickup? Stereotipi, ma non così tanto. Passi le tue serate davanti al fuoco suonando la chitarra con i tuoi amici, anche se ne hai pochi. Afferra il lazo e al galoppo!</p>""", unsafe_allow_html=True)
                st.markdown("""<p class='recommended-song';>Canzone consigliata: John Denver - Country roads (oppure il debut album di Taylor Swift ;D)</p>""", unsafe_allow_html=True)
                  
            elif max_value == rockpoints:
                st.markdown("""<h2>SEI ROCK!</h2>""", unsafe_allow_html=True)
                st.markdown("""<p class='site-description';>Spirito libero, eh? Non ti piacciono le regole, e sei la dimostrazione del fatto che il mondo è bello perché è vario. Magari non scaldarti troppo quando qualche sfigatello fa confusione tra i sottogeneri: non tutti abbiamo una cultura. Potresti pensare di contare fino a 10 prima di parlare ogni tanto, ma alla fine ci piaci anche così, impulsivə e casinista. Magari non lanciare la chitarra di sotto quando non riesci a suonare come vorresti: potresti pentirtene.</p>""", unsafe_allow_html=True)
                st.markdown("""<p class='recommended-song';>Canzone consigliata: Nirvana - Smells like teen spirit</p>""", unsafe_allow_html=True)
                
            elif max_value == rappoints:
                st.markdown("""<h2>SEI RAP!</h2>""", unsafe_allow_html=True)
                st.markdown("""<p class='site-description';>Decisə come pocə, non ti fai scrupoli quando si tratta di ottenere quello che vuoi (magari resta nell’ambito della legalità). Quando passi per strada con i tuoi fra, incappucciatə nella tua felpa grigia e armatə di bomboletta spray, anche mia zia si spaventa. In realtà hai un cuore d’oro ma hai paura di dimostrarlo, e noi di Rhythmized lo sappiamo bene.</p>""", unsafe_allow_html=True)
                st.markdown("""<p class='recommended-song';>Canzone consigliata: Gemitaiz - Toradol</p>""", unsafe_allow_html=True)
                  
        
        key = 'FormSubmitter:my_form-Submit'


if __name__ == '__main__':
    quiz_uno()