import os
from datetime import date
import streamlit as st
import pandas as pd

st.title("Pokedex Tracker")

@st.cache_data(ttl=60)
def fetch_data():
    df = pd.read_csv(data_file)
    return df

data_file = os.path.join(os.getcwd(), "static", "shinypokemon.csv")
df = fetch_data()

static = 'shiny&!traded&'
display = df['id'].tolist()
new = '' 

for i in display: 
    s = str(i)
    new += s
    new += ','

concat = static +  new
clean = concat[:-1]

st.subheader('Tap/Hover over a section below and copy')


st.write('Shiny Pokemon')
st.code(clean, language=None)

st.write('Lucky Pokemon (placeholder)')

st.code(clean, language=None)