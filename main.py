import pandas as pd
from pandasql import sqldf
from coords import Coords
from temperature import Temperature
import configparser

def main():

    #load data from csv
    boxes_df = pd.read_csv("Boxes.csv")
    temperature_bands_df = pd.read_csv("Temperature_bands.csv")


    #added for testing
    config = configparser.ConfigParser()
    config.read("config.ini")
    maxRecords = int(config['default']["maxRecords"])
    boxes_df = boxes_df.head(maxRecords)


    boxes_df['temp'] = boxes_df.apply(lambda x: Coords(x.postcode).getLatLong(), axis=1)
    #find temp at that location on that day
    boxes_df['temp'] = boxes_df.apply(lambda x: Temperature(x.postcode,x.delivery_date).getTemp(), axis=1)
    boxes_df = boxes_df[["box_id","Box Size","temp"]]


    #unpivot temperature df for joining to boxes_df
    temperature_bands_df = pd.melt(temperature_bands_df, id_vars=['temperature_min','temperature_max'], value_vars=['S','M','L'],var_name='size', value_name='ice_packs')


    #join using sql for ease
    output_df = sqldf("""
        SELECT B.box_id
            , T.ice_packs
        FROM boxes_df B 
        LEFT OUTER JOIN temperature_bands_df T 
            ON B.temp > temperature_min 
                AND B.temp <= temperature_max 
                AND B.[Box Size] = T.size
        """)


    #create outpt csv
    output_df.to_csv("output.csv",index=False)


if __name__ == "__main__":
    main()
