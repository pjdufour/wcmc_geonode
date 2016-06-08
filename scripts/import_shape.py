#!/usr/bin/python
import sys
import os
import os.path  
import psycopg2
import osgeo.ogr
from os.path import basename
import pdb
from subprocess import call
from geoserver.catalog import Catalog
from osgeo import osr

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
sourceFile = sys.argv[1]
if len(sys.argv) > 2:
    epsg = sys.argv[1]
else:
    epsg = '4326'

conn_str = "PG:dbname='%s' host='%s' port='%s' user='%s' password='%s'" % (database,serverName,port,usr,pw)

def table_name(sourceFile):
    file_name = basename(sourceFile)
    return os.path.splitext(file_name)[0]

def testLoad(serverDS, sourceFile, table):
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

def geoserver_config(table, epsg):
	geoserver_url = GEOSERVER_URL
	geoserver = OGC_SERVER['default']
	geoserver_user = geoserver['USER']
	geoserver_pwd = geoserver['PASSWORD']

	cat = Catalog( geoserver_url + "rest", geoserver_user, geoserver_pwd)
	ds = cat.get_store("datastore")
	cat.publish_featuretype(table, ds, 'EPSG:' + epsg, srs='EPSG:4326')
	call(["geonode", "updatelayers", "-f", table])


ogrds = ogr.Open(conn_str)
table_name = table_name(sourceFile)
name = testLoad(ogrds,sourceFile, table_name)
geoserver_config(table_name, epsg)
