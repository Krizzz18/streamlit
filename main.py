import streamlit as st
from streamlit_option_menu import option_menu

# st.title("Idhu title uh")
# st.header("Idhu dhan Header📄🖍️o(≧o≦)o🧸")
# st.subheader("SUbheader𒅒𒈔𒅒𒇫𒄆")
# st.write("# WRite is for paragraph")
# st.write("_WRite is for paragraph_")
# st.write("## WRite is for paragraph")
# st.write("- WRite is for paragraph")
# st.text("Text")
# st.code("""
# #include <stdio.h>

# int main() {
#   printf("Hello World!");
#   return 0;
# }

# """, language="c")
# st.latex(r"y=mx+b")
# st.metric(label="temparature",value="75℃",delta="-1.2℉")
# st.progress(0.5,text="50%")
# st.progress(0.75,text="75%")
# st.text_input("Enter something : ")
# st.date_input("Enter your date of birth : ")
# st.number_input("Enter your age : ")
# st.radio("Enter your gender : ",{"Male","Female","Other"})
# st.checkbox("I agree")
# st.multiselect("Interests",["Watching Movies","Songs"])
# st.slider(label="Select your age : ",min_value=0,max_value=100,value=25)

with st.sidebar:
    st.title("Annamalai president")
    st.text_input("name")

    select =option_menu(
        menu_title="Internship",
        options = ['Home','About','Service','Exit'],
        icons = ['house-door','file-person-fill','gear-fill','box-arrow-left']
    )

if select == "Home":
    st.title("Vanakkam 🙏")
    st.text_input("Name")
    st.text_input("Username")
    st.divider()
    col1,col2,col3 = st.columns(3)
    with col1:
        a = st.text_input("About")
        print(a)
        if st.button("Click"):
            st.write(a)
            st.balloons()
    with col2:
        st.text_input("Email")
        st.image(r"nvkXseeman.png")
    with col3:
        st.text_input("Address")
        st.video("D:\SK\Internship\Post Malone, Swae Lee - Sunflower (Spider-Man_ Into the Spider-Verse).mp4")
elif select == "About":
    st.title("Welcome to About page")
elif select == "Service":
    st.title("Welcome to Service page")
elif select == "Exit":
    st.title("Exit from  the page")
