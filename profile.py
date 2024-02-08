# addressed update 

# aggiunge tag source=pippo
add_source = False
source = 'Comune-di-Venezia'

# do not add unique reference IDs to OSM?

# aggiunge tag ref:<dataset_id>=<id del Comune di Venezia>
# True -> relying only on geometric matching every time
no_dataset_id = True
dataset_id = 'Strato03_GestioneViabilita_Indirizzi'

# Overpass query to use when searching OSM for data
#overpass_timeout = 120 default
overpass_timeout = 300
#query = [('addr:housenumber','.*')] 
#query = [('addr:housenumber','~.*')]  e se lettera e interno non hanno stesso case?
#query = [('addr:street','~.*'),('addr:city','Milano')] non tutti hanno city valorizzato
query = [('addr:housenumber','~.*')] 
# do not comment: seems needed even if external --osm data

# alternatively, parameter --osm export.osm will use indipendently generated queries, ie:
# http://overpass-turbo.eu/s/S17
# use wget -O manual-query.osm <http_addr obtained exporting compact query>

bbox = True
max_request_boxes = 32


# tags to replace on matched OSM objects
master_tags = ('addr:housenumber', 'addr:street', 'addr:place')
#master_tags = ('addr:street')

# delete_unmatched = True cancellerebbe anche i POI con indirizzo
delete_unmatched = False
tag_unmatched = { 'fixme':'Maybe addr is plate in wrong position: please check' }


# max distance to search for a match in meters (default 100)
# max_distance = 10 several housenumbers in polygon centriod unmatched... wider distance
max_distance = 5

# max distance to consider dataset duplicates
duplicate_distance = 2
