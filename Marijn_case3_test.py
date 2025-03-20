import streamlit as st
import pandas as pd

# Laad de weerdata
weer_data = pd.read_csv('weather_london.csv')

# Zet de 'Unnamed: 0' kolom om naar een datetime-object
weer_data['Date'] = pd.to_datetime(weer_data['Unnamed: 0'], format='%Y-%m-%d')

# Maak de Streamlit-app
st.title('Weerdata per Dag')

# Voeg een jaarkiezer toe
jaar = st.selectbox("Selecteer het jaar", sorted(weer_data['Date'].dt.year.unique()))

# Voeg een dagkiezer toe, die afhankelijk is van het geselecteerde jaar de juiste dagen toont
dagen_in_jaar = weer_data[weer_data['Date'].dt.year == jaar]['Date'].dt.day.unique()
dag = st.selectbox("Selecteer de dag", sorted(dagen_in_jaar))

# Filter de data voor het geselecteerde jaar en de geselecteerde dag
filtered_data = weer_data[(weer_data['Date'].dt.year == jaar) & (weer_data['Date'].dt.day == dag)]

# Toon de gegevens voor de geselecteerde dag
if not filtered_data.empty:
    st.write(f"Gegevens voor {dag}-{jaar}:")
    st.dataframe(filtered_data[['Date', 'tavg', 'tmin', 'tmax', 'prcp', 'snow', 'wdir', 'wspd', 'wpgt', 'pres', 'tsun']])
else:
    st.write("Geen gegevens gevonden voor de geselecteerde datum.")
