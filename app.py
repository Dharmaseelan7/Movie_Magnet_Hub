import streamlit as st
import requests
import pickle

movies = pickle.load(open("new_movies.pkl", "rb"))
similarity = pickle.load(open("new_similarity.pkl", "rb"))

movies_list = set(movies["title"].values)
movies_list = list(movies_list)
st.set_page_config(layout="wide")

st.markdown(
    "<h1 style='text-align: center; font-size:40px;'>Movie--Magnet--Hub</h1>",
    unsafe_allow_html=True,
)
# st.markdown(
#     "<h1 style='text-align: center; font-size:30px;'>Movie Recommendation System</h1>",
#     unsafe_allow_html=True,
# )
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
selected_movie = st.selectbox(
    "Curious about movies? Make a choice!", movies_list, index=1
)


def fetch_image(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=6567e12fa42dcf7c8aa4f2ef3017278d".format(
        movie_id
    )
    data = requests.get(url)
    data = data.json()
    poster_path = data["poster_path"]
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommand(movie):
    movie_info = [[0, 0, 0, 0, 0, 0] for j in range(11)]
    movie_poster = []
    index = movies[movies["title"] == movie].index[0]
    distance = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1]
    )
    print()
    for i in range(0, 11):
        value = distance[i]
        movies_id = movies.iloc[value[0]].id
        movie_poster.append(fetch_image(movies_id))
        movie_info[i][0] = movies.iloc[value[0]].title
        movie_info[i][1] = movies.iloc[value[0]].genre
        movie_info[i][2] = movies.iloc[value[0]].release_date
        movie_info[i][3] = movies.iloc[value[0]].cast
        movie_info[i][4] = movies.iloc[value[0]].crew
        movie_info[i][5] = movies.iloc[value[0]].overview
    return movie_info, movie_poster


if st.button("Find Your Film"):
    hide_img_fs = """
    <style>
    button[title="View fullscreen"]{
        visibility: hidden;}
    </style>
    """
    st.markdown(hide_img_fs, unsafe_allow_html=True)
    movies_info, movies_poster = recommand(selected_movie)
    main_img, main_info, _ = st.columns(spec=[0.3, 0.45, 0.25], gap="small")
    with main_img:
        st.image(movies_poster[0], width=350)
    with main_info:
        st.markdown(
            """<h1 style='font-size:40px;'>{0} ({1})</h1>""".format(
                movies_info[0][0], movies_info[0][2][0:4]
            ),
            unsafe_allow_html=True,
        )
        st.markdown(
            """<h1 style='font-size:20px;'>{0} (Genre)</h1>""".format(
                movies_info[0][1]
            ),
            unsafe_allow_html=True,
        )
        st.markdown(
            """<h1 style='font-size:20px;'>{0} (Director)</h1>""".format(
                movies_info[0][4][0]
            ),
            unsafe_allow_html=True,
        )
        st.markdown(
            """<h1 style='font-size:20px;'>{0} (Cast)</h1>""".format(movies_info[0][3]),
            unsafe_allow_html=True,
        )
        st.markdown(
            """<h1 style='font-size:20px;'>{0}</h1>""".format(movies_info[0][5]),
            unsafe_allow_html=True,
        )
    st.markdown(
        "<h1 style='text-align: center; font-size:30px;'>More like this</h1><br>",
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4, col5 = st.columns(5, gap="large")
    col6, col7, col8, col9, col10 = st.columns(5, gap="large")
    with col1:
        st.text(movies_info[1][0])
        st.image(movies_poster[1])

    with col2:
        st.text(movies_info[2][0])
        st.image(movies_poster[2])
    with col3:
        st.text(movies_info[3][0])
        st.image(movies_poster[3])
    with col4:
        st.text(movies_info[4][0])
        st.image(movies_poster[4])
    with col5:
        st.text(movies_info[5][0])
        st.image(movies_poster[5])
        st.markdown(
            "<br>",
            unsafe_allow_html=True,
        )
    with col6:
        st.text(movies_info[6][0])
        st.image(movies_poster[6])
    with col7:
        st.text(movies_info[7][0])
        st.image(movies_poster[7])
    with col8:
        st.text(movies_info[8][0])
        st.image(movies_poster[8])
    with col9:
        st.text(movies_info[9][0])
        st.image(movies_poster[9])
    with col10:
        st.text(movies_info[10][0])
        st.image(movies_poster[10])
