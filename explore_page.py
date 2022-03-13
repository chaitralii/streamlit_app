import streamlit as st
# import seaborn as sns
import numpy as np
import pandas as pd
import plotly.figure_factory as ff

import requests
from bs4 import BeautifulSoup


import matplotlib.pyplot as plt

import plotly.express as px
import plotly.graph_objs as go


#cases_pune = pickle.load(open('pune.pkl', 'rb'))
response = requests.get("https://coronaclusters.in/maharashtra/pune")
print(response.status_code)



def load_data():

    df = pd.read_csv('http://www.cessi.in/coronavirus/images/model_output/pmc_1.csv')
    Date = df['Date'].str.split('.', expand=True)
    Date.columns = ['Day', 'Month', 'Year']
    df = pd.concat([df, Date], axis=1)
    df.fillna(0)
    df['Month']= df['Month'].replace(['1','2','3','4','5','6','7','8','9','10','11','12'],['Jan','Feb','March','April','May','June','July','August','Sept','Oct','Nov','Dec'])
    months_categories = ["Jan", "Feb", "March", "April", "May", "June", "July", "August", "Sept","Oct","Nov","Dec"]
    df["Month"] = pd.Categorical(df["Month"], categories=months_categories)
    df.sort_values(by="Month")
    #df['Month'].sort_values(asc)
    #df = df.sort_values(by='Month',ascending=True,inplace=True)
    #df['month']= pd.DatetimeIndex(pd.to_datetime(df['Month'],format='%b')).month
    #df = df.set_index('month').sort_index()
    df = df.groupby('Month')[['dailyconfirmed', 'dailyrecovered', 'dailydeceased']].sum()
    df.reset_index(level=0,inplace=True)


    return df



# def live_data():
#     url = "https://coronaclusters.in/maharashtra/pune"
#
#     page = requests.get(url)
#     print(page.content)

    # soup = BeautifulSoup(page.content, 'html.parser')

    # confirm_cases_live = soup.findAll(attrs={'class': 'card-title text-md text-md-lg'})
    # confirm_cases_live = confirm_cases_live[0].text.replace('<h5 class="card-title text-md text-md-lg">', " ")
    # print(confirm_cases_live)

    # recovered_cases_live = soup.findAll(attrs={'class': 'card-title text-md text-md-lg'})
    # recovered_cases_live = recovered_cases_live[1].text.replace('<h5 class="card-title text-md text-md-lg">', " ")
    # print(recovered_cases_live)

    # death_cases_live = soup.findAll(attrs={'class': 'card-title text-md text-md-lg'})
    # death_cases_live = death_cases_live[3].text.replace('<h5 class="card-title text-md text-md-lg">', " ")
    # print(death_cases_live)
    # st.title("LIVE COVID-19 CASES IN PUNE")





    # x = int(confirm_cases_live)
    # y = int(recovered_cases_live)
    # z = int(death_cases_live)

    # col1, col2, col3 = st.columns(3)
    # col1.metric("CONFIRMED CASES", value=x )
    # col2.metric("RECOVERED CASES",value=y)
    # col3.metric("DECEASED CASES",value=z)
    #
    # df = pd.DataFrame([["Covid Status", x, y, z]],
    #                   columns=["Status", "Confirmed", "Recovered", "Deceased"])
    # fig = px.bar(df, x="Status", y=["Confirmed", "Recovered", "Deceased"], barmode='group', height=400)
    # st.dataframe(df) # if need to display dataframe
    # st.plotly_chart(fig)

    # from PIL import Image
    # image = (href='https://www.google.com/url?sa=i&url=https%3A%2F%2Fswachhindia.ndtv.com%2Fsince-coronavirus-induced-lockdown-pune-based-ngo-has-supported-6-lakh-people-with-ration-and-hygiene-kit-52586%2F&psig=AOvVaw10x5YvfCwIXUkiA6yPgIzh&ust=1640113767697000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPCQ3vSJ8_QCFQAAAAAdAAAAABAP')






    return


def show_explore_page():

    # print(live_data())
    # chart_data = live_data(columns)

    # st.area_chart(data=, use_container_width=True)

    data_new = load_data()

    # st.write(data_new)
    st.title("Covid 19 Data Analysis For Pune District")
    st.image('https://bchc.org.au/wp-content/uploads/2020/12/corona-banner.jpg', width=700)
    st.markdown(
        "Pune is one of the highly populated cities of Maharastra -- an Indian state which is the most affected by COVID19. Here are some of the crucial plots which might be helpful in assessing the current scenario of COVI19 progression in Maharastra and Pune. It is important to note that the dataset used for the analysis of the state-wide (Maharastra) and city-wide (Pune) progression of COVID19 are obtained from two different sources. The database used for generating the plots can be downloaded here. The line breaks in the plots indicate data gap.")
    st.markdown("Below Bar graph plots the monthly status of cases in Pune.")
    options = data_new.columns.tolist()
    select = st.selectbox('select status', options, )
    s = data_new[select]
    # covid= covid[covid['Month'].isin()]#
    trace = go.Bar(x=data_new['Month'], y=s, marker_color='#E3634D')
    data = [trace]
    fig = go.Figure(data=data)
    st.plotly_chart(fig)
    st.markdown(
        " The Bar graph shows trend in monthly confirmed,recovered and deceased covid cases for the year 2021, dated 1 January 2021 to 3 days rolling data.  ")
    st.subheader("Visualising monthly status of Covid 19 cases in Pune using Scatter Plot.Select status for analysis.")
    st.markdown(" ")
    # scatterplt
    option_sct = data_new.columns.tolist()
    select_sct = st.selectbox('select the status to plot scatter plot', option_sct)
    p = data_new[select_sct]
    fig_sct = px.scatter(data_frame=data_new, x='Month', y=p, color=p, width=800, height=500)
    fig_sct.update_traces(marker_size=15)
    # fig_sct.update_layout(margin=dict(l=0.5,r=0.5,t=5,b=5),paper_bgcolor ="LightSteelBlue")
    st.write(fig_sct)
    # last 10 days data:
    st.header("Insight of last 10 Days covid 19 Data (3 Days rolling data) ")
    st.markdown("Previously the plots discribed monthly trends in Covid data."
                "The further graphs depict the variation in Covid 19 Confirmed,Recovered and deceased cases from last 10 days of 3 Days rolling data."
                "Trend in Covid Confirmed Cases:(3 days rolling data)")
    # line chart
    df = pd.read_csv('http://www.cessi.in/coronavirus/images/model_output/pmc_1.csv')
    data_last = df.tail(10)
    # st.write(data_last)
    fig_line1 = px.line(data_last, x='Date', y='dailyconfirmed', width=700, height=450,
                        title='Covid 19 Confirmed cases- Last 10 Days (3 days rolling data)', markers='o')
    st.plotly_chart(fig_line1)
    st.subheader("Trend in Covid Recovered Cases :(3 days rolling data)")
    fig_line2 = px.line(data_last, x='Date', y='dailyrecovered', width=700, height=450,
                        title='Covid 19 Recovered cases- Last 10 Days (3 days rolling data)', markers='o')
    st.plotly_chart(fig_line2)
    st.subheader("Trend in Covid Deceased Cases :(3 days rolling data)")
    fig_line3 = px.line(data_last, x='Date', y='dailydeceased', width=700, height=450,
                        title='Covid 19 Deceased cases- Last 10 Days (3 days rolling data)', markers='o')
    st.plotly_chart(fig_line3)
    return








