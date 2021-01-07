import folium

map = folium.Map(Location=[-6.2203023,106.8370596])
map.save('jakarta.html')

data = folium.Map(Location=[-6.2203023,106.8370596], zoom_start=12)
data.save('jakarta-zoom.html')

terain = folium.Map(Location=[-6.2203023,106.8370596], zoom_start=12, tiles='stamenterrain')
terain.save('jakarta-terrain.html')

toner = folium.Map(Location=[-6.2203023,106.8370596], zoom_start=12, tiles='stamentoner')
toner.save('jakarta-toner.html')