'''
This is a list of prepared endpoints to load data from into our applications.

These have been chosen from: https://opendata.london.ca/search
For the purpose of building a pokemon go-esque app to help people find interesting places to go to 
alleviate load on public parks while mantaining social distancing during these times

Next Steps: download these endpoints into the NoSQL Server
'''

'''
This is logistical information such as the boundary of the city
'''
LONDON_CANADA_CITY_BOUNDARY = 'https://opendata.arcgis.com/datasets/e81aed234f8b4bbeaa3bd9e72acc4b64_51.geojson'
PLANNING_DISTRICTS = 'https://opendata.arcgis.com/datasets/5e086120a5c54832b7aa358887f388a8_18.geojson'

'''
These are points of interest throughout the city that have been deemed a historical site
'''
HERITAGE_CONSERVATION_DISTRICTS = 'https://opendata.arcgis.com/datasets/accdfc5946194f1cad7507ca322e5c7a_6.geojson'
HISTORIC_LOTS_AND_CONCESSIONS = 'https://opendata.arcgis.com/datasets/6407cdb40ec342ac8d17587eb530dc76_8.geojson'
HISTORIC_SITES = 'https://opendata.arcgis.com/datasets/42c3ef4f1e814262a5f32d3ee0a01fa9_9.geojson'
HERITAGE_PARCELS = 'https://opendata.arcgis.com/datasets/ac8425f044e1477b849c53f37df11eff_7.geojson'
CEMETARIES = 'https://opendata.arcgis.com/datasets/5b2d9f05ae964c8e8075903ef8b7d540_5.geojson'

'''
These are paths, trails, walking places of interest
'''
WALKWAYS = 'https://opendata.arcgis.com/datasets/687a84ceb6f0415d9188a5992afa5234_6.geojson'
BICYCLE_ROUTES_AND_WALKING_TRAILS = 'https://opendata.arcgis.com/datasets/a1c044cbeb5c4030909764177cd35a26_2.geojson'
BIKE_ROUTES_ON_STREET = 'https://opendata.arcgis.com/datasets/b9ccfd746f2640b78cc18d2b78ef586a_20.geojson'
SIDEWALKS = 'https://opendata.arcgis.com/datasets/6dc013901d03481c822f1e0d0af4e7fa_4.geojson'
SIDEWALKS_TOPO = 'https://opendata.arcgis.com/datasets/932f50c6fe054483a7b782c0b6acf2ac_34.geojson'
TRAILS = 'https://opendata.arcgis.com/datasets/b5928e87da664758b72cdd3571c6e722_43.geojson'

SCHOOL_CROSSINGS = 'https://opendata.arcgis.com/datasets/11e0b88ae41d481ca00201e2a55a837e_13.geojson'
INTERSECTION_TYPES = 'https://opendata.arcgis.com/datasets/1c46503e8c0f4874bc8a6bf5bc2f91c8_16.geojson'
PEDESTRIAN_CROSSOVERS = 'https://opendata.arcgis.com/datasets/2ac9c9951f9940c3905c6ee7f9214322_12.geojson'
SIGNAIZED_INTERSECTIONS = 'https://opendata.arcgis.com/datasets/8ee2291c09bc48aaab67b5cf0ad8bc46_14.geojson'

# A linear feature class representing substantial steps significant to the accurate representation of 
# topography within the municipal boundaries of the City of London as identified through aerial imagery.
STEPS = 'https://opendata.arcgis.com/datasets/966dbb5a413645128beacbd1fa9f5972_38.geojson'

PUBLIC_ART = 'https://opendata.arcgis.com/datasets/ff7c7d0cb468473daa95f4cb5753aacc_17.geojson'
TREE_INVENTORY = 'https://opendata.arcgis.com/datasets/4438232044b941ff8591df6f2d287e95_12.geojson'
TREES = 'https://opendata.arcgis.com/datasets/15a0bfc0a5334d52b4b8cf510b954fd4_45.geojson'
LIBRARIES = 'https://opendata.arcgis.com/datasets/bc16dc17fb75479fa7588aa162fb8e22_3.geojson'
PARKS = 'https://opendata.arcgis.com/datasets/83b7006bcc8e43ee88c434a85e5a857e_3.geojson'
PARK_AMENITIES = 'https://opendata.arcgis.com/datasets/716311972be047f39a5937247ed80a2c_1.geojson'

