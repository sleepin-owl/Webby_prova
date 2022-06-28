import pandas as pd
import streamlit as st
from musixmatch import Musixmatch
from youtubesearchpython import VideosSearch
st.set_page_config(layout="wide")


def visualise_youtube_video(track_name, track_artist):
            name_and_artist_string = " ".join(
                [track_name,
                track_artist]
            )
            st.write(name_and_artist_string)

            videosSearch = VideosSearch(
                name_and_artist_string,
                limit=1
            )

            if videosSearch.result()["result"]:
                st.write(videosSearch.result()["result"][0]["link"])
                st.video(videosSearch.result()["result"][0]["link"])
            else:
                st.error("Il video di questo brano non è stato trovato. Scusate.")


def style():
    with open('statics.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    tracks_data = dataframe()
    tracks_data_vecchio = dataframe_vecchio()
    # st.dataframe(tracks_data)

    
     
    
    st.markdown("<h2 class='title-search';'> Ricerca la canzone</h2>", unsafe_allow_html=True)
    selected_song = st.selectbox('Inserisci il nome della canzone', tracks_data['song_name'])
    selected_song_row = tracks_data[tracks_data['song_name'] == selected_song]
    # st.write(selected_song_row)
    selected_artist = selected_song_row['artist_1'].values[0]
    selected_artist2 = selected_song_row['artist_2'].values[0]
    selected_artist3 = selected_song_row['artist_3'].values[0]
        
    selected_date = selected_song_row['release_date'].values[0]
        
    name_song = f'''{selected_song}'''
        
    if str(selected_artist2) == 'nan':
        selected_artist2 = ''
    if str(selected_artist3) == 'nan':
        selected_artist3 = ''
            
    
    if len(selected_artist2) == 0 and len(selected_artist3) == 0:
        artist_song = f'''{selected_artist}'''
    elif len(selected_artist2) > 0:
        artist_song = f'{selected_artist}, {selected_artist2}'
    elif len(selected_artist3) > 0:
        artist_song = f'{selected_artist}, {selected_artist3}'
    if len(selected_artist2) > 0 and len(selected_artist3) > 0:
        artist_song = f'{selected_artist}, {selected_artist2}, {selected_artist3}'

    
    date_song = f'''{selected_date}'''
        
        
    st. metric(label='Titolo', value=name_song)
    st.metric(label='Artista', value=artist_song)
    st.metric(label='Data di uscita', value=date_song)
    
    st.markdown('**** ****')
    st_searchSong, buf, st_searchEmbed = st.columns([10,1,10])
    

    with st_searchSong:
        st.markdown("<h2 class='title-search';'>Dello stesso artista</div>", unsafe_allow_html=True)
        same_artist = tracks_data.loc[tracks_data['artist_1'] == selected_artist, "song_name"]
        
        same_artist_list = same_artist.values.tolist()

        for song in same_artist_list:
            st.markdown(f"<p class='same-artist'>{song}</p>", unsafe_allow_html=True)


    with st_searchEmbed:
        st.markdown("<h2 class='title-search';'> Ricerca il testo o vedi il music video</h2>", unsafe_allow_html=True)
        
        mxm = Musixmatch('d63448247d144f22f2bfc15d5bfc58ba')
        track_response = mxm.track_search(
            q_artist = selected_artist,
            q_track = selected_song,
            page_size=10, page=1, s_track_rating='desc'
        )

        if len(track_response["message"]["body"]["track_list"]) > 0:
            track_id = track_response["message"]["body"]["track_list"][0]["track"]["track_id"]
            if mxm.track_lyrics_get(track_id)["message"]["header"]["status_code"] == 200:
                testo = mxm.track_lyrics_get(track_id)["message"]["body"]["lyrics"]["lyrics_body"]
                st.write(testo)
            else:
                st.error("Il testo di questo brano non è stato trovato. Scusate.")
        else:
            st.error("Il testo di questo brano non è stato trovato. Scusate.")
        
        visualise_youtube_video(selected_song, selected_artist)
            
        
        
       
    
def main ():
    st.title('Ricerca il tuo brano! 🔍')
    st.markdown("<p class='welcome-caption';'> Usa la barra di ricerca per trovare la canzone che preferisci. </p>", unsafe_allow_html=True)
    st.markdown('**** ****')
    style()
   
def dataframe():
    url = "https://raw.githubusercontent.com/baggiponte/webby-2022/main/data/processed/random_tracks.csv"
    tracks_data = pd.read_csv(url, index_col=0).sort_index()
    return tracks_data

def dataframe_vecchio():
    url_vecchio = "https://raw.githubusercontent.com/AleCioc/STEMdays/master/10k_random_tracks.csv"
    tracks_data_vecchio = pd.read_csv(url_vecchio, index_col=0).sort_index()
    return tracks_data_vecchio
    
if __name__ == '__main__':
    main()
    


