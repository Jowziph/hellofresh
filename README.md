# hellofresh
repo for hello fresh technical task


# coords.py
contains class Coords. uses pgeocode to find longitude and latitude of a postcode.

# temperature.py
contains class Temperature which inherits Coords. used for finding the temperature
on a date at a postcode. basis closest weather station from meteostat with 50km

# main.py
main file for processing meal boxes data. extracts CSVs, applies transformations,
and then loads to output.csv. 

# test.py
unit tests for Coords and Temperature classes.

run main.py to produce the output required, and test.py to for unit tests.

# further notes
- I investigated a few geospatial libraries for finding coordinates from postcodes.
  pgeocode seemed fairly quick, but in production I would spend more time on this
  potentially creating a database table for postcode to coordinate look ups.
- I chose to cut off weather stations at 50km away arbitrarily. this could be increased.
  This impacts locations which are very remote (e.g. the Gurnsey postcode)
- Temperature is based on the average temperature of that day. But meal boxes are most
  likely not delivered at night. A more accurate temperature estimate could be made here.