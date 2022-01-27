import pandas as pd
import re
from tqdm import tqdm
import numpy as np


data = pd.read_csv('artists.csv', dtype={"artist_mb": "string"})
data = data.loc[data['country_mb'].isin(['United States', 'United Kingdom', 'Canada', 'Australia'])]
data = data['artist_lastfm']
data = data.dropna()
artists = data.unique()
artist_list = []
for artist in tqdm(artists):
    try:
        cur_artist = re.sub(r'[^A-Za-z ]+', '', artist)
        cur_artist = cur_artist.strip()
    except:
        break
    # print (cur_artist)
    if len(cur_artist) > 2 and ' ' not in cur_artist:
        artist_list.append(cur_artist)
artist_list = np.unique(artist_list)
print (len(artist_list))
index = np.random.choice(artist_list.shape[0], 10000, replace=False)
artist_list = artist_list[index]
print (len(artist_list))
with open('artist_name.txt', 'w') as f:
    for item in artist_list:
        f.write("%s\n" % item)
