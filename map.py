import plotly.plotly as py
from plotly.graph_objs import *
import reader
import artworks
import pprint

print "Fire up your engines"
def formatText(names, artist, period, year, material, terms, other):
  text = []
  for i in range(len(names)):
    text.append("{}</br></br>{}</br>{}</br>{}</br>{}</br>{}</br>{}".format(
                  names[i], artist[i], period[i], 
                  year[i].replace(u'\xa0', ''), material[i].replace(u'\xa0', ''), terms[i].replace(u'\xa0', ''), other[i].replace(u'\xa0', '')))
  #pprint.pprint(text)
  return text

file = "data.csv"

read = reader.reader(file)
read.read()
art = artworks.artworks(read.data)

periods = ['Geometric', 'Orientalizing', 'Archaic', 'Hellenistic', 'Early Classical',
           'High Classical', 'Late Classical', 'Roman Republicain', 'Roman Early Imperial',
           'Roman Late Imperial', 'Early Christain', 'Early Medieval Art', 'Romanesque Art']
p = [[] for i in periods]
for i in range(len(art.period)):
  match = False
  for j in range(len(periods)):
    
    if art.period[i] == periods[j]:
      p[j].append(read.data[i])
      match = True
      continue
  if not match:
    print read.data[i]


data = Data([{ 
    "lat" : art.lat,
    "lon" : art.lon,
    "text" : formatText(art.name, art.artist, art.period,
                       art.year, art.material, art.terms, art.other),
    "hoverinfo" : "text",
    "marker": {
      "color": 10,  
      "colorscale": "Greens", 
      "symbol" : "square", 
      "size": 5,
  }, 
  "mode": "markers", 
  "name": "", 
  "type": "scattergeo"
}])
#print trace1

#data = Data([trace1])
layout = {
  "autosize": True, 
  "geo": {
    "resolution": 50, 
    "scope": "europe"
  }, 
  "height": 701, 
  "showlegend": False, 
  "title": "ARH 141 Artwork locations", 
  "width": 792
}

fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename="ARH 141 Artwork locations")

for i in range(len(periods)):
  if len(p[i]) == 0: continue
  layout['title'] = periods[i]
  tmp = artworks.artworks(p[i])
  data[0]['lat'] = tmp.lat
  data[0]['lon'] = tmp.lon
  data[0]['text'] = formatText(tmp.name, tmp.artist, tmp.period,
                       tmp.year, tmp.material, tmp.terms, tmp.other)
  #pprint.pprint(data)
  fig = Figure(data=data, layout=layout)
  plot_url = py.plot(fig, filename = periods[i])