WATERBODIES = 'https://opendata.arcgis.com/datasets/04d375a6836f414e835c2fad405c9643_7.geojson'
WATERCOURSES = 'https://opendata.arcgis.com/datasets/01ba1344b72e41dbb12c4e7f49722303_8.geojson'
WATER = 'https://opendata.arcgis.com/datasets/46d82aeb310147e1b464fafdbea2b868_49.geojson'
WATER_EDGES = 'https://opendata.arcgis.com/datasets/e44b267fa22a43018e19b9880c4c461b_50.geojson'

RACETRACKS = 'https://opendata.arcgis.com/datasets/69139b02d44145559aafa01da47260b8_26.geojson'

# A linear feature class representing the boundaries of solid masonry ruins within the '
# municipal boundaries of the City of London as identified through aerial imagery.
RUINS = 'https://opendata.arcgis.com/datasets/138e2962d4064d278392fc9da5f7d061_31.geojson'
# A linear feature class representing towers within the municipal boundaries of the City of London as identified through aerial imagery.
TOWERS = 'https://opendata.arcgis.com/datasets/ea89158e3029449c8f2a828b80320261_41.geojson'
FIRE_HYDRANTS = 'https://opendata.arcgis.com/datasets/3095f15d0bf449b1aea9987fa3e246c8_10.geojson'

SCHOOLS = 'https://opendata.arcgis.com/datasets/cabb026f825348ae9c606f2c8b013e21_4.geojson'
'''
These are roads which could be used for local pedestrian traffic
'''
SINGLE_LINE_ROADS = 'https://opendata.arcgis.com/datasets/0bacba3c5aa94ad18d2a12d2d9797315_7.geojson'

'''
This is areas of business development areas that we could encourage walkability to to spur local business development
'''
BUSINESS_IMPROVEMENT_AREAS = 'https://opendata.arcgis.com/datasets/c627bb303c664a04ae7225960be761b4_11.geojson'
COMMUNITY_IMPROVEMENT_PROJECT_AREAS = 'https://opendata.arcgis.com/datasets/1b0d11ccf60f4e77b2e86dc98ace1e83_12.geojson'
NEAR_CAMPUS_NEIGHBOURHOOD_AREA = 'https://opendata.arcgis.com/datasets/5eb4a265cbc2428eb9a2e5217249efb3_13.geojson'

'''
This is stuff that seems intersting and warrants another look
'''
BRIDGES = 'https://opendata.arcgis.com/datasets/45bf441fc3104fb7b9af0674c0863a92_9.geojson'
BRIDGES_TOPO = 'https://opendata.arcgis.com/datasets/6f10021f6d1c4d9e863105ece561be65_1.geojson'
RAILWAYS = 'https://opendata.arcgis.com/datasets/10ff4a7c53d14c588f0b905aa04d721b_10.geojson'
RAILWAYS_TOPO = 'https://opendata.arcgis.com/datasets/b98ca617e76449f2a1ddaca1146abfb4_27.geojson'
# A line feature class coded by year digitized, as an estimation for year built, of 
# buildings within the municipal boundaries of the City of London as identified through aerial imagery.
BUILDING_OUTLINES = 'https://opendata.arcgis.com/datasets/f5dd65b8b5fb440ab4092f6c8d2431f7_2.geojson'
# A polygon feature class representing permanent or semi-permanent buildings, larger than 10 
# square meters within the municipal boundaries of the City of London as identified through aerial imagery.
BUILDINGS = 'https://opendata.arcgis.com/datasets/0653b9ffb0034a7f910059b5d7af684b_3.geojson'

DAMS = 'https://opendata.arcgis.com/datasets/190ab18e8b354c77810218acb6d20f17_9.geojson'
DOCKS = 'https://opendata.arcgis.com/datasets/988cf1501eb64ac691a29bc061322842_10.geojson'
OVERHEAD_WALKWAYS = 'https://opendata.arcgis.com/datasets/959f0bcf03484efc9f74b47571128b81_19.geojson'
PUBLIC_POOLS = 'https://opendata.arcgis.com/datasets/69ad77da18b14df9abbb28e622f3448a_25.geojson'
SILOS = 'https://opendata.arcgis.com/datasets/1767602302344bc3b8bed1a97b5a289c_35.geojson'
SMOKESTACKS = 'https://opendata.arcgis.com/datasets/10d768187a7044e49c2d6c24dfff113f_36.geojson'
# A point feature class representing the spot heights with elevation labelling 
# within the municipal boundaries of the City of London as identified through aerial imagery.
SPOT_HEIGHT = 'https://opendata.arcgis.com/datasets/b20be4fb7fb34bcca5d00f17290bb7df_37.geojson'
TRUCK_ROUTES = 'https://opendata.arcgis.com/datasets/12238060346c4471ae92a8c610166549_17.geojson'

