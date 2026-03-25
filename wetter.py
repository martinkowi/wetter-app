import streamlit as st
import requests
import os
import datetime
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

st.title ("Wetter App")

stadt = st.text_input("Stadt eingeben")

if st.button("Wetter abrufen") and stadt:
	url = f"{BASE_URL}?q={stadt}&appid={API_KEY}&units=metric&lang=de"
	antwort = requests.get(url)
	daten = antwort.json()

	if daten["cod"] == 200:
		temp = daten["main"]["temp"]
		gefuehlt = daten["main"]["feels_like"]
		beschreibung = daten["weather"][0]["description"]
		luftfeuchtigkeit = daten["main"]["humidity"]
		wind = daten["wind"]["speed"]
		luftdruck = daten["main"]["pressure"]
		icon = daten["weather"][0]["icon"]
		sonnenaufgang = datetime.datetime.utcfromtimestamp(daten["sys"]["sunrise"] + daten["timezone"]).strftime("%H:%M")
		sonnenuntergang = datetime.datetime.utcfromtimestamp(daten["sys"]["sunset"] + daten["timezone"]).strftime("%H:%M")
		icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"

		col1, col2 =  st.columns([1, 3])
		with col1:
			st.image(icon_url, width=100)
		with col2:
			st.success(f"Temperatur: {temp}°C")
			st.info(f"Gefühlt: {gefuehlt}°C")

		col3, col4 = st.columns(2)
		with col3:
			st.info(f"Luftfeuchtigkeit: {luftfeuchtigkeit}%")
			st.info(f"Wind: {wind} m/s")
		with col4:
			st.info(f"Luftdruck: {luftdruck} hPa")
			st.info(f"Wetter: {beschreibung.capitalize()}")
		
		st.divider()
		col5, col6 = st.columns(2)
		with col5:
			st.info(f"Sonnenaufgang: {sonnenaufgang} Uhr")
		with col6:
			st.info(f"Sonnenuntergang: {sonnenuntergang} Uhr")

	else:
		st.error("Stadt nicht gefunden")