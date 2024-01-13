import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, mean_squared_log_error
@st.cache()
def prediction(cars_df, carwidth, enginesize, horsepower, drive_wheel_fwd, car_company_buick):
	x = cars_df.iloc[:, :-1]
	y = cars_df['price']
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

	lr = LinearRegression()
	lr.fit(x_train, y_train)
	lr_score = lr.score(x_train, y_train)
	predict_price = lr.predict([[carwidth, enginesize, horsepower, drive_wheel_fwd, car_company_buick]])
	predict_price = predict_price[0]
	y_pred = lr.predict(x_test)
	r2 = r2_score(y_test, y_pred)
	mae = mean_absolute_error(y_test, y_pred)
	rmse = np.sqrt(mean_squared_error(y_test, y_pred))
	msle = mean_squared_log_error(y_test, y_pred)

	return predict_price, lr_score, r2, mae, rmse, msle

def app(cars_df):
	st.markdown("<p style = 'color: blue; font-size = 25px'>This app uses <b>Linear Regresssion</b> to predict the price of a car based on your inputs.</p>", unsafe_allow_html = True)
	st.subheader('Select Values: ')
	cw = st.slider('Car Width', float(cars_df['carwidth'].min()), float(cars_df['carwidth'].max()))
	es = st.slider('Engine Size', float(cars_df['enginesize'].min()), float(cars_df['enginesize'].max()))
	hp = st.slider('Horsepower', float(cars_df['horsepower'].min()), float(cars_df['horsepower'].max()))
	dfwd = st.radio('Is it a Forward Drive Wheel Car?', ('Yes', 'No'))
	if dfwd == 'Yes':
		dfwd = 1
	else:
		dfwd = 0
	cb = st.radio('Is it manufactured by Buick? $$', ('Yes', 'No'))
	if cb == 'Yes':
		cb = 1
	else:
		cb = 0
	if st.button('Predict'):
		st.subheader('Prediction Results') 
		pr, score1, r2, mae, rmse, msle = prediction(cars_df, cw, es, hp, dfwd, cb)
		st.success(f'The Predicted price of the car is: ${pr}')
		st.info(f'Accuracy score of this model is: {score1}')
		st.info(f'The R-squared score is: {r2}')
		st.info(f'The Mean Squared Error value is: {mae}')
		st.info(f'The Root Mean Sqaured Error value is: {rmse}')
		st.info(f'The Mean Squared Log Error value is: {msle}')