EVERYTHING = {'LONDON_CANADA_CITY_BOUNDARY': LONDON_CANADA_CITY_BOUNDARY, 
              'PLANNING_DISTRICTS': PLANNING_DISTRICTS, 
              'HERITAGE_CONSERVATION_DISTRICTS': HERITAGE_CONSERVATION_DISTRICTS, 
              'HISTORIC_LOTS_AND_CONCESSIONS': HISTORIC_LOTS_AND_CONCESSIONS, 
              'HISTORIC_SITES' : HISTORIC_SITES, 
              'HERITAGE_PARCELS' : HERITAGE_PARCELS, 
              'CEMETARIES' : CEMETARIES, 
              'WALKWAYS' : WALKWAYS, 
              'BICYCLE_ROUTES_AND_WALKING_TRAILS' : BICYCLE_ROUTES_AND_WALKING_TRAILS, 
              'BIKE_ROUTES_ON_STREET' : BIKE_ROUTES_ON_STREET, 
              'SIDEWALKS' : SIDEWALKS, 
              'SIDEWALKS_TOPO' : SIDEWALKS_TOPO, 
              'TRAILS' : TRAILS, 
              'SCHOOL_CROSSINGS' : SCHOOL_CROSSINGS, 
              'INTERSECTION_TYPES' : INTERSECTION_TYPES, 
              'PEDESTRIAN_CROSSOVERS' : PEDESTRIAN_CROSSOVERS, 
              'SIGNAIZED_INTERSECTIONS' : SIGNAIZED_INTERSECTIONS, 
              'STEPS' : STEPS, 
              'PUBLIC_ART' : PUBLIC_ART, 
              'TREE_INVENTORY' : TREE_INVENTORY, 
              'TREES' : TREES, 
              'LIBRARIES' : LIBRARIES, 
              'PARKS' : PARKS, 
              'PARK_AMENITIES' : PARK_AMENITIES, 
              'WATERBODIES' : WATERBODIES, 
              'WATERCOURSES' : WATERCOURSES, 
              'WATER' : WATER, 
              'WATER_EDGES' : WATER_EDGES, 
              'RACETRACKS' : RACETRACKS, 
              'RUINS' : RUINS, 
              'TOWERS' : TOWERS, 
              'FIRE_HYDRANTS' : FIRE_HYDRANTS, 
              'SCHOOLS' : SCHOOLS, 
              'SINGLE_LINE_ROADS' : SINGLE_LINE_ROADS, 
              'BUSINESS_IMPROVEMENT_AREAS' : BUSINESS_IMPROVEMENT_AREAS, 
              'COMMUNITY_IMPROVEMENT_PROJECT_AREAS' : COMMUNITY_IMPROVEMENT_PROJECT_AREAS, 
              'NEAR_CAMPUS_NEIGHBOURHOOD_AREA' : NEAR_CAMPUS_NEIGHBOURHOOD_AREA, 
              'BRIDGES' : BRIDGES, 
              'BRIDGES_TOPO' : BRIDGES_TOPO, 
              'RAILWAYS' : RAILWAYS, 
              'RAILWAYS_TOPO' : RAILWAYS_TOPO, 
              'BUILDING_OUTLINES' : BUILDING_OUTLINES, 
              'BUILDINGS' : BUILDINGS, 
              'DAMS' : DAMS, 
              'DOCKS' : DOCKS, 
              'OVERHEAD_WALKWAYS' : OVERHEAD_WALKWAYS, 
              'PUBLIC_POOLS' : PUBLIC_POOLS, 
              'SILOS' : SILOS, 
              'SMOKESTACKS' : SMOKESTACKS, 
              'SPOT_HEIGHT' : SPOT_HEIGHT, 
              'TRUCK_ROUTES' : TRUCK_ROUTES}