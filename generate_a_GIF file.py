# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:50:07 2020

@author: LENOVO
"""


import PIL
import numpy as np
image_frames = []
days =np.arange(1,366)

for k in days:
    new_frame = PIL.Image.open(r'E:\Chintan\Python\Displaying the Temparature Data in a Map\Rainfall\jpegs' + '\\' + str(k) + '.jpg')
    image_frames.append(new_frame)    
    

image_frames[0].save('rainfall2015.gif', format = 'GIF', append_images = image_frames[1: ],
                     save_all = True, duration = 200,
                     loop = 0)