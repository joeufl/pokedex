import streamlit as st
st.title('Use My Own Data')

import io
from datetime import date
import requests
import streamlit as st
import pandas as pd

FILE_ID = st.text_input('Enter your Google Drive ID')
GID = None  # Sheets only: pick a tab via the #gid= in its URL, or None for the first tab

try:
    @st.cache_data(ttl=600)
    def build_url(file_id, gid):
        if len(file_id) > 40:
            # A Sheet: uc?export=download returns an HTML page, not CSV.
            url = f"https://docs.google.com/spreadsheets/d/{file_id}/export?format=csv"
            return f"{url}&gid={gid}" if gid is not None else url
        # An uploaded file: confirm=t skips the "can't scan for viruses" interstitial.
        return f"https://drive.google.com/uc?id={file_id}&export=download&confirm=t"

    def load_public_data(file_id, gid):
        response = requests.get(build_url(file_id, gid), timeout=30)
        response.raise_for_status()

        # A login or interstitial page comes back as HTML with a 200, so check the body.
        if response.content.lstrip()[:1] == b"<":
            raise ValueError(
                "Got HTML instead of CSV. Check that the ID is right and that the file "
                "is shared as 'Anyone with the link'."
            )
        return pd.read_csv(io.StringIO(response.text))

    try:
        df = load_public_data(FILE_ID, GID)
        # st.dataframe(df)
    except Exception as e:
        st.error(f"Error loading data: {e}")

    base_str = '!favorite&!traded&!shadow&!4*&!mythical&'
    shiny_base = 'shiny&'

    # Needs for Shinies
    shinies = df.loc[df['SHINY'] == 'Y', ['ID']]
    shiny_str = ''
    shiny_list = shinies['ID'].to_list()
    for i in shiny_list: 
        s = str(i)
        shiny_str += s
        shiny_str += ','
    shiny_concat = base_str + shiny_base + shiny_str
    clean_shinies = shiny_concat[:-1]

    # Needs for Lucky
    lucky = df.loc[df['LUCKY'] == 'Y', ['ID']]
    lucky_str = ''
    lucky_list = lucky['ID'].to_list()
    for i in lucky_list: 
        s = str(i)
        lucky_str += s
        lucky_str += ','
    lucky_concat = base_str + lucky_str
    clean_lucky = lucky_concat[:-1]

    # Needs for Shiny and Lucky
    shlucky = df.loc[(df['SHINY'] == 'Y') & (df['LUCKY'] == 'Y'), ['ID']]
    shlucky_str = ''
    shlucky_list = shlucky['ID'].to_list()
    for i in shlucky_list: 
        s = str(i)
        shlucky_str += s
        shlucky_str += ','
    shlucky_concat = base_str + shiny_base + shlucky_str
    clean_shlucky = shlucky_concat[:-1]

    # Print to Streamlit
    st.subheader('Tap/Hover over a section below and copy by clicking the squares')

    st.write('Shiny & Lucky Pokemon You Need')
    st.code(clean_shlucky, language=None)

    st.write('Shiny Pokemon You Need')
    st.code(clean_shinies, language=None)

    st.write('Lucky Pokemon You Need')
    st.code(clean_lucky, language=None)
except:
    print('hello')