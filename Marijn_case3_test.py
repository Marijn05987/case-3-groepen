import streamlit as st
import pandas as pd

# Laad de weerdata
weer_data = pd.read_csv('weather_london.csv')

# Zet de 'Unnamed: 0' kolom om naar een datetime-object
weer_data['Date'] = pd.to_datetime(weer_data['Unnamed: 0'], format='%Y-%m-%d')

# Filter de data voor 2021
weer_data_2021 = weer_data[weer_data['Date'].dt.year == 2021]

# Maak de Streamlit-app
st.title('Weerdata voor 2021')

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

# Kalender om een specifieke datum te kiezen
datum = st.date_input("Selecteer een datum in 2021", min_value=pd.to_datetime("2021-01-01"), max_value=pd.to_datetime("2021-12-31"))

# Haal het weeknummer van de geselecteerde datum op
week_nummer = datum.isocalendar()[1]

# Filter de data voor de geselecteerde week
weer_data_2021['Week'] = weer_data_2021['Date'].dt.isocalendar().week
filtered_data_week = weer_data_2021[weer_data_2021['Week'] == week_nummer]

# Toon de gegevens voor de geselecteerde week
if not filtered_data_week.empty:
    st.write(f"Gegevens voor week {week_nummer} van 2021 (rondom {datum.strftime('%d-%m-%Y')}):")
    # Vervang kolomnamen met de vertaalde versie
    filtered_data_week = filtered_data_week.rename(columns=column_mapping)

    # Reset de index en voeg de aangepaste index toe die begint bij 1
    filtered_data_week_reset = filtered_data_week.reset_index(drop=True)
    filtered_data_week_reset.index = filtered_data_week_reset.index + 1  # Start de index vanaf 1

    # Zorg ervoor dat de juiste kolommen worden weergegeven zonder de oude index
    st.dataframe(filtered_data_week_reset[['Date', 'Gemiddelde Temperatuur (°C)', 'Minimale Temperatuur (°C)', 
                                           'Maximale Temperatuur (°C)', 'Neerslag (mm)', 'Sneeuwval (cm)', 
                                           'Windrichting (°)', 'Windsnelheid (m/s)', 'Windstoten (m/s)', 
                                           'Luchtdruk (hPa)', 'Zonduur (uren)']])
else:
    st.write(f"Geen gegevens gevonden voor week {week_nummer} van 2021.")
