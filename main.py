"""
This is the main file that contains the FastAPI app.
It should contain the following endpoints: 
- list_client_ids: List all client ids.
- summarize: Summarize the dataset.
- predict: Predict client id.
- client_info: Get client info.
- explanation: Get explanation for the decision.
- ping: Check if the app is up and running.
"""

#import pickle, json,  joblib
#import pandas as pd
#from fastapi import FastAPI
#import uvicorn
#from colorama import init
#import shap
import streamlit as st
import requests
import matplotlib.pyplot as plt

# create the FastAPI app
#app = FastAPI()

    
def get_pong():
    url = 'https://p7-api.onrender.com/ping'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error: {response.status_code}"



def get_client_ids():
    url = 'https://p7-api.onrender.com/list_client_ids'
    response = requests.get(url)
    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            return "Invalid JSON response"
    else:
        return f"Error: {response.status_code}"
    


def get_summarize():
    url = 'https://p7-api.onrender.com/summarize'
    response = requests.get(url)
    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            return "Invalid JSON response"
    else:
        return f"Error: {response.status_code}"
    
    
    
def get_client_info(client_id):
    url = 'https://p7-api.onrender.com/client_info/' + str(client_id)
    response = requests.get(url)
    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            return "Invalid JSON response"
    else:
        return f"Error: {response.status_code}"
    
    
def get_predict(client_id):
    url = 'https://p7-api.onrender.com/predict/' + str(client_id)
    response = requests.get(url)
    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            return "Invalid JSON response"
    else:
        return f"Error: {response.status_code}"
    
    
    
def get_explanation(client_id):
    url = 'https://p7-api.onrender.com/explanation/' + str(client_id)
    response = requests.get(url)
    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            return "Invalid JSON response"
    else:
        return f"Error: {response.status_code}"
    
    

    
# Commandes Streamlit

st.sidebar.title("Project 7")


url = 'https://p7-api.onrender.com/list_client_ids'
response = requests.get(url)
list_client_ids = response.json()['client_ids']


st.write("### List of Client Ids")
st.write(get_client_ids())

valeur_choisie = st.selectbox("Choose a Client Id :", list_client_ids)


st.write("### summarize")
st.write(get_summarize())
    

st.write("### Client Info")
st.write(get_client_info(valeur_choisie))
    

st.write("### Prediction")
st.write(get_predict(valeur_choisie))
prediction = get_predict(valeur_choisie)
if prediction['prediction']==0:
    st.write("You do not have your credit")
else:
    st.write("You have your credit")



st.write("### Explanation")
st.write(get_explanation(valeur_choisie))
    
# bar plot graph
fig, ax = plt.subplots()

# Obtenir les données
data = get_explanation(valeur_choisie)

# Trier les données par ordre décroissant des valeurs
sorted_data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

# Extraire les clés et les valeurs triées
keys = list(sorted_data.keys())
values = list(sorted_data.values())

# Tracer le graphique en barres
ax.bar(keys, values)
ax.set_xlabel('Keys')
ax.set_ylabel('Values')
ax.set_title('Bar Plot from Dictionary Data')
ax.set_xticklabels(keys, rotation=90, fontsize=7)
st.pyplot(fig)
 
    
#if __name__ == '__main__':
#    init()
#    uvicorn.run(app, host = "127.0.0.1", port = 5000)