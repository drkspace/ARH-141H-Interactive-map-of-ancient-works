import csv

name = raw_input("Artwork name ")
lat = raw_input("Latitude ")
lon = raw_input("Longitude ")
artist = raw_input("artist ")
per = raw_input("Period ")
year = raw_input("year(s) ")
mat = raw_input("Material ")
term = raw_input("Terms ")
n = int(raw_input("How many facts "))

f = []
for i in range(n):
    
    f.append(raw_input("fact #{} ".format(i+1)))

s=""
br = "</br>"
for i in f:
    if i is "":
        continue
    s+=(i+br)

with open('data.csv', 'a') as data:
    writer = csv.writer(data, dialect='excel')
    writer.writerow([name, lat, lon, artist, per, year, mat, term, s])
