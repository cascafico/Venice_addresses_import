# addressed update 

# aggiunge tag source=pippo
add_source = False
source = 'Comune-di-Milano'

# do not add unique reference IDs to OSM?

# aggiunge tag ref:<dataset_id>=<id del Comune di Milano (IDMASTER)>
# True -> relying only on geometric matching every time
no_dataset_id = True
dataset_id = 'ds634'

# Overpass query to use when searching OSM for data
#overpass_timeout = 120 default
overpass_timeout = 300
#query = [('amenity', 'fuel'),('waterway', 'fuel')] both conditions
#query = [('amenity', 'fuel')],[('waterway', 'fuel')]  or condition
#query = [('amenity', 'fuel'),('disused:amenity','fuel')]  namespace disused and abandoned are implicit
#query = [('addr:housenumber','.*')] 
#query = [('addr:housenumber','~.*')]  e se lettera e interno non hanno stesso case?
#query = [('addr:street','~.*'),('addr:city','Milano')] non tutti hanno city valorizzato
query = [('addr:street','~.*')] 

# alternatively, parameter --osm export.osm will use indipendently generated queries, ie:
# http://overpass-turbo.eu/s/S17
# use wget -O manual-query.osm <http_addr obtained exporting compact query>

bbox = True


# tags to replace on matched OSM objects
master_tags = ('addr:housenumber', 'addr:street')

# delete_unmatched = True cancellerebbe anche i POI con indirizzo
delete_unmatched = False
tag_unmatched = { 'fixme':'this addr is suppressed from ds634-20200320 dataset or in wrong position: please check in range +10 meters' }


# max distance to search for a match in meters (default 100)
# max_distance = 10 several housenumbers in polygon centriod unmatched... wider distance
max_distance = 20

# max distance to consider dataset duplicates
duplicate_distance = 2
