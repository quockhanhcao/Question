import json
import pandas as pd
import plotly.express as px


country = json.load(open("countries.geojson", "r"))
df = pd.read_csv('forward_country.csv')
country_code_map = {}

for feature in country['features']:
    feature['code'] = feature['properties']['ISO_A3']
    country_code_map[feature['properties']['ADMIN']] = feature['code']


df['code'] = df['Country'].apply(lambda x: country_code_map[x])


fig = px.choropleth(df, locations='code', geojson=country, color = 'Number')
fig.show()
