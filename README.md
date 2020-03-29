wiki page
https://wiki.openstreetmap.org/wiki/Import/Catalogue/Milan_addresses_import

audit map
http://audit.osmz.ru/project/MI-addrs/


workflow example:

query overpass http://overpass-turbo.eu/s/S2Q

wget -O addresses.osm "http://overpass-api.de/api/interpreter?data=%5Bout%3Axml%5D%5Btimeout%3A25%5D%3Barea%5B%22name%22%3D%22Milano%22%5D%5B%22admin%5Flevel%22%3D%228%22%5D%2D%3E%2EsearchArea%3B%28nwr%5B%22addr%3Ahousenumber%22%5D%28area%2EsearchArea%29%3B%29%3Bout%20meta%20qt%20center%3B%0A"

conflate -i ds634_civici_coordinategeografiche_20200302.json --osm addresses.osm -v  -c preview-10mt.json profile.py
