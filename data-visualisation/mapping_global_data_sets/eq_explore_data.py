import json
from plotly.graph_objs import Scattergeo, Layout, Figure
from plotly import offline

# Explore the structure of the data
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []

for dict in all_eq_dicts:
    mag = dict['properties']['mag']
    mags.append(mag)
    lon = dict['geometry']['coordinates'][0]
    lons.append(lon)
    lat = dict['geometry']['coordinates'][1]
    lats.append(lat)
    title = dict['properties']['title']
    hover_texts.append(title)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    }
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data':data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')