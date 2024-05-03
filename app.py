import streamlit as st
from streamlit_option_menu import option_menu
import dataset
import activeEnrollment, present, financialAnalysis, demographics, dashboard

st.set_page_config(
    page_title="Final Project",
    page_icon=":chart_with_downwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define the CSS style for the iframe
iframe_style = """
    width: 1024px; 
    height: 612px;
    border: none 
"""

with st.sidebar:
    selected = option_menu("Main Menu", ["Presentation", "Looker Dashboard", "Dataset", "Enrollment", "Financial", "Demographics"], 
    icons=['bi bi-projector', 'bi bi-bar-chart-line-fill', 'bi bi-filetype-csv', "bi bi-card-checklist", 'bi bi-currency-dollar', 'bi bi-people-fill'], 
    menu_icon="cast", default_index=0, orientation="vertical")

if selected == "Presentation":
    present.main(st)
elif selected == "Looker Dashboard":
    dashboard.main(st, iframe_style)
elif selected == "Dataset":
    st.markdown("""
    <h1 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>Dataset: Student and Billing Information</h1>
    """, unsafe_allow_html=True)
    st.write("-----------------------------")
    
    # Note to TA
    st.markdown("""
    <div>
        <h4 style='text-align: left; font-weight: bold; color: #FF3131; margin-bottom: -10px;'>PLEASE NOTE:</h4>
        <div style='text-align: justify;'>
            <strong><em>This dataset has been obtained from a real business. Student names have been removed for confidentiality purposes. 
            Please feel free to click on the "Fullscreen" option to view the entire dataset.</em></strong>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    df = dataset.load_data()    
    st.write(df)
    
    dataset.describe_dataset()

elif selected == "Enrollment":
    activeEnrollment.main(st, iframe_style)
elif selected == "Financial":
    financialAnalysis.main(st, iframe_style)
elif selected == "Demographics":
    demographics.main(st, iframe_style)



