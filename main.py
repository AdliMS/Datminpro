import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import altair as alt
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Analisis Energi Listrik Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")
alt.themes.enable("dark")

df = pd.read_csv('data/global-data-on-sustainable-energy (1) (1).csv')
st.title('Analisis Kategori Suatu Wilayah Berdasarkan Aksesibilitas Terhadap Energi Listrik')
st.image('img/nasa.jpg', width=1700)

st.header('Business Understanding')
st.subheader('Business Objective')
st.write('Tujuan Bisnis dari dataset ini adalah untuk memahami pengkategorian baik-buruknya suatu daerah dalam aksesibilitasnya ke sumber energi listrik.')

st.subheader('Assess Situation')
st.write('Situasi bisnis yang mendasari penelitian ini adalah kurangnya pemahaman tentang suatu daerah apakah akses listriknya sudah baik atau belum.')

st.subheader('Data Mining Goals')
st.write('Hasil pengolahan pada dataset ini bertujuan agar pemerintah dapat memiliki pemahaman lebih dan pengetahuan yang lebih ringkas untuk masalah tingkat aksesibilitasnya terkait energi listrik.')

st.subheader('Project Plan')
st.write('Rencana dari proyek penelitian dataset ini adalah pertama - tama mengumpulkan data - data yang tersedia dari sumbernya. Selanjutnya data akan di eksplorasi mengenai pola - pola atau variabel - variabel yang berkaitan atau yang memiliki hubungan yang menarik. Lalu data akan dibersihkan dari nilai bias, nilai kosong, maupun nilai yang tidak relevan jika terdapat di dalam dataset tersebut. Dan terakhir data akan diolah dan divisualisasikan.')

st.header('Exploratory Data Analysis')

st.subheader('Tampilan dari 10 negara dengan rata - rata penggunaan listrik rendah karbon diurutkan dari yang paling banyak (%).')
country_electricity = df.groupby('Entity').mean(numeric_only=True).sort_values(by='Low-carbon electricity (% electricity)', ascending=False)
country_electricity = country_electricity['Low-carbon electricity (% electricity)']
st.table(country_electricity.head(10))

df_subset = df[['Entity', 'Year', 'Access to electricity (% of population)']]

st.subheader('5 Negara dengan emisi C02 terbanyak.')
average_co2_emission_by_country = df.groupby('Entity')['Value_co2_emissions_kt_by_country'].mean()
top_5_countries = average_co2_emission_by_country.nlargest(5)
fig = plt.figure(figsize = (5, 2))
sns.barplot(x = top_5_countries.index, y = top_5_countries.values)
plt.xlabel('Country')
plt.ylabel('Average CO2 Emissions (kT x 1e6)')
plt.title('Top 5 Countries with Highest Average CO2 Emissions')
st.pyplot(fig)

st.subheader('5 Negara dengan emisi C02 paling sedikit.')
top_5_lowest_emissions = average_co2_emission_by_country.nsmallest(5)
fig = plt.figure(figsize = (10, 6))
sns.barplot(x = top_5_lowest_emissions.values, y = top_5_lowest_emissions.index)
plt.xlabel('Average CO2 Emissions (kT)')
plt.ylabel('Country')
plt.title('Top 5 Countries with the Lowest CO2 Emissions')
st.pyplot(fig)

st.subheader('Pertumbuhan rata - rata untuk emisi CO2 tiap tahunnya.')
average_co2_by_year = df.groupby('Year')['Value_co2_emissions_kt_by_country'].mean()
average_co2_by_year = average_co2_by_year.reset_index()
fig = plt.figure(figsize = (10, 6))
sns.lineplot(data = average_co2_by_year, x = 'Year', y = 'Value_co2_emissions_kt_by_country', color = 'black')
plt.title('Average Growth of CO2 Emissions Over the Years')
plt.xlabel('Year')
plt.ylabel('Average CO2 Emissions (kT)')
plt.xticks(average_co2_by_year['Year'], rotation = 0, ha = 'center')
plt.xlim(2000, 2019) #2020 doesn't containt data
plt.tight_layout()
plt.show()
st.pyplot(fig)

st.subheader('Korelasi antar kolom pada dataset.')
corr_subset = df.drop(columns=['Entity', 'Year'])
corr_matrix = corr_subset.corr()
corr_values = corr_matrix.values.tolist()
corr_columns = corr_matrix.columns.tolist()

fig = go.Figure(data = go.Heatmap(z = corr_values,
                                x = corr_columns,
                                y = corr_columns,
                                colorscale = 'RdBu_r',
                                zmin = -1,
                                zmax = 1,
                                colorbar_title = 'Legend'))
fig.update_layout(title = 'Correlation Heatmap', width = 1000, height = 1000)
st.plotly_chart(fig)
# st.bar_chart(year, x='work_year', y='salary_in_usd')
# st.caption('Tampilan di atas merupakan rata - rata gaji tiap tahunnya untuk pekerjaan di bidang Data Science mulai dari tahun 2020 hingga tahun 2023.')

# # first plot with X and Y data
# plt.plot(year['work_year'], year['salary'])
# # second plot with x1 and y1 data
# plt.plot(year['work_year'], year['salary_in_usd'])

# plt.xlabel("X-axis data")
# plt.ylabel("Y-axis data")
# plt.title('multiple plots')
# st.pyplot(plt)
# st.caption('Dari sini kita bisa melihat, bahwa baik dari salary maupun salary_in_usd, keduanya mengalami peningkatan nilai untuk tiap tahunnya, dengan peningkatan paling besar ada diantara tahun 2021 - 2022.')

# job_title = df[['job_title', 'salary_in_usd']]
# job_title = job_title.groupby('job_title').median()
# job_title = job_title.rename_axis('job_title').reset_index()
# job_title = job_title.sort_values(by=['salary_in_usd'], ascending=False).head(10)
# job_title

# # Figure Size
# fig, ax = plt.subplots(figsize =(16, 9))

# # Horizontal Bar Plot
# ax.barh(job_title['job_title'], job_title['salary_in_usd'])

# # Remove axes splines
# for s in ['top', 'bottom', 'left', 'right']:
#     ax.spines[s].set_visible(False)

# # Remove x, y Ticks
# ax.xaxis.set_ticks_position('none')
# ax.yaxis.set_ticks_position('none')

# # Add padding between axes and labels
# ax.xaxis.set_tick_params(pad = 5)
# ax.yaxis.set_tick_params(pad = 10)

# # Add x, y gridlines

# # Show top values
# ax.invert_yaxis()
# st.pyplot(plt)
# st.caption('Lalu dari tabel dan grafik diatas kita bisa menyimpulkan bahwa "Analytics Engineering Manager" merupakan pekerjaan dengan salary atau gaji tertinggi. Diikuti oleh "Data Science Tech Lead", "Managing Director Data Science", dst.')
