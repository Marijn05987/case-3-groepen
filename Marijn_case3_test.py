import streamlit as st
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static  # Importeer folium_static
import pandas as pd

# Laad de fietsstations data
cyclestations_data = pd.read_csv('cycle_stations_updated.csv')

# Convert 'Datetime' column to a readable string format (if it's not already in string format)
cyclestations_data['Datetime'] = pd.to_datetime(cyclestations_data['Datetime'], errors='coerce').dt.strftime('%Y-%m-%d')

# Maak een Streamlit app layout
st.title('London Cycle Stations')
st.markdown("Interaktive map met fietsverhuurstations in Londen")

# Voeg een slider toe om het aantal fietsen in te stellen
bike_slider = st.slider("Selecteer het aantal beschikbare fietsen", 0, 100, 0)

# Maak een basemap van Londen
m = folium.Map(location=[51.5074, -0.1278], zoom_start=12)

# MarkerCluster om stations te groeperen
marker_cluster = MarkerCluster().add_to(m)

# Voeg de stations toe aan de kaart
for index, row in cyclestations_data.iterrows():
    lat = row['lat']
    long = row['long']
    station_name = row['name']
    nb_bikes = row['nbBikes']  # Aantal fietsen
    nb_standard_bikes = row['nbStandardBikes']  # Aantal standaardfietsen
    nb_ebikes = row['nbEBikes']  # Aantal ebikes
    install_date = row['Datetime']  # Installatiedatum van het station

    # Voeg een marker toe met info over het station
    if nb_bikes >= bike_slider:  # Controleer of het aantal fietsen groter of gelijk is aan de slider
        folium.Marker(
            location=[lat, long],
            popup=folium.Popup(
                f"Station: {station_name}<br>Aantal fietsen: {nb_bikes}<br>Standaard: {nb_standard_bikes}<br>EBikes: {nb_ebikes}<br>Installatie datum: {install_date}",
                max_width=300
            ),
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(marker_cluster)

# Render de kaart in de Streamlit app
folium_static(m)
