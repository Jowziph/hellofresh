from meteostat import Daily, Point
from datetime import datetime
from coords import Coords

class Temperature(Coords):

    def __init__(self,postcode,date):
        self.date = datetime.strptime(date,'%d/%m/%Y %H:%M')
        super().__init__(postcode)

    def __repr__(self):
        return f"{super().__repr__()};{str(self.date)}"

    def getTemp(self):
        self.lat, self.long = self.getLatLong()
        point =  Point(self.lat, self.long)
        point.radius = 50000
        try:
          return Daily(point,self.date,self.date).fetch().tavg[0]
        except:
            print(self)
            Exception