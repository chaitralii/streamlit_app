import warnings
import streamlit as st
import matplotlib
from jedi.api.refactoring import inline

warnings.filterwarnings('ignore')
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# %matplotlib inline
from scipy.stats import *
import matplotlib.pyplot as plt  # Matlab-style plotting
import seaborn as sns # informative statistical graphics.
import statsmodels.api as sm #for ARIMA and SARIMAX
import datetime
from datetime import timedelta


sns.set_style('darkgrid')

def show_cases():
    train = pd.read_csv('http://www.cessi.in/coronavirus/images/model_output/pmc_1.csv')
    # print(train.tail())

    train = train.drop(
        ['ventilatorpatients', 'totalhousesurvey', 'housescovered', 'flu', 'populationcovered', 'dailysamples',
         'dailydeceased', 'totalcritical', 'totalcritical', 'totalsamples', 'totalconfirmed', 'dailyrecovered',
         'totalhospital', 'totalrecovered', 'totaldeceased', 'active_home', 'active_hosp'], axis=1)
    # print(train)

    train_df = train
    train_df['Date'] = pd.to_datetime(train_df['Date'])
    # print(train_df.tail())

    train_df = train_df.set_index('Date')
    train_df['dailyconfirmed'] = train_df['dailyconfirmed'].astype(float)

    # print(train_df.head())

    from statsmodels.tsa.stattools import adfuller  # adfuller stands for Augmented Dickey-Fuller unit root test.

    # The function find mean and standard deviation of the series and and performs augmented dickey fuller test.
    # returns pvale .. The samaller the pvalue more stationary is the series.

    def test_stationarity(timeseries, window=15, cutoff=0.01):
        rolmean = timeseries.rolling(window).mean()
        rolstd = timeseries.rolling(window).std()
        fig = plt.figure(figsize=(12, 8))
        orig = plt.plot(timeseries, color='blue', label='Original')
        mean = plt.plot(rolmean, color='red', label='Rolling Mean')
        std = plt.plot(rolstd, color='black', label='Rolling Std')
        plt.legend(loc='best')
        plt.title('Rolling Mean & Standard Deviation')
        plt.show()

        # print('Results of Dickey-Fuller Test:')
        dftest = adfuller(timeseries, autolag='AIC', )
        dfoutput = pd.Series(dftest[0:4],
                             index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
        for key, value in dftest[4].items():
            dfoutput['Critical Value (%s)' % key] = value
        pvalue = dftest[1]
        if pvalue < cutoff:
             print('p-value = %.4f. The series is likely stationary.' % pvalue)
        else:
             print('p-value = %.4f. The series is likely non-stationary.' % pvalue)

        # print(dfoutput)

    # print(test_stationarity(train_df['dailyconfirmed']))

    # we can see a recurring correlation exists in both ACF and PACF hece we should choose SARIMAX model which also deals with seasonality

    # RULE : A model with no orders of differencing assumes that the original series is stationary (mean-reverting). A model with one order of differencing assumes that
    # the original series has a constant average trend (e.g. a random walk or SES-type model, with or without growth). A model with two orders of total differencing assumes that
    # the original series has a time-varying trend

    # Since our series has a contant average trend ( with growth ) we would take I = 1 and MA = 0 ( I-1 ).

    sarimax_mod = sm.tsa.statespace.SARIMAX(train_df.dailyconfirmed, trend='n', order=(7, 0, 1)).fit()
    # print(sarimax_mod.summary())

    last_row = train_df.index[-1]
    last_row

    # Now lets predict using out model.
    # today = datetime.date.today()

    start_index = '1.1.2021'
    # end_index = today.strftime("%Y-%m-%d")

    # adding forecasted values and plotting
    train_df['forecast'] = sarimax_mod.predict(start=start_index, end=last_row, dynamic=False, )

    # print(train_df[start_index:][['dailyconfirmed', 'forecast']].plot(figsize=(12, 8)))
    # future_predict = sarimax_mod.predict(start= last_row ,end = train_df.index+timedelta(days=7) ,dynamic= True,)
    # print(future_predict)

    # lets predict for upcomming dates ..
    # future_predict = sarimax_mod.predict(start=694, end=694 + 9)
    # print(future_predict.tail(7))



    future_predict = sarimax_mod.predict(start=694, end=694 + 9)
    f_temp = pd.DataFrame()
    f_temp['values'] = future_predict.values
    st.write(f_temp['values'].tail(7))
    fig_line1 = st.line_chart(f_temp, width=700, height=450)

    # today = datetime.date.today()+timedelta(days=7)
    # day_count = (end_date - start_date).days + 1
    import datetime
    for i in range(0,10):
        date=((datetime.date.today() + datetime.timedelta(i)).isoformat())
        st.write(date)


    # f_temp['date']= today + timedelta(days=7)
    # st.write(f_temp['date'])


