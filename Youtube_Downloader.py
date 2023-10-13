from io import BytesIO
import streamlit as st
from settings import *
from streamlit_lottie import st_lottie
import streamlit as st
from streamlit_option_menu import option_menu
from pytube import YouTube

# streamlit run Youtube_Downloader.py
st.set_page_config(page_title=TITLE,
    layout="wide")

st.markdown("<h2 style=\
    'text-align : center';\
    font-weight : bold ;\
    font-family : Arial;>\
    Youtube Downloader</h2>", unsafe_allow_html=True)

st.markdown("""---""")

with st.sidebar :
    nav_menu = option_menu(menu_title=None, options=['Home', 'Download Audio', 'Download Video'], 
        default_index=0, orientation="vertical",
        icons=["youtube", "mic", "camera-video"],
        styles={
            "container": {"padding": "0!important"},
            "nav-link": {"font-size": "14px", "text-align": "left", "margin":"2px", "--hover-color": "#805E83"}
        })

if nav_menu == 'Home':
    st.markdown("<br>", unsafe_allow_html=True)

    colpi1, colpi2 = st.columns([85, 15], gap="small")
    with colpi1:
        st.info("This tool allows you to :\
            \n ● Listen to and download YouTube videos in audio format\
            \n ● Watch and download YouTube videos in 720p video format\
            \n\n Please select the desired module from the left menu")
        
        # st.warning("Pytube library is currently encountering some issues, a fix is in progress...")

    with colpi2:
        lottie_yt = load_lottiefile(lottie_yt)
        st_lottie(
            lottie_yt,
            speed=1,
            reverse=False,
            loop=True,
            quality="high", # medium ; high ; low
            height=150)


if nav_menu == 'Download Audio':

    @st.cache_data(show_spinner=False) # Special thank to : Franky1
    def download_audio_to_buffer(url):
        buffer = BytesIO()
        youtube_video = YouTube(url)
        audio = youtube_video.streams.get_audio_only()
        default_filename = audio.default_filename
        audio.stream_to_buffer(buffer)
        return default_filename, buffer

    colpi1_aud, colpi2_aud = st.columns([85, 15], gap="small")
    with colpi1_aud :
        url = st.text_input(label="📌 Download Youtube AUDIO",
            placeholder="Copy/Paste the video URL to download here...")
    with colpi2_aud :  
        st.markdown("<br>", unsafe_allow_html=True)
        dl_btn_audi = st.button(label="➰Start Conversion", use_container_width=True)

    BASE_YOUTUBE_URL1 = "https://www.youtube.com"
    BASE_YOUTUBE_URL2 ="https://youtu.be"

    if dl_btn_audi :
        # if not (str(url.lower().startswith(BASE_YOUTUBE_URL1)) or str(url.lower().startswith(BASE_YOUTUBE_URL2))):
        #    st.error("Veuillez saisir une URL de video Youtube valide")
        try :
            with st.spinner("Conversion in progress... Please wait") :
                default_filename, buffer = download_audio_to_buffer(url)

            title_vid = Path(default_filename).with_suffix(".mp3").name

            st.markdown(f"<h5 style=\
                'text-align : center';\
                font-weight : bold ;\
                font-family : Arial;>\
                <u>Title :</u> {title_vid[:-4]}</h5>", unsafe_allow_html=True)

            st.download_button(
                label="✔ Download Audio",
                data=buffer,
                file_name=title_vid,
                mime="audio/mpeg")

            st.audio(buffer, format='audio/mpeg')

        except:
            st.error("The URL is protected or incorrect, please try again with another address")      
            

if nav_menu == 'Download Video':

    @st.cache_data(show_spinner=False)
    def download_video_to_buffer(url):
        buffer = BytesIO()
        youtube_video = YouTube(url)
        video = youtube_video.streams.filter(progressive="True",file_extension="mp4").order_by('resolution').desc()
        video_720p=video[0]
        default_filename = video_720p.default_filename
        video_720p.stream_to_buffer(buffer)
        return default_filename, buffer

    colpi1_vid, colpi2_vid = st.columns([85, 15], gap="small")
    with colpi1_vid :
        url_vid = st.text_input(label="📌 Download Youtube VIDEO",
            placeholder="Copy/Paste the video URL to download here...")

    with colpi2_vid :  
        st.markdown("<br>", unsafe_allow_html=True)
        dl_btn_vid = st.button(label="➰Start Conversion", use_container_width=True)

    BASE_YOUTUBE_URL1_vid = "https://www.youtube.com"
    BASE_YOUTUBE_URL2_vid ="https://youtu.be"

    if dl_btn_vid :
        try :
            with st.spinner("Conversion in progress... Please wait") :
                default_filename_video, buffer_vid = download_video_to_buffer(url_vid)

            title_video = Path(default_filename_video).with_suffix(".mp4").name

            st.markdown(f"<h5 style=\
                'text-align : center';\
                font-weight : bold ;\
                font-family : Arial;>\
                <u>Title :</u> {title_video[:-4]}</h5>", unsafe_allow_html=True)

            st.download_button(
                label="✔ Download Video",
                data=buffer_vid,
                file_name=title_video,
                mime="video/mpeg")

            esp1_vid, col_video, esp2_vid = st.columns([15, 70, 15], gap="small")
            with col_video :
                st.video(buffer_vid, format='video/mpeg')

        except:
            st.error("The URL is protected or incorrect, please try again with another address")
