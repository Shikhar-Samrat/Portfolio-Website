import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

image1 = Image.open("loan.jpeg")
image2 = Image.open("movie.png")
image3 = Image.open("pneumonia-detection.webp")
image4 = Image.open("analytics.png")

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About', 'Projects', 'Experience', 'Contact Info'],
        icons = ['person', 'code-slash', 'briefcase-fill','chat-left-text-fill'],
        orientation = 'horizontal'
    ) 

if selected == 'About':
    with st.container():
            st.subheader("Heyy there!! :smiley:")
            st.write("""
I'm Shikhar Samrat, currently a pre-final year undergraduate student at the prestigious Indian Institute of Technology (IIT) Kharagpur, majoring in Chemical Engineering.

Driven by a passion for exploring the intersection of technology and innovation, I've delved into the exciting realms of Data Science and Machine Learning. My journey has been particularly focused on Computer Vision, where I've discovered a profound interest and have dedicated my efforts to mastering this captivating field.

Beyond academia, I am a fervent believer in the power of hands-on learning and real-world applications. I thrive on challenges and am constantly seeking opportunities to apply my skills to solve practical problems.

I'm excited to share my journey and connect with like-minded individuals who share a passion for leveraging technology to drive meaningful change.
""")
    st.write("___")

    with st.container():
         col1,col2 = st.columns(2)
         with col1:
            st.subheader("""
            Education
            - IIT Kharagpur
                - Dual Degree in Chemical Engineering
                - Grade: 6.84
            - Central Public School (CBSE)
                - 90.8% in 12th
                - 95.8% in 10th
            """)
    with col2:
            st.subheader("""
            Relavant Coursework
               - Programming and Data Structures (C++)
               - Supervised Machine Learning Algorithms
               - Unsupervised Machine Learning Algorithms
               - Probability and Statistics
               - Deep Learning Algorithms
               - Computer Vision
            """)

if selected == 'Projects':
     with st.container():
          st.write('#')
          col3, col4 = st.columns((3,4))
          with col3:
               st.image(image1)
          with col4:
               st.subheader("Loan eligibility prediction (Web App)")
               st.markdown("[Visit Web App](https://loanmlwebapp-c9omor2mwaamnhiswccev3.streamlit.app/)")
          st.markdown("***")
          col5, col6 = st.columns((3,4))
          with col5:
               st.image(image2)
          with col6:
               st.subheader("Movie recommender system (Content based filtering)")
               st.markdown("[Visit Github repo](https://github.com/Shikhar-Samrat/Data-Science-Projects/tree/Movie-Recommender-System)")
          st.markdown("***")
          col7, col8 = st.columns((3,4))
          with col7:
               st.image(image3)
          with col8:
               st.subheader("Pneumonia Detection (Using chest X-ray)") 
               st.markdown("[Visit Github repo](https://github.com/Shikhar-Samrat/Data-Science-Projects/tree/Pneumonia-Detection-Chest-X-ray)")   
          st.markdown("***")
          col9, col10 = st.columns((3,4))
          with col9:
               st.image(image4)
          with col10:
               st.subheader("Agriculture Crop Analysis (Bihar)")
               st.markdown("[Visit Github repo](https://github.com/Shikhar-Samrat/Data-Science-Projects/tree/Agriculture-Production-Analysis)")
        
if selected == 'Experience':
     with st.container():
          st.subheader("""
        Python research intern |  Advisor : Dr. Salman Ali, IIM Kozhikode
          - Extracted and cleaned Amazon video games JSON file.
          - Transformed the cleaned data into a structured CSV file
          """)
          st.subheader("""
        Accenture North America Data Analytics and Visualization Job Simulation on Forage - January 2024


 * Completed a simulation focused on advising a hypothetical social media client
   as a Data Analyst at Accenture
 * Cleaned, modelled and analyzed 7 datasets to uncover insights into content
   trends to inform strategic decisions
 * Prepared a PowerPoint deck and video presentation to communicate key insights
   for the client and internal stakeholders
          """)

if selected == 'Contact Info':
     st.write("##")
     st.subheader("Email ID : shikharsamrat22@gmail.com")
     st.subheader("Phone no : 6205324328")
     st.subheader("Linkedin : https://www.linkedin.com/in/s-sam-1a4913226/")
     st.subheader("Github : https://github.com/Shikhar-Samrat")
