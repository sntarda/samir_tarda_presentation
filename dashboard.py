import streamlit as st

def main(st, iframe_style):
    iframe_style = {iframe_style}
    st.write(f'<iframe width="1200" height="1600" src="https://lookerstudio.google.com/embed/reporting/78af4f00-fcfa-4f0b-bb14-a59abc6124e6/page/1M" frameborder="0" style="border:0" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"></iframe>', unsafe_allow_html=True)