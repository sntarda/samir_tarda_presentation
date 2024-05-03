def main(st, iframe_style):
    iframe_style = {iframe_style}
    
    st.markdown("""
    <h1 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>Active Enrollment Distribution</h1>
    """, unsafe_allow_html=True)
    st.write("-----------------------------")
    
    # Figure 1
    st.markdown("""
    <h5 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>Figure (1) Pi Chart & Table Matrix (PowerBI)</h5>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>STUDENT COUNTS DISTRIBUTION BY PROGRAM AND SCHEDULE</h4>
    """, unsafe_allow_html=True)
    
    st.write("FD: Full Day (7:00 AM - 6:00 PM), SD: School Days (8:30 AM - 2:45 PM), HD: Half Days (8:30 AM - 12:00 PM)")
    # Use the st.write() function to display the iframe
    st.write(f'<iframe title="Students Counts by Program" width="1024" height="612" src="https://app.powerbi.com/view?r=eyJrIjoiMjk2NjhhOGYtYzE1NS00ZjBkLWFkZWQtZmJjMGZiMDU3YzdkIiwidCI6IjcwZGUxOTkyLTA3YzYtNDgwZi1hMzE4LWExYWZjYmEwMzk4MyIsImMiOjN9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)  
    st.write("\n\n")
    st.subheader("Analysis")
    multi = '''
    This pie chart that represents the distribution of student counts by program and schedule and different colors denote various 
    programs such as Primary, Toddler, Lower Elementary, Infant, and Upper Elementary, with corresponding active student counts and percentages.
    The small table next to the pie chart breaks down these numbers further by schedule type: Half Days (5HD), School Days (5SD), and Full Days (FD).
    
    - <strong>IMPORTANCE:</strong>
    This graphs provides essential information for understanding the composition of the student body across different programs and schedules. It summarizes 
    invaluable insights about the school's program levels with the number of student counts in each program and program schedule. 
    
    Figure (1) show that the Primary program has the largest enrollment, with the majority of students (48) enrolled in the Full Day schedule, 
    indicating a high demand for extended care. We can see that the Toddlers program also predominantly participate in the Full Day program. On the other hand, although the table reveals that
    the Elementary programs have more balanced distribution, the Full Day scheudle still appears to have slightly higher enrollment. 
    
    It is also worth noting that the 5HD schedule is only offered for the Primary and Toddlers Program. Therefore, the missing values of this schedule for the Infant and Elementary Programs doesn't 
    indicates anything. However, lower or missing values for the 5HD schedule in Primary and Toddlers should raise a question mark for school's owner and further investigation into the reason
    of decreased enrollment should be considered.
    '''
    st.markdown(multi, unsafe_allow_html=True)
    
    # Divider
    st.image('top_data-science-divider-1.png',  width=1024, output_format='auto')
    st.write("\n\n")

    # Figure 2
    st.markdown("""
    <h5 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>Figure (1) Bar Chart & Stacked Bar Chart (Tableau)</h5>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h4 style='text-align: left; font-weight: bold; color: #204760; margin-bottom: -10px;'>ACTIVE STUDENTS DASHBOARD</h4>
    """, unsafe_allow_html=True)

    st.write("FD: Full Day (7:00 AM - 6:00 PM), SD: School Days (8:30 AM - 2:45 PM), HD: Half Days (8:30 AM - 12:00 PM)")
    # Correctly embedding the Tableau visualization
    st.write(f'<iframe src="https://prod-useast-b.online.tableau.com/t/samirtarda707500432c/views/Dashboard/Dashboard1?:embed=y&:display_count=yes&:showVizHome=no" width="1024" height="825"></iframe>', unsafe_allow_html=True)
    st.write("\n\n")
    st.subheader("Analysis")
    multi = '''
    This Tableau dashboard features multiple graphs related to the active student population. Again, Figure (2) does reveal the same type of information as Figure (1) above 
    with a more enhanced and feautred visualization, assessing program popularity, scheduling preferences, and classroom utilization.
    
    Users can utilize this dashboard to view and analyze each individual program at a time reducing any confusion resulting from viewing too many numbers at once, and enabling a clearer understanding of specific trends and 
    patterns within the data.
    
    Figure (1) and (2) both show that the primary program appears to be the most popular, particulary for Full Day schedules. This may indicate that there is a strong demand on daycare 
    in this age group within the community.  
    
    For school management, the dashboard can be very useful for monitoring and optimizing classrooms untilization, staffing, and resources allocations. Additionally, 
    for the owner, program distributions suggest potential growth opportunities in the Primary and Toddler programs and the need to evaluate the marketing and appeal of the Elementary programs.  
    '''
    st.markdown(multi, unsafe_allow_html=True)
    
