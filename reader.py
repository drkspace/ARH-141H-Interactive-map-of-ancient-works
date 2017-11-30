import csv

"""
Format:
name,lat,lon,artist,period,year,material,relevent terms,other
"""
class reader(object):

    def __init__(self, file):
        self.file = file
        self.data = []
    
    def read(self):
        lines = []
        with open(self.file, 'r') as file:
            r = csv.reader(file, delimiter = ',')
            for i in r:
                if i is []:
                    continue
                self.data.append(i)
    



