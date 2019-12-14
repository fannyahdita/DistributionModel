import pandas as pd
import googlemaps
import time

start_time = time.time()

df = pd.read_csv(r'C:\Users\HP\Desktop\data.csv', delimiter=',')

API_key = 'AIzaSyBdUM-15Fz24K9QZuRpPo4-oZIAqm3-Z-U'
gmaps = googlemaps.Client(key=API_key)

# print(df['Latitude'][2])

origins = []
dests = []
distances = []

for i in df['Coordinate'] :
    for j in df['Coordinate'] :
        origins_coor = i.split('|')
        dest_coor = j.split('|')

        origin_lat = origins_coor[0]
        origin_long = origins_coor[1]

        dest_lat = dest_coor[0]
        dest_long = dest_coor[1]

        origins.append(i)
        dests.append(j)

        r = gmaps.distance_matrix([str(origin_lat) + " " + str(origin_long)], [str(dest_lat) + " " + str(dest_long)])['rows'][0]['elements'][0]

        distance = r['distance']['value']

        distances.append(distance)

df_result = pd.DataFrame(data={"origins" : origins, "destinations" : dests, "distance" : distances })
df_result.to_csv(r'C:\Users\HP\Desktop\data_distance.csv', sep=',', index=False)
print("--- %s seconds ---" % (time.time() - start_time))



