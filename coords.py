import pgeocode

class Coords():

    def __init__(self,postcode):
        self.postcode = postcode
        if not " " in self.postcode:
            self.postcode = self.postcode[:-3] + " " + self.postcode[-3:]

    def __repr__(self):
        return self.postcode

    def getLatLong(self):
        nomi = pgeocode.Nominatim('gb') 
        return nomi.query_postal_code(self.postcode)[["latitude","longitude"]]
    