import streamlit as st
import base64

def main():
    st.set_page_config(page_title="niddydata", layout='wide')
    cu1,cu2=st.columns(2)
    with cu1:
        st.markdown("# Hello👨🏻‍💻, I am Rohit")
    with cu2:
        st.image("neww.png",width=420)
    page = st.sidebar.radio("Select a page:", ["Home", "About Me", "Skills", "Projects","Syllabus"])
    if page == "Home":
            st.write("Hello, my name is Rohit Verma, and I am a highly skilled and motivated professional in the field of Data Science and Analytics. I have a strong passion for using data to uncover valuable insights. I am currently based in Indore.")

            st.write("I have successfully completed my Master's degree in Data Science and Analytics, which has allowed me to refine my expertise in various areas of data management and analysis.")

            st.write("Throughout my academic and professional journey, I have been involved in a wide range of projects, both as an individual contributor and as part of a team. I take pride in effectively deploying these projects on cloud platforms, ensuring that they are accessible and scalable for users.")
            st.write("My dedication to data science and analytics drives me to continuously seek innovative solutions and contribute to the ever-evolving field.")


            st.markdown("<h3 style='color: red;'>Experience</h3>", unsafe_allow_html=True)
            col1ex,col2ex,col3ex=st.columns(3)
            with col1ex:
                st.markdown(
            '<span style="color:orange">MasterDexter</span>',
            unsafe_allow_html=True)
                st.write("Junior Data Analyst | Mar 2022 – Dec 2022")
                st.write("- Excelled at gathering, validating, and organizing diverse data sources to ensure quality and integrity.")
                st.markdown("- Proficient in data cleaning, manipulation, visualization, and collaborated with senior analysts for statistical modeling and data quality solutions.")
        # Dropdown menus for blogs and projects side by side
            with col2ex:
                st.markdown(
            '<span style="color:orange">HemanshAI</span>',
            unsafe_allow_html=True)
                st.write("Business Analyst intern | Jan 2023 – May 2022")
                st.write("As a Business Analyst Intern, I actively gathered stakeholder requirements, analyzed customer needs, and meticulously documented my work, resulting in effective decision making and actionable insights.")
            with col3ex:
                st.markdown(
            '<span style="color:orange">Protonshub</span>',
            unsafe_allow_html=True)
                st.write(" Business Analyst | May 2022 - Present")
                st.write("As a Business Analyst intern, I engaged stakeholders, gathered requirements, provided project updates, analyzed needs/specifications, and contributed valuable insights for informed decision-making through documentation and analysis")

# ------------------------------------------------------------------------------------------------------
    blog='''Data analytics is indeed a powerful tool that brings valuable insights and transformative changes to every industry. With Streamlit's ease-of-use and interactivity, organizations can unlock the full potential of their data, 
    leading to smarter decisions and a competitive edge in the market. By harnessing the power of data analytics through Streamlit web apps, businesses can stay at the forefront of innovation and thrive in today's data-driven world.'''
#---------------------------------------------------------------------------------------------------------
    # Other sections in the sidebar for navigation
    # page = st.sidebar.selectbox("Select a page:", ["Home", "About Me", "Skills", "Projects"])

    if page == "About Me":
        st.markdown("<h1 style='color: red;'>About Me - Gaming, Sports, Movies, and Learning!</h1>",
                    unsafe_allow_html=True)

        # Introduction
        st.write(
            "Hey there! Welcome to my about page. I'm a passionate individual who loves exploring various interests and learning new things. Here's a little bit about me:")

        # Interests section
        st.markdown("<h2 style='color: orange;'>Interests</h2>", unsafe_allow_html=True)
        st.write(
            "I have a diverse set of interests that keep me engaged and entertained. Some of my top interests include:")
        st.write("- Gaming: I absolutely love playing video games and exploring different virtual worlds.")
        st.write("- Sports: I am an avid runner, and I also enjoy working out at the gym to stay fit and active.")
        st.write("- Movies: Watching movies is one of my favorite pastimes, and I enjoy various genres.")
        st.write(
            "- Learning: In my free time, I like to work on my skills and acquire new knowledge in different areas.")

        # Education section
        st.markdown("<h2 style='color: green;'>Education</h2>", unsafe_allow_html=True)
        st.write("I pursued my education at Devi Ahilya University in Indore, M.P.")
        st.write("• Master of Science, Data Science (SGPA: 7.17)")
        st.write("  Post Graduation Date: May 2023")
        st.write("• Bachelor of Science, Computer Science (SGPA: 6.8)")
        st.write("  Graduation Date: Sep 2021")

        # Social activity section
        st.markdown("<h2 style='color: blue;'>Social Activity</h2>", unsafe_allow_html=True)
        st.write(
            "During my time at Devi Ahilya Vishwavidvalaya, I was involved in event organization and various social activities.")

        # Contact information
        st.markdown("<h2 style='color: purple;'>Get in Touch</h2>", unsafe_allow_html=True)
        st.write("Feel free to connect with me via the following channels:")
        st.write("- Email: your.email@example.com")
        st.write("- LinkedIn: [Your LinkedIn Profile URL]")
        st.write("- GitHub: [Your GitHub Profile URL]")
    elif page == "Skills":
        skill1,skill2=st.columns(2)
        with skill1:
            st.header("Skills")
            st.write("Here are some of my key skills:")
            st.write("- Python")
            st.write("- MySQL")
            st.write("- Database Managment")
            st.write("- Machine Learning")
            st.write("- Statistics")
            st.write("- Natrual Language Processing")
            st.write("- Power BI")
            st.write("- Tableau")
            st.write("- Web Scrapping")
            st.write("- Data Analytics")
            st.write("- Data Visualization")
            st.write("- NumPy")
            st.write("- Pandas")
            st.write("- Plotly")
            # Add more skills as needed
        with skill2:
            st.write("## **how it works and its show time**")
            new1,new2=st.columns(2)
            with new1:
                st.write("## This is my and second columns")
            with new2:
                st.write("## now it show time")

    elif page == "Projects":
        p1,p2=st.columns(2)
        with p1:
            st.markdown("[](https://ipl-win-probability-predictor-niddydata0021.streamlit.app/?embed_options=dark_theme)")
            st.header("Projects")
            st.write("Check out some of my projects:")
            st.write("- Project 1")
            st.write("- Project 2")
            st.write("- Project 3")
        # Add more projects as needed



#------------------------------------------------------------------------------------------------------------------
    elif page == "Syllabus":
        sy1,sy2,sy3=st.columns(3)
        with sy3:
            st.markdown("hello how are you can we show the any thing is else")
        with sy2:
            st.write("hello world how are you can we solve the problem")
        with sy2:
            def show_pdf(file_path):
                with open(file_path, "rb") as f:
                    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="250" height="200"></iframe>'
                    st.markdown(pdf_display, unsafe_allow_html=True)

            show_pdf("syllabus.pdf")



#------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()


