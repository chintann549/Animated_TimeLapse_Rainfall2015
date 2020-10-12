# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:16:32 2020

@author: LENOVO
"""


from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
data = Dataset(r'E:\Chintan\Python\Displaying the Temparature Data in a Map\Rainfall\rawdata\APHRO_MA_025deg_V1101_EXR1.2015.nc')
lats = data.variables['lat'][:]
lons = data.variables['lon'][:]
time = data.variables['time'][:]
precip = data.variables['precip'][:]
map = Basemap(projection = 'merc', 
             llcrnrlon = 64.45,
             llcrnrlat = 7.05,
             urcrnrlon = 103.50,
             urcrnrlat = 42.24, 
             resolution = 'i')
map1 = Basemap(projection = 'merc', 
             llcrnrlon = 62.8,
             llcrnrlat = -2,
             urcrnrlon = 105.37,
             urcrnrlat = 38.78, 
             resolution = 'i') 
lon, lat = np.meshgrid(lons, lats)
x,y = map1(lon,lat)

days = np.arange(0,365)

for i in days:
    
    c_scheme = map1.pcolor(x, y, np.squeeze(precip[i,:,:]), cmap ='jet')
    # draw coastlines, country boundaries, fill continents.
    # draw coastlines, country boundaries, fill continents.
    map1.drawcoastlines()
    map1.drawcountries()
    map1.drawstates()
    #map.fillcontinents(color='coral',lake_color='aqua')
    # draw the edge of the map projection region (the projection limb)
    #map1.drawmapboundary(fill_color='white')
    # draw the edge of the map projection region (the projection limb)
    cbar = map1.colorbar(c_scheme, location = 'right', pad = '5%')
    day = i+1
    plt.title('Average Rainfall Day ' + str(day) + ' of Year 2015')
    plt.clim(0, 200)
    plt.savefig(r'E:\Chintan\Python\Displaying the Temparature Data in a Map\Rainfall\jpegs' + '\\' + str(day) + '.jpg', dpi=300)
    plt.clf()