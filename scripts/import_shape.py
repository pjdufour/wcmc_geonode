#!/usr/bin/python
import sys
import os.path  
import psycopg2
import osgeo.ogr

sys.path.insert(0, '../wcmc_geonode/wcmc_geonode')

try:
    from local_settings import *
except ImportError:
    pass

datastore = DATABASES['datastore']
conn_string = "host=" + datastore['HOST'] + " port=" + datastore['PORT'] + " dbname=" + datastore['NAME'] + " user=" + datastore['USER'] + " password=" + datastore['PASSWORD']
connection = psycopg2.connect(conn_string)  
cursor = connection.cursor()  
cursor.execute("DELETE FROM countries")  
srcFile = ".shp"  
shapefile = osgeo.ogr.Open(srcFile)    
layer = shapefile.GetLayer(0)    cursor.execute("DELETE FROM countries")
for i in range(layer.GetFeatureCount()):  
    feature = layer.GetFeature(i)  
    name = feature.GetField("NAME").decode("Latin-1")  
    wkt = feature.GetGeometryRef().ExportToWkt()  
    cursor.execute("INSERT INTO countries (name,outline) " +"VALUES (%s, ST_GeometryFromText(%s, " +"4326))", (name.encode("utf8"), wkt))  

connection.commit()  

