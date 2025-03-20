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

# Keuze voor de weergave: specifieke datum of specifieke week
keuze = st.radio("Kies een weergave:", ('Specifieke Dag', 'Specifieke Week'))

if keuze == 'Specifieke Dag':
    # Datumkiezer voor een specifieke dag in 2021
    datum = st.date_input("Selecteer de datum", min_value=pd.to_datetime("2021-01-01"), max_value=pd.to_datetime("2021-12-31"))

    # Filter de data voor de geselecteerde datum
    filtered_data = weer_data_2021[weer_data_2021['Date'] == datum]

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

    # Toon de gegevens voor de geselecteerde datum
    if not filtered_data.empty:
        st.write(f"Gegevens voor {datum.strftime('%d-%m-%Y')}:")
        filtered_data = filtered_data.rename(columns=column_mapping)
        st.dataframe(filtered_data[['Date', 'Gemiddelde Temperatuur (°C)', 'Minimale Temperatuur (°C)', 
                                     'Maximale Temperatuur (°C)', 'Neerslag (mm)', 'Sneeuwval (cm)', 
                                     'Windrichting (°)', 'Windsnelheid (m/s)', 'Windstoten (m/s)', 
                                     'Luchtdruk (hPa)', 'Zonduur (uren)']])
    else:
        st.write("Geen gegevens gevonden voor de geselecteerde datum.")

elif keuze == 'Specifieke Week':
    # Keuze voor weeknummer (1 t/m 52)
    week_nummer = st.slider("Kies een weeknummer", 1, 52)

    # Voeg een kolom voor weeknummer toe aan de dataset
    weer_data_2021['Week'] = weer_data_2021['Date'].dt.isocalendar().week

    # Filter de data voor de geselecteerde week
    filtered_data_week = weer_data_2021[weer_data_2021['Week'] == week_nummer]

    # Toon de gegevens voor de geselecteerde week
    if not filtered_data_week.empty:
        st.write(f"Gegevens voor week {week_nummer} van 2021:")
        filtered_data_week = filtered_data_week.rename(columns=column_mapping)
        st.dataframe(filtered_data_week[['Date', 'Gemiddelde Temperatuur (°C)', 'Minimale Temperatuur (°C)', 
                                         'Maximale Temperatuur (°C)', 'Neerslag (mm)', 'Sneeuwval (cm)', 
                                         'Windrichting (°)', 'Windsnelheid (m/s)', 'Windstoten (m/s)', 
                                         'Luchtdruk (hPa)', 'Zonduur (uren)']])
    else:
        st.write(f"Geen gegevens gevonden voor week {week_nummer} van 2021.")
