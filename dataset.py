import pandas as pd
import streamlit as st

def load_data():
    DATA_URL = 'students_info.csv'
    data = pd.read_csv(DATA_URL)
    df = pd.DataFrame(data)
    return df

def describe_dataset():
    
    multi = '''
    <h5><strong>DATA DESCRIPTION</srong></h5>
    
    The dataset named <strong><em>"student_info.csv"</em></strong> Provides comprehensive details about the students of a private Montessori school, capturing various aspects that span from 
    student enrollment details to financial charges over a the span of two consectutive school calendar year (Augut 2022 - May 2024).
    
    <h5><strong>DATA COLLECTION AND PREPROCESSING:</srong></h5>
    
    The dataset was downloaded from the school's CRM system. Initially, I started with five separate datasets. And after cleaning and wrangling, I was able to co

    Upon reviewing the dataset, we found many inconsistencies and missing information, which we manually cleaned and wrangled through Excel. 
    Then, we used Python code to combine both datasets into one to arrive at this final version, which we then used to implement our visualization graphs.
    
    <h5><strong>DATA FEATURES:</srong></h5>
    
    1. <strong>Students basic identification information:</strong> represented by columns such as "Date", "Student Name", "First Name", and "Last Name", "Gender", "Age", "City". 
    Relationships within the school</strong> are noted through "Sibling Name," suggesting a discount structure for families with multiple children enrolled.
    2. <strong>Financial information:</strong> is detailed through columns like "Charge Category", "Original Charge", "Discount Type", "Discount Amount", and "Adjustment". 
    These entries shed light on the tuition structure, the types and amounts of discounts applied, and any additional adjustments, painting a picture of the school's revenue streams and the financial diversity of its student body.
    3. <strong>Student Enrollment Information:</strong> additonal identifiers about students which include "Status", "Program", "Schedule", "Room", program "Start Time" and "End Time". These addiotional student infromation are crucial
    for understanding enrollment trends and analyzing the financial standing and diversity of the students populaiton within the school.   
    '''
    return st.markdown(multi, unsafe_allow_html=True)


