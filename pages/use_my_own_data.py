import streamlit as st
st.title('Keep a copy of your own data')

st.write('Download a copy of the file below')
with open("base/pokemon.csv", "rb") as file:
    st.download_button(
        label="Download File",
        data=file,
        file_name="pokedex.csv",
    )
st.write('Upload the file to Google Drive')
st.write('Mark the Pokemon you need with a "Y" in the column you need (SHINY or LUCKY)')
st.write('Note the character string in the URL')