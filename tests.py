import unittest
from coords import Coords
from temperature import Temperature
from datetime import datetime

class TestSum(unittest.TestCase):

    def test_postcode_spacing(self):
        """
        Test that spaces are added correctly
        """
        self.assertEqual(Coords("BA11AA").postcode,"BA1 1AA")
        self.assertEqual(Coords("BA151AA").postcode,"BA15 1AA")
        
    def test_postcode_coords(self):
        """
        Test that lat long is approximately right from pgeocode library
        """
        lat, long = list(Coords("BA11AA").getLatLong())
        self.assertAlmostEqual(lat,51.3788,1)
        self.assertAlmostEqual(long,-2.3556,1)

    def test_date_format(self):
        """
        Test that str->date works. using date which could
        be confused with american date format.
        """
        outputDate = Temperature("BA11AA","12/02/2022 00:00").date
        self.assertEqual(outputDate,datetime(2022,2,12))

    def test_temp_result(self):
        """
        Test that the returned temp for postcode/date combination
        is roughly the same as data available from the website.
        Basis hourly csv downloaded from https://meteostat.net/en/place/gb/bath?s=03726&t=2022-06-15/2022-06-22
        then averaged for relevant day
        """
        outputTemp = Temperature("BA11AA","15/06/2022 00:00").getTemp()
        self.assertAlmostEqual(outputTemp,16.875,1)

if __name__ == '__main__':
    unittest.main()