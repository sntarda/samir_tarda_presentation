import streamlit as st

def main(st):
    
    st.markdown("""
    <h1 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>FINAL PROJECT PRESENTATION</h1>
    """, unsafe_allow_html=True)
    st.write("-----------------------------")

    canva_embed_code = """
    <div style="position: relative; width: 100%; height: 0; padding-top: 56.2500%;
    padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
    border-radius: 8px; will-change: transform;">
    <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
        src="https://www.canva.com/design/DAGDupfpCso/AbJuV5Mfc7iMrWHgtcsvBQ/view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
    </iframe>
    </div>
    <a href="https://www.canva.com/design/DAGDupfpCso/AbJuV5Mfc7iMrWHgtcsvBQ/view?utm_content=DAGDupfpCso&utm_campaign=designshare&utm_medium=embeds&utm_source=link" target="_blank" rel="noopener"></a> by Samir Tarda
    """

    # Display Canva embed code in Streamlit app
    st.markdown(canva_embed_code, unsafe_allow_html=True)



   