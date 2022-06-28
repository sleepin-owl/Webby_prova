import pandas as pd
import streamlit as st
import altair as alt

import plotly.express as px

st.set_page_config(layout="wide")

def style():
    with open('statics.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    tracks_data = dataframe()
    
    st_chartbar, buf, st_chartroot = st.columns([10,1,10])
    
    with st_chartbar:
        st.markdown("<h2 class='title-search';'>Confronta due brani</h2>", unsafe_allow_html=True)
        
        chosen_songs: tuple[str, str] = st.multiselect(
            label='Seleziona solo due canzoni', 
            options=tracks_data["song_name"],
            default=["Style", "Bergamo"],
        )

        if len(chosen_songs) > 2 or len(chosen_songs) < 2:
            raise ValueError("Seleziona solo due canzoni")
            st.stop()
        else:
            cols =['song_name', 'popularity', 'danceability', 'energy', 'loudness', 'liveness']
            
            songs = (
                pd.concat([
                    tracks_data.loc[tracks_data["song_name"] == chosen_songs[0], cols],
                    tracks_data.loc[tracks_data["song_name"] == chosen_songs[1], cols]
                ])
                .pipe(
                    pd.melt,
                    id_vars=["song_name"],
                )
            )


            chart = alt.Chart(songs).mark_bar().encode(
                x=alt.X("song_name:N", title=None),
                color="song_name",
                column="variable:O",
                y="value:Q"
            )
            

            st.altair_chart(chart)
    
    with st_chartroot:
        st.markdown(f"<h2 class='title-search';'>{chosen_songs[0]}</h2>", unsafe_allow_html=True)     
        fig = px.line_polar(songs.loc[lambda df: df.song_name == chosen_songs[0]], r='value', theta='variable', line_close=True)
        st.plotly_chart(fig)
        
        st.markdown(f"<h2 class='title-search';'>{chosen_songs[1]}</h2>", unsafe_allow_html=True)     
        fig = px.line_polar(songs.loc[lambda df: df.song_name == chosen_songs[1]], r='value', theta='variable', line_close=True)
        st.plotly_chart(fig)
        
    
def main ():
    st.title('Analytics 📊')
    st.markdown("<p class='welcome-caption';'> In questa sezione analizzi e confronti la tua musica preferita! </p>", unsafe_allow_html=True)
    st.markdown('**** ****')
    style()
   
def dataframe():
    url = "https://raw.githubusercontent.com/baggiponte/webby-2022/main/data/processed/random_tracks.csv"
    tracks_data = pd.read_csv(url, index_col=0).sort_index()
    return tracks_data

if __name__ == '__main__':
    main()


