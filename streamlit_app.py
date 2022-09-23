import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favories')
streamlit.text('🥣  Omega 3 &Blueberry ouatmeal')
streamlit.text(' 🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocato Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#import requests

streamlit.header('Fruityvice Fruit Advice!')

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/{}".format(fruit_choice))


#normaliza a resposta json
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# envia a tabela de output
streamlit.dataframe(fruityvice_normalized)

streamlit.stop()
#import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header('The fruit load list contains')
streamlit.dataframe(my_data_rows)


fruit_choice1 = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ', fruit_choice1)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/{}".format(fruit_choice))



