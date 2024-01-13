import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def app(cars_df):
	st.header('Visualized Data: ')
	st.set_option('deprecation.showPyplotGlobalUse', False)
	plot_choice = st.multiselect('Select Charts or Plots: ', ('Scatter Plot', 'Histogram', 'Box Plot', 'Correlation Heatmap'))

	if 'Scatter Plot' in plot_choice:
		st.subheader('Scatter Plot: ')
		features_list = st.multiselect('Select X-axis Value: ', ('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick'))
		for f in features_list:
			st.subheader(f'Scatter Plot between {f}, and Price.')
			plt.figure(figsize = (10, 5))
			sns.scatterplot(x = f, y = 'price', data = cars_df)
			st.pyplot()

	if 'Histogram' in plot_choice:
		st.subheader('Histogram: ')
		columns = st.selectbox('Select the column to make its Histogram: ', ('carwidth', 'enginesize', 'horsepower'))
		st.subheader(f'Histogram between {columns}, and Price.')
		plt.figure(figsize = (10, 5))
		plt.hist(cars_df[columns], bins = 'sturges', edgecolor = 'black')
		st.pyplot()
	

	if 'Box Plot' in plot_choice:
		st.subheader('Box Plot: ')
		columns = st.selectbox('Select the column to make its Box Plot: ', ('carwidth', 'enginesize', 'horsepower'))
		st.subheader(f'Box Plot for {columns}.')
		plt.figure(figsize = (10, 5))
		sns.boxplot(cars_df[columns])
		st.pyplot()


	if 'Correlation Heatmap' in plot_choice:
		st.subheader('Heatmap: ')
		st.subheader(f'Correalation Heatmap: ')
		plt.figure(figsize = (10, 5))
		ax = sns.heatmap(cars_df.corr(), annot = True)
		bottom, top = ax.get_ylim()
		ax.set_ylim(bottom + 0.5, top - 0.5)
		st.pyplot()