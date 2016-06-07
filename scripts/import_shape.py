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

ogr = osgeo.ogr
datastore = DATABASES['datastore']
database = datastore['NAME']
serverName = datastore['HOST']
port = datastore['PORT']
usr = datastore['USER']
pw = datastore['PASSWORD']
sourceFile = '/home/miguel/Downloads/ne_10m_admin_0_countries.shp'
conn_str = "PG:dbname='%s' host='%s' port='%s' user='%s' password='%s'" % (database,serverName,port,usr,pw)

def testLoad(serverDS, table, sourceFile):
    ogr.RegisterAll()
    shapeDS = ogr.Open(sourceFile)
    sourceLayer = shapeDS.GetLayerByIndex(0)
    options = []
    newLayer = serverDS.CreateLayer(table,sourceLayer.GetSpatialRef(),ogr.wkbUnknown,options)
    for x in xrange(sourceLayer.GetLayerDefn().GetFieldCount()):
        newLayer.CreateField(sourceLayer.GetLayerDefn().GetFieldDefn(x))

    newLayer.StartTransaction()

    for x in xrange(sourceLayer.GetFeatureCount()):
        newFeature = sourceLayer.GetNextFeature()
        newFeature.SetFID(-1)
        newLayer.CreateFeature(newFeature)
        if x % 128 == 0:
            newLayer.CommitTransaction()
            newLayer.StartTransaction()

    newLayer.CommitTransaction()
    return newLayer.GetName()


ogrds = ogr.Open(conn_str)
name = testLoad(ogrds,'countries4',sourceFile)
