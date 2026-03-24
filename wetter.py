import streamlit as st
import requests

API_KEY = "60f3b0b3faec46c13e06d3758f6df964"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

st.title ("Wetter App")

stadt = st.text_input("Stadt eingeben")

if st.button("Wetter abrufen") and stadt:
	url = f"{BASE_URL}?q={stadt}&appid={API_KEY}&units=metric&lang=de"
	antwort = requests.get(url)
	daten = antwort.json()

	if daten["cod"] == 200:
		temp = daten["main"]["temp"]
		beschreibung = daten["weather"][0]["description"]
		luftfeuchtigkeit = daten["main"]["humidity"]

		st.success(f"Temperatur: {temp}°C")
		st.info(f"Wetter: {beschreibung}")
		st.info(f"Luftfeuchtigkeit: {luftfeuchtigkeit}%")
	else:
		st.error("Stadt nicht gefunden")