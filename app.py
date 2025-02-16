import pickle
from PIL import Image
import streamlit as st
import streamlit.components.v1 as stc

# importing the smaller apps
from home import home
from info import info
from precaution import precaution
from analysis import analysis
from prediction import prediction

def main():

	menu = ["Home", "Info", "Precautions","Analysis", "Prediction"]
	choice = st.sidebar.selectbox("PAGES", menu)

	if choice=="Home":
		home()
	elif choice=="Info":
		info()
	elif choice == "Precautions":
		precaution()
	elif choice == "Analysis":
		analysis()		
	elif choice == "Prediction":
		prediction()
	

main()