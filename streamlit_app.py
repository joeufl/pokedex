import os
from datetime import date
import streamlit as st
import pandas as pd

st.title("Pokedex Tracker")

@st.cache_data(ttl=60)
def fetch_data():
    df = pd.read_csv(data_file)
    return df

data_file = os.path.join(os.getcwd(), "static", "POKEMON_DATA.csv")
df = fetch_data()

# Shinies
shinies = df.loc[df['SHINY'] != 'Y', ['ID']]
shiny_str = ''
shiny_list = shinies['ID'].to_list()
for i in shiny_list: 
    s = str(i)
    shiny_str += s
    shiny_str += ','
shiny_base = 'shiny&!traded&'
shiny_concat = shiny_base + shiny_str
clean_shinies = shiny_concat[:-1]

# Lucky
lucky = df.loc[df['LUCKY'] != 'Y', ['ID']]
lucky_str = ''
lucky_list = lucky['ID'].to_list()
for i in lucky_list: 
    s = str(i)
    lucky_str += s
    lucky_str += ','
lucky_base = '!traded&'
lucky_concat = lucky_base + lucky_str
clean_lucky = lucky_concat[:-1]

# Jillian
shinies_j = df.loc[df['JILLIAN'] != 'Y', ['ID']]
shiny_str_j = ''
shiny_list_j = shinies_j['ID'].to_list()
for i_j in shiny_list_j: 
    s_j = str(i_j)
    shiny_str_j += s_j
    shiny_str_j += ','
shiny_base_j = 'shiny&!traded&'
shiny_concat_j = shiny_base_j + shiny_str_j
clean_shinies_j = shiny_concat_j[:-1]

# Print to Streamlit
st.subheader('Tap/Hover over a section below and copy')

st.write('Shiny Pokemon')
st.code(clean_shinies, language=None)

st.write('Lucky Pokemon')
st.code(clean_lucky, language=None)

st.write('Jillian Shiny Living Pokemon (Kanto)')
st.code(clean_shinies_j, language=None)