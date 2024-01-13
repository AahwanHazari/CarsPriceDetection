import streamlit as st
import numpy as np           
import pandas as pd
def app(cars_df):
	st.header('View Data')
	with st.beta_expander('View Dataset: '):
		st.table(cars_df)
	st.subheader('Columns Description: ')
	if st.checkbox('Show Summary: '):
		st.table(cars_df.describe())
	beta_col1, beta_col2, beta_col3 = st.beta_columns(3)
	with beta_col1:
		if st.checkbox('Show all Column Names: '):               
			st.table(list(cars_df.columns)) 
	with beta_col2:
		if st.checkbox('Show Column Data Types: '):               
			st.table(cars_df.dtypes) 
	with beta_col3:
		if st.checkbox('Show Column Data: '):               
			col_data = st.selectbox('Select Columns', tuple(cars_df.columns))
			st.write(cars_df[col_data])                        
