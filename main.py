import streamlit as st
from explore_page import show_explore_page
from predict_page import run




def show_app_page():


    #st.image('')
    st.markdown("""# What Is Coronavirus? """)
    st.write("Coronaviruses are a type of virus. There are many different kinds, and some cause disease. A coronavirus identified in 2019, SARS-CoV-2, has caused a pandemic of respiratory illness, called COVID-19.")
    st.subheader(""":exclamation:COVID-19 """)
    col1,mid,col2 = st.columns([2,1,3])
    with col1:
        st.image('https://thumbor.forbes.com/thumbor/fit-in/1200x0/filters%3Aformat%28jpg%29/https%3A%2F%2Fspecials-images.forbesimg.com%2Fimageserve%2F5f62861e8470f68876063111%2F0x0.jpg',width=350)
    with col2:
        st.write("""COVID-19 is the disease caused by SARS-CoV-2, the coronavirus that emerged in December 2019.
COVID-19 can be severe, and has caused millions of deaths around the world as well as lasting health problems in some who have survived the illness.
The coronavirus can be spread from person to person. It is diagnosed with a laboratory test.
COVID-19 vaccines have been authorized for emergency use by the U.S. Food and Drug Administration, and vaccination programs are in progress across the U.S. and in many parts of the world.
Prevention involves physical distancing, mask-wearing, hand hygiene and staying away from others if you feel sick.""")
    st.video('https://youtu.be/i0ZabxXmH4Y')
    st.markdown("""# How does the Coronavirus spread ?""")
    st.write("As of now, researchers know that the coronavirus is spread through droplets and virus particles released into the air when an infected person breathes, talks, laughs, sings, coughs or sneezes. Larger droplets may fall to the ground in a few seconds, but tiny infectious particles can linger in the air and accumulate in indoor places, especially where many people are gathered and there is poor ventilation. This is why mask-wearing, hand hygiene and physical distancing are essential to preventing COVID-19.")
    st.markdown(" # How did the coronavirus start?")
    st.write("The first case of COVID-19 was reported Dec. 1, 2019, and the cause was a then-new coronavirus later named SARS-CoV-2. SARS-CoV-2 may have originated in an animal and changed (mutated) so it could cause illness in humans. In the past, several infectious disease outbreaks have been traced to viruses originating in birds, pigs, bats and other animals that mutated to become dangerous to humans. Research continues, and more study may reveal how and why the coronavirus evolved to cause pandemic disease.")
    st.markdown("# What are symptoms of coronavirus?")
    st.write(":white_small_square: Cough ")
    st.write(":white_small_square: Fever or chills")
    st.write(":white_small_square: Shortness of breath or difficulty breathing")
    st.write(":white_small_square: Headache")
    st.write(":white_small_square: New fatigue")
    st.write(":white_small_square: Congestion or runny nose")
    st.write("Some people infected with the coronavirus have mild COVID-19 illness, and others have no symptoms at all. In some cases, however, COVID-19 can lead to respiratory failure, lasting lung and heart muscle damage, nervous system problems, kidney failure or death.")
    st.image('https://st3.depositphotos.com/3256961/35685/v/1600/depositphotos_356857062-stock-illustration-covid-coronavirus-infographic-vector-illustration.jpg')
    st.video('https://www.youtube.com/watch?v=oqFn6AHoJZQ')
    st.markdown("# How is COVID-19 treated?")
    st.write("Treatment for COVID-19 addresses the signs and symptoms of the infection and supports people with more severe disease. For mild cases of coronavirus disease, your doctor may recommend measures such as fever reducers or over-the-counter medications. More severe cases may require hospital care, where a patient may receive a combination of treatments that could include steroids, oxygen, mechanical breathing support and other COVID-19 treatments in development. Infusions of monoclonal antibodies given to certain patients early in the infection may reduce the symptoms, severity and duration of the illness.")



    return
page = st.sidebar.selectbox("Explore Or Predict",("Covid-19", "Predict", "Explore"))

if page == "Predict":
    run()
elif page == "Explore":
    show_explore_page()
else:
    show_app_page()

