import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
from PIL import Image

def main():
    with open('statics.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
   
        st.title("About us :sparkles:")
        st.markdown("<p class='welcome-caption';'> Breve presentazione delle ragazze che hanno lavorato al progetto. ATTENZIONE ABUSO DI IRONIA! </p>", unsafe_allow_html=True)
        st.markdown('**** ****')
        

        st.markdown("<h2 class='title-search';'> Paola</h2>", unsafe_allow_html=True)
        st.markdown("""<p class='site-description'>Appassionata dall'astrologia a livelli estremi, tanto da aver costretto Paolo Fox alle dimissioni (questione di nomi…); è meglio conosciuta come quella letteralmente OSSESSIONATA da Taylor Swift. No, davvero, non sta zitta un attimo. Ne parlerebbe senza sosta se le fosse possibile. Abbiamo tentato di sopprimerla ma è risorta cantando “My tears ricochet”, anche se sembrava più una gallina a cui viene tirato il collo. E se provi a criticare il suo idolo, ti scaglia contro tutta la furia degli dei dell'Olimpo, invocandoli in greco antico. Cosa c'è di peggio di una classicista infuriata? Una classicista SWIFTIE infuriata.</p>""", unsafe_allow_html=True)
        
        st.markdown("<h2 class='title-search';'> Marianna</h2>", unsafe_allow_html=True)
        st.markdown("""<p class='site-description'>È quella intelligente del gruppo, sfrutta i poteri della fisica del suono per inviarti le peggio disgrazie sotto forma di onde anomale. Guai a te se le fai perdere la pazienza (anche perché devi impegnarti VERAMENTE tanto). Fondatrice del “Team Marianna”, Startup di cui è contemporaneamente CEO e dipendente. Intollerante alla stupidità, è alla ricerca di personale. No perditempo.</p>""", unsafe_allow_html=True)
        
        st.markdown("<h2 class='title-search';'> Jessica</h2>", unsafe_allow_html=True)
        st.markdown("""<p class='site-description'>L'ossessivo-compulsiva del gruppo, non si farà scrupoli a ucciderti spietatamente se lascerai qualcosa fuori posto. Ti consiglio di essere precisə quando ti trovi a lavorare con lei, ma se tieni poco alla tua vita, mettile il portapenne in disordine. Silenziosa ma cattiva.</p>""", unsafe_allow_html=True)
        
        st.markdown("<h2 class='title-search';'> Beatrice</h2>", unsafe_allow_html=True)
        st.markdown("""<p class='site-description'>L'altra Swiftie, nonché l'unica che coglie al volo le citazioni di Paola-Fox-Swift. Si è offerta di programmare la versione multi-lingue del sito, ma odia lo spagnolo e abbiamo optato per la sezione quiz. Fissata con il lilla, i gatti neri e il numero 13. Probabilmente è una strega, ma almeno somiglia a Taylor Swift, che di recente le ha proposto di diventare la sua make up artist. Un insider ha rivelato che le due sono amanti, e i fan sospettano che “Seven” sia stata scritta proprio per Bea. L'oracolo di Delfi ammonisce: “L'età è solo un numero, ma anche gli anni di galera”. Attenta Taylor, la pena per questi reati va da 7 a 13 anni di reclusione.</p>""", unsafe_allow_html=True)
        
        st.markdown("<h2 class='title-search';'> Clara</h2>", unsafe_allow_html=True)
        st.markdown("""<p class='site-description'>La disegnatrice, studia Arti figurative al Liceo Artistico. Paola e Bea hanno organizzato una colletta per provare a commissionarle una statua di Taylor in stile Madame Tusseauds, ma l'Italia è un popolo ignorante e non conosce la vera arte (n.d.r. questo lo ha scritto Paola), per cui sono riuscite a raccogliere 10 euro. È grazie a lei se questo sito è perlomeno guardabile. Conosce l'arte della freddura nei momenti meno opportuni, quindi anche se le sue opere sono più care degli assorbenti in Italia riesce sempre a strapparci una risata.</p>""", unsafe_allow_html=True)
        
        st.markdown("<h2 class='title-search';'> Giorgia</>", unsafe_allow_html=True)
        st.markdown("""<p class='site-description'>Da un lato il braccio (Clara), dall'altro la mente. Lei studia Design all'Artistico e giustamente non sopporta le cose fatte male - infatti il secondo giorno di lavoro abbiamo rischiato due/tre volte la morte, tra lei e Miss OCD. Timidina ma lavoratrice, ha un talento per le cose ✨aesthetic✨ e ha uno spiccato senso dell'umorismo (n.d.r. parole del “braccio”). Si spaventa quando vede un computer, a meno che non ci sia AutoCAD aperto.</p>""", unsafe_allow_html=True)
        
        st.markdown("<h2 class='title-search';'> Silvia</h2>", unsafe_allow_html=True)
        st.markdown("""<p class='site-description'>Un ossimoro vivente: possiede gadget de “Il Signore degli anelli” ma non ha mai avuto il tempo di guardarlo. È l'unica che capisce i tecnicismi di Kiara quando si tratta di informatica e la amiamo perché sa tradurli in linguaggio pseudo-umano. Insomma, il nostro personale traduttore simultaneo dal codice binario all'italiano. Indimenticabile la sua treccina Padawan, unica sicurezza in questi giorni insieme a Taylor Swift.   </p>""", unsafe_allow_html=True)
        
        st.markdown("<h2 class='title-search';'> Kiara</h2>", unsafe_allow_html=True)    
        st.markdown("""<p class='site-description'>Avete presente il meme Hackerman? Ecco, il tizio è lei. Ogni giorno ti fa scoprire un videogioco diverso, a differenza nostra che siamo rimaste al dinosauro di Chrome. Da subito abbiamo scoperto il suo talento nel fare sticker esilaranti per Whatsapp a partire dai meme di Clara. Sa un po' di tutto, ma soprattutto è l'unica che sa usare Python. Sicuramente il pilastro del gruppo.</p>""", unsafe_allow_html=True)
        
        st.balloons()

  
        
if __name__ == "__main__":
    main()
