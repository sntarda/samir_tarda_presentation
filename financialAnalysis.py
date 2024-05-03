import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st


def read_original_data():
    # dataset file path
    file_path = 'students_info.csv'
    data = pd.read_csv(file_path)
    return data

def stat_summary_data(data):
    data = read_original_data()
    # Define the columns you're interested in
    columns = ['Billing Amount', 'Original Charge', 'Discount Amount', 'Status']
    if columns:  
        # Select only these columns
        df = data.loc[:, columns]     
    return df

def new_func():
    return "Active"

def confusion_matrix_data(data):
    data = read_original_data()
    columns = ['Billing Amount', 'Original Charge', 'Discount Amount', 'Program', 'Date']
    df = data[columns].copy()
    
    df['Program'] = df['Program'].astype('category')
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by='Date')

    for column in ['Billing Amount', 'Original Charge', 'Discount Amount',]:
        df[column] = pd.to_numeric(df[column].replace('[\$,]', '', regex=True).replace('', 'NaN'), errors='coerce')
    
    return df
def pairplot_data(data):
    data = read_original_data()
    # Define the columns you're interested in
    columns = ['Billing Amount', 'Discount Amount', 'Program']
    if columns:  
        # Select only these columns
        df = data.loc[:, columns]     
    return df

def main(st, iframe_style):
    iframe_style = {iframe_style}
    st.markdown("""
    <h1 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>Financial Analysis</h1>
    """, unsafe_allow_html=True)
    st.write("-----------------------------")
    
    # Figure 1
    st.markdown("""
    <h5 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>Figure (1) Line Chart (PowerBI)</h5>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>HISTORY OF Tuition CHARGES: Original Vs. Actual</h4>
    """, unsafe_allow_html=True)

    # Use the st.write() function to display the iframe
    st.write(f'<iframe title="Total Revenue over 2 years" width="1024" height="612" src="https://app.powerbi.com/view?r=eyJrIjoiYjYxNTE4YWUtM2E0ZC00ODMyLThiMmMtZWUyYTE1YjExMGZhIiwidCI6IjcwZGUxOTkyLTA3YzYtNDgwZi1hMzE4LWExYWZjYmEwMzk4MyIsImMiOjN9" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)  
    st.write("\n\n")
    st.subheader("Analysis")
    multi = '''
    The line graph tracks the history of monthly tuition charges over two consecutive school years (August 2022 - May 2024), comparing the original charges against the actual billing amounts 
    after discounts. There are three lines: the "Sum of Billing Amount," "Sum of Original Charge," and "Sum of Discount Amount," each representing the aggregated financial figures over time.
    
    - <strong>IMPORTANCE:</strong>
    It highlights the school’s financial trends and the impact of discounts on the overall revenue. From my experience working at this school for so many years, this is one of the
    most frequently asked for financial reports by ownership. Continuous checking and updating of this information on monthly basis is crucial to the school's financial health. 

    From the graph we can see the consistent gap between the original tuition charges and the actual billed amounts, indicating a steady application of discounts. 
    The "Sum of Discount Amount" remains relatively flat, suggesting a uniform discount strategy across the different discount types. 
    
    We notice a steep dip around Jun and July 2023 in both billed and original amounts. For the school's owners this could be interpreted as a large increase in student withdrawals,
    which raises their concern regarding the coverage of school's expenses during these months. However, from my experience, this is a normal and consistent trend during the summer time for 
    which may correlate with seasonal enrollment changes due to family travels. For the business owner, understanding these trends are crucial for financial planning, resource allocation,
    and re-evaluation of the current discounting strategy. Potential adjustments to tuition or discount policies may be considered to conpensate for revenue loss, especially during the 
    mid-year dips.  
    '''
    st.markdown(multi, unsafe_allow_html=True)
    
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
    
    # Figure 2
    st.markdown("""
    <h5 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>Figure (2) Line Charge (Plotly Express)</h5>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>AVERAGE PROGRAM BILLING BY MONTH</h4>
    """, unsafe_allow_html=True)
    
    df = read_original_data()
    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

    # Group by 'Program' and 'Date', then calculate the mean of 'Billing Amount'
    monthly_billing = df.groupby(['Program', pd.Grouper(key='Date', freq='M')])['Billing Amount'].mean().reset_index()

    # Create an interactive line plot using Plotly Express
    fig = px.line(monthly_billing, x='Date', y='Billing Amount', color='Program', 
                title='Program Billing Amount Over Months',
                labels={'Billing Amount': 'Average Billing Amount ($)', 'Date': 'Date'},
                markers=True)

    # Enhance the layout
    fig.update_layout(xaxis_title='Date',
                    yaxis_title='Average Billing Amount ($)',
                    xaxis_tickangle=-45,
                    xaxis=dict(tickformat='%b %Y'))  # Format x-axis tick labels to show abbreviated month and year

    # Show the plot in Streamlit
    st.plotly_chart(fig)

    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
    
    # Figure 3
    st.markdown("""
    <h5 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>Figure (3) Line & Clustered Column Chart (PowerBI)</h5>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>HISTORY OF Tuition CHARGES By Qurater</h4>
    """, unsafe_allow_html=True)
    # Use the st.write() function to display the iframe
    st.write(f'<iframe title="Revenue by Querter" width="1024" height="612" src="https://app.powerbi.com/view?r=eyJrIjoiOWYxZDI5ZmUtMGIzZi00NmQwLWFjZTMtZTdmZDllZjM3NWY0IiwidCI6IjcwZGUxOTkyLTA3YzYtNDgwZi1hMzE4LWExYWZjYmEwMzk4MyIsImMiOjN9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)  
    st.write("\n\n")
    st.subheader("Analysis")
    multi = '''
    Similar to Figure (1), this clusterd chart displays the same type of information in a different view by quarter. The main reason We included this graph is because we believe it provides 
    better visualization for the school's onwers to compare total revenues and understand the school's financial standing throughout the year. 
        '''
    st.markdown(multi, unsafe_allow_html=True)
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
    
    # Figure 4
    st.markdown("""
    <h5 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>Figure (4) Ribbon Chart (PowerBI)</h5>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>PROGRAM CONTRIBUTION TO REVENUE BY Schedule</h4>
    """, unsafe_allow_html=True)

    st.write("FD: Full Day (7:00 AM - 6:00 PM), SD: School Days (8:30 AM - 2:45 PM), HD: Half Days (8:30 AM - 12:00 PM)")
    # Use the st.write() function to display the iframe
    st.write(f'<iframe title="Program Schedules Revenue Contribution" width="1024" height="612" src="https://app.powerbi.com/view?r=eyJrIjoiNDkxYjVmNjQtYjRjYS00MDgyLWE1YmYtMDBlYzc2YTA0MTg1IiwidCI6IjcwZGUxOTkyLTA3YzYtNDgwZi1hMzE4LWExYWZjYmEwMzk4MyIsImMiOjN9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)  
    st.write("\n\n")
    st.subheader("Analysis")
    multi = '''
    Figure (4) expands on the information provided by the earlier graphs by adding Programs and Schedules as color marks, enabling the comparison of programs and schedules contributions 
    to revenue. 
        '''
    st.markdown(multi, unsafe_allow_html=True)
    
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
    
    # Figure 5
    st.markdown("""
    <h5 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>Figure (5) Treemap (PowerBI)</h5>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>DISCOUNT DISTRIBUTION Over Two School Years</h4>
    """, unsafe_allow_html=True)
    
    # Use the st.write() function to display the iframe
    st.write(f'<iframe title="Discount Amount by Discount Type" width="1024" height="612" src="https://app.powerbi.com/view?r=eyJrIjoiNGUxODNiMGUtNzk4ZS00YjM4LTlhYzktYjllYjRhOTAwNmNhIiwidCI6IjcwZGUxOTkyLTA3YzYtNDgwZi1hMzE4LWExYWZjYmEwMzk4MyIsImMiOjN9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)  
    st.write("\n\n")
    st.subheader("Analysis")
    multi = '''
    Figure (5) provides business owners with a closer look at the different discounts categories offered to families and deepening thier understanding of the gap difference between original 
    charges and billed amount. For example, by looking at the graph, we can see that Employee discount and Friends & Family discount show to be the highest discount rates offered both totalling
    to about $332K over two years. This is a huge amount and may need to be reevaluated. For example, the dataset shows that employees get a 100% discount on their children's tuition. While this 
    may help with the school's turnover rate by taking care of staff and showing them apprecaition, it is highly recommended that the school consisder an alternative offer, perhapse reducing the percetage 
    discount rate to compensate for some of the huge amout of employee discount. 
    
    Additionally, as much as it is important to revisit the discounting strategy and assess its sustainability as they significantly reduce revenue, business owners should know that discounts do also affect 
    student retention rate. Therefore, a well structured strategies that can balance between attractiveness to prospective and current families, and the financial viability of the institution, 
    are crucial for long-term success.
        '''
    st.markdown(multi, unsafe_allow_html=True)
    
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
    
    # Figure 6
    st.markdown("""
    <h5 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>Figure (6) BUBBLE CHART (Google Looker Studio)</h5>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>DISCOUNT DISTRIBUTION For Active Enrollments<br>Over Two Consecutive School Years (Aug 2022 - May 2024)</h4>
    """, unsafe_allow_html=True)

    # Use the st.write() function to display the iframe
    st.write(f'<iframe width="1024" height="612" src="https://lookerstudio.google.com/embed/reporting/3716267f-7edf-4b56-9f90-1ddb3630af02/page/z3GyD" frameborder="0" style="border:0" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"></iframe>', unsafe_allow_html=True)  
    st.write("\n\n")
    st.subheader("Analysis")
    multi = '''
    The chart illustrates the number of students receiving each type of discount and the cumulative amount of each. For example, consider the orange bubble, which represents sibling discounts. 
    Around 350 students receive this discount, indicating that their siblings are also enrolled in the school. The total discount for this category accumulates to approximately $1000. Similarly, 
    each bubble represents a different discount category, with the size of the bubble indicating the total discount offered for that category.

    This graph provides valuable information for financial administrators or school representatives. They can quickly assess whether adjustments are needed in their discount campaigns based on 
    this data.
        '''
    st.markdown(multi, unsafe_allow_html=True)
    
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")

    # Figure 7
    st.markdown("""
    <h5 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>Figure (7) Line Charge (Plotly Express)</h5>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>AVERAGE PROGRAM BILLING BY MONTH</h4>
    """, unsafe_allow_html=True)
    
    df = read_original_data()
    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

    # Group by 'Program' and 'Date', then calculate the mean of 'Billing Amount'
    monthly_billing = df.groupby(['Program', pd.Grouper(key='Date', freq='M')])['Billing Amount'].mean().reset_index()

    # Create an interactive line plot using Plotly Express
    fig = px.line(monthly_billing, x='Date', y='Billing Amount', color='Program', 
                title='Program Billing Amount Over Months',
                labels={'Billing Amount': 'Average Billing Amount ($)', 'Date': 'Date'},
                markers=True)

    # Enhance the layout
    fig.update_layout(xaxis_title='Date',
                    yaxis_title='Average Billing Amount ($)',
                    xaxis_tickangle=-45,
                    xaxis=dict(tickformat='%b %Y'))  # Format x-axis tick labels to show abbreviated month and year

    # Show the plot in Streamlit
    st.plotly_chart(fig)

    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")
       
    # Figure 8
    st.markdown("""
    <h5 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>Figure (8) Confusion Matrix (Seaborn)</h5>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>AVERAGE PROGRAM BILLING BY MONTH</h4>
    """, unsafe_allow_html=True)

    df = confusion_matrix_data(data=any)
    
    heatmap_data = df.pivot_table(index='Program', columns='Date', values='Billing Amount', aggfunc='mean')
    fig, ax = plt.subplots(figsize=(10.24, 6.12))  # You create a Matplotlib figure and axis
    sns.heatmap(heatmap_data, annot=True, fmt=".0f", linewidths=.5, cmap="YlGnBu", ax=ax)
    # Format the dates on the x-axis to be month abbreviations
    ax.set_xticklabels([pd.to_datetime(date).strftime('%b %Y') for date in heatmap_data.columns])
    # Set labels and title
    ax.set_title("Average Program Billing Amount By Month")
    ax.set_xlabel("Date")
    ax.set_ylabel("Program")
    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45)
    # Ensure the plot is tight and nothing is cut off
    plt.tight_layout()
    # Display the plot in the Streamlit app
    st.pyplot(fig)