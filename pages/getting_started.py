import streamlit as st
st.title('Getting Started Using My Own Data')

st.write('Download a copy of the file below')
with open("base/pokemon.csv", "rb") as file:
    st.download_button(
        label="Download File",
        data=file,
        file_name="pokedex.csv",
    )

st.write('Upload the file to Google Drive')
st.write('Mark the Pokemon you need with a "Y" in the column you need (SHINY or LUCKY)')
st.write('Click SHARE, make sure the access is "Anyone with the link", then click Copy Link')
st.write('Note the character string in the URL')
st.write('For example, if your URL is "docs.google.com/spreadsheets/d/1GkeodImJ24ulJpE94ddZTeujSI0/edit?usp=sharing", so you want to note this string: "1GkeodImJ24ulJpE94ddZTeujSI0".')