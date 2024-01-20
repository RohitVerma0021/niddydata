import streamlit as st
import base64

def main():
    st.set_page_config(
        page_title="niddydata",
        layout='wide',
        page_icon="®️",
    )
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
        st.markdown("• Master of Science, Data Science (SGPA: <span style='color: red;'>7.17</span>)",unsafe_allow_html=True)
        st.write("  Post Graduation Date: May 2023")
        st.markdown("• Bachelor of Science, Computer Science (SGPA: <span style='color: red;'> 6.8</span>)",unsafe_allow_html=True)
        st.write("  Graduation Date: Sep 2021")



        # Social activity section
        st.markdown("<h2 style='color: blue;'>Social Activity</h2>", unsafe_allow_html=True)
        st.write(
            "During my time at Devi Ahilya Vishwavidvalaya, I was involved in event organization and various social activities.")

# contect infomation

        st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css">
        """, unsafe_allow_html=True)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        st.markdown("""
            <div style="text-align: center;">
                <h2 style="color: purple;">Get in Touch</h2>
                <p>Feel free to connect with me via the following channels:</p>
        """, unsafe_allow_html=True)
        first,second,third = st.columns(3)
        with first:
            st.markdown(
                "[![Email](https://img.shields.io/badge/Email-rohitverma-red?style=for-the-badge&logo=gmail)](mailto:rohitvermav0021@gmail.com)")
        with second:
            st.markdown(
                "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rohit%20Verma-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/rohit-verma-3094b8224/)")

        with third:
            st.markdown(
                "[![GitHub](https://img.shields.io/badge/GitHub-RohitVerma0021-black?style=for-the-badge&logo=github)](https://github.com/RohitVerma0021)")




    #=================================================================================================
    elif page == "Skills":
        skill1, skill2 = st.columns(2)

        with skill1:
            st.header("Data Science Skills")
            st.markdown(
                """
                <div style="font-size: 18px; color: #2C3E50; font-weight: bold;">Key Data Science Skills:</div>
                <ul style="list-style-type: none; padding-left: 0;">
                    <li style="margin-bottom: 15px;">
                        <b>Python:</b> Proficient in Python programming for data analysis, machine learning, and scripting.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>R:</b> Knowledge of R programming for statistical analysis and data visualization.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>NumPy:</b> Used for numerical operations and efficient array manipulations in Python.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>Pandas:</b> Expertise in data manipulation, analysis, and cleaning using the Pandas library.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>Matplotlib:</b> Created static, animated, and interactive visualizations with Matplotlib.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>Seaborn:</b> Employed for statistical data visualization, enhancing Matplotlib plots.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>Plotly:</b> Developed interactive and dynamic visualizations with Plotly in Python.
                    </li>
                </ul>
                """, unsafe_allow_html=True
                )

            st.markdown(
                    """
                <div style="font-size: 18px; color: #2C3E50; font-weight: bold;">Advance Skills:</div>
                <ul style="list-style-type: none; padding-left: 0;">
                    <li style="margin-bottom: 15px;">
                    <ul style="list-style-type: none; padding-left: 0;">
                        <li style="margin-bottom: 15px;">
                            <b>Machine Learning:</b> Implemented machine learning algorithms for predictive modeling.
                        </li>
                        <li style="margin-bottom: 15px;">
                            <b>Scikit-Learn:</b> Utilized for machine learning tasks, including classification and regression.
                        </li>
                        <li style="margin-bottom: 15px;">
                            <b>TensorFlow:</b> Developed deep learning models for complex tasks using TensorFlow.
                        </li>
                        <li style="margin-bottom: 15px;">
                            <b>PyTorch:</b> Applied for deep learning and neural network implementations.
                        </li>
                        <li style="margin-bottom: 15px;">
                            <b>Natural Language Processing (NLP):</b> Applied NLP techniques for text analysis and processing.
                        </li>
                        <li style="margin-bottom: 15px;">
                            <b>Feature Engineering:</b> Created meaningful features to improve model performance.
                        </li>
                        <li style="margin-bottom: 15px;">
                            <b>Model Evaluation and Hyperparameter Tuning:</b> Employed techniques to optimize model performance.
                        </li>
                    </ul>
                    """, unsafe_allow_html=True
                )


            st.markdown(
                """
                <div style="font-size: 18px; color: #2C3E50; font-weight: bold;">Additional Skills:</div>
                <ul style="list-style-type: none; padding-left: 0;">
                    <li style="margin-bottom: 15px;">
                        <b>Database Management:</b> Skills in managing and optimizing databases for efficient data handling.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>SQL:</b> Proficient in writing SQL queries for data retrieval and manipulation.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>Big Data Technologies:</b> Familiarity with tools like Hadoop and Spark for processing large datasets.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>Data Cleaning and Preprocessing:</b> Ensured data quality through cleaning and preprocessing techniques.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>Data Visualization:</b> Designed compelling visualizations to communicate complex data.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>Statistical Analysis:</b> Applied statistical methods for hypothesis testing and data analysis.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>Git and Version Control:</b> Used Git for version control and collaboration on projects.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>Power BI and Tableau:</b> Created interactive dashboards and reports for data visualization.
                    </li>
                </ul>
                """, unsafe_allow_html=True
            )

        with skill2:
            st.markdown(
                """
                <div style="font-size: 18px; color: #2C3E50; font-weight: bold;">Soft Skills:</div>
                <ul style="list-style-type: none; padding-left: 0;">
                    <li style="margin-bottom: 15px;">
                        <b>Communication:</b> Clear and effective communication to convey complex data concepts to diverse audiences.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>Mentorship:</b> Experience in mentoring aspiring data scientists, providing guidance and support.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>Leadership:</b> Demonstrated leadership skills in guiding data science projects and teams.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>Problem-Solving:</b> Strong analytical and problem-solving abilities to address complex data challenges.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>Adaptability:</b> Ability to adapt to new technologies and methodologies in a dynamic data science landscape.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>Collaboration:</b> Collaborative mindset, working effectively within cross-functional teams.
                    </li>
                    <li style="margin-bottom: 15px;">
                        <b>Community Building:</b> Founded and led the Needata community, fostering knowledge sharing and collaboration.
                    </li>
                </ul>
                """, unsafe_allow_html=True
            )

    elif page == "Projects":
        p1,p2=st.columns(2)
        with p1:
            st.header("Projects")
            st.write("Check out some of my projects:")
        with p2:
            st.write(" https://ipl-win-probability-predictor-niddydata0021.streamlit.app/?embed_options=dark_theme ")
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


