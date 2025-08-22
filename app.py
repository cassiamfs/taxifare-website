import streamlit as st
import datetime
import requests


'''
# TaxiFare Prediction Model
'''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''

d = st.date_input(
    "Date",
    datetime.date(2019, 7, 6))

t = st.time_input('Time')

st.write()
date_time = f"{d} {t}"
st.markdown("***")
plon = st.number_input('Pickup Longitude')

st.markdown("***")
plat = st.number_input('Pickup Latitude')

st.markdown("***")
dlon = st.number_input('Dropoff Longitude')

st.markdown("***")
dlat = st.number_input('Dropoff Latitude')

st.markdown("***")
passenger_num = st.number_input('Passengers', min_value=1, value=int(1),)



# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

url = 'https://taxifare-794605485301.europe-southwest1.run.app/predict' # pon tu api url

# usar request package para hacer un get request a nuestro api
# guardar la prediction y display pred en la web st

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

params = {'pickup_datetime': date_time,
          'pickup_longitude':plon,
          'pickup_latitude': plat,
          'dropoff_longitude':dlon,
          'dropoff_latitude': dlat,
          'passenger_count': passenger_num
          }
response = requests.get(url, params=params)
st.markdown("***")
if st.button('Prediction'):
    # print is visible in the server output, not in the page

    json_response = response.json()
    fare_amount = json_response['fare']
    fare_rounded = round(fare_amount, 2)


    st.write('Fare:','$',fare_rounded)

    st.markdown("***")
    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXkwaGQydmhzaWJpZWlwcGc1YTFrc2I5dW51cDR1M3k2d3d1NTVsaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3orieXpGEQYMhTVwsM/giphy.gif")

else:
    st.write('🤑')

# # Verificar el status code
# if response.status_code == 200:
#     print("Request exitoso")
#     # Convertir la respuesta JSON a diccionario de Python
#     data = response.json()
#     print("Respuesta:", data)
#     pred = data.get("fare")
#     print("Predicción:", pred)
# else:
#     print("Error en la petición:", response.status_code)


# '''


# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''
