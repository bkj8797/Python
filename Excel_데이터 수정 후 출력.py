import numpy as np
import pandas as pd

crimeanal_police = pd.read_csv("02. crime_in_Seoul.csv", thousands = ',', encoding='euc-kr')
crimeanal_police.head()

station_name = []
for name in crimeanal_police['관서명'] :
    station_name.append('서울' + str(name[:-1]) + '경찰서')  
# station_name

station_address = []
station_lat = []
station_lng = []

for name in station_name : 
    tmp = gmaps.geocode(name, language = 'ko')
    station_address.append(tmp[0].get("formatted_address"))
    
    tmp_loc = tmp[0].get("geometry")
    
    station_lat.append(tmp_loc['location']['lat'])
    station_lng.append(tmp_loc['location']['lng'])
    
    print(name + '---------->' + tmp[0].get("formatted_address"))