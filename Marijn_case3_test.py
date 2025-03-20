import streamlit as st
import pandas as pd

# Laad de weerdata
weer_data = pd.read_csv('weather_london.csv')

# Zet de 'Unnamed: 0' kolom om naar een datetime-object
weer_data['Date'] = pd.to_datetime(weer_data['Unnamed: 0'], format='%Y-%m-%d')

# Filter de data zodat alleen 2021 wordt getoond
weer_data_2021 = weer_data[weer_data['Date'].dt.year == 2021]

# Maak de Streamlit-app
st.title('Weerdata voor 2021')

# Voeg een jaarkiezer toe (alleen 2021 beschikbaar)
jaar = st.selectbox("Selecteer het jaar", [2021])

# Voeg een dagkiezer toe, die alleen de dagen in 2021 toont
dagen_in_jaar = weer_data_2021['Date'].dt.day.unique()
dag = st.selectbox("Selecteer de dag", sorted(dagen_in_jaar))

# Filter de data voor 2021 en de geselecteerde dag
filtered_data = weer_data_2021[(weer_data_2021['Date'].dt.year == jaar) & (weer_data_2021['Date'].dt.day == dag)]

# Vertaling van kolomnamen naar volledige betekenis
column_mapping = {
    'tavg': 'Gemiddelde Temperatuur (°C)',
    'tmin': 'Minimale Temperatuur (°C)',
    'tmax': 'Maximale Temperatuur (°C)',
    'prcp': 'Neerslag (mm)',
    'snow': 'Sneeuwval (cm)',
    'wdir': 'Windrichting (°)',
    'wspd': 'Windsnelheid (m/s)',
    'wpgt': 'Windstoten (m/s)',
    'pres': 'Luchtdruk (hPa)',
    'tsun': 'Zonduur (uren)'
}

# Toon de gegevens voor de geselecteerde dag met vertaalde kolomnamen
if not filtered_data.empty:
    st.write(f"Gegevens voor {dag}-{jaar}:")
    # Vervang de kolomnamen door de volledige betekenis
    filtered_data = filtered_data.rename(columns=column_mapping)
    st.dataframe(filtered_data[['Date', 'Gemiddelde Temperatuur (°C)', 'Minimale Temperatuur (°C)', 
                                 'Maximale Temperatuur (°C)', 'Neerslag (mm)', 'Sneeuwval (cm)', 
                                 'Windrichting (°)', 'Windsnelheid (m/s)', 'Windstoten (m/s)', 
                                 'Luchtdruk (hPa)', 'Zonduur (uren)']])
else:
    st.write("Geen gegevens gevonden voor de geselecteerde datum.")
