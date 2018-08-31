#!/usr/bin/python
import sys
import matplotlib.image as im
import matplotlib.pyplot as plot
import numpy as np

input=sys.argv[1]

A = im.imread(input)
#plot.subplot(121)
#plot.imshow(A)
#print(A[:1,:1,:])
B = A/2
C = B.astype(np.uint8)
#print(C[:1,:1,:])
#plot.subplot(122)
#plot.imshow(C)
#plot.imsave('Q2.jpg',C,vmin=0,vmax=255,format='jpg')
plot.imsave('Q2.jpg',C)
