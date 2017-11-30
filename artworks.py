class artworks():

    def __init__(self,artlist):
        self.artlist = artlist
        self.name = [i[0] for i in self.artlist]
        self.lat = [float(i[1]) for i in self.artlist]
        self.lon = [float(i[2]) for i in self.artlist]
        self.artist = [i[3] for i in self.artlist]
        self.period = [i[4] for i in self.artlist]
        self.year = [i[5] for i in self.artlist]
        self.material = [i[6] for i in self.artlist]
        self.terms = [i[7] for i in self.artlist]
        self.other = [i[8] for i in self.artlist]
        

