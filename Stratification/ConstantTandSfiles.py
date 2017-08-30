import os

import numpy as np

import matplotlib.pyplot as plt

from scipy.stats import nanmean

from math import *

import struct


def iniTracerCnt(xsize, ysize, CntVal, Depth ):
    # Generate constant nutrient profile  
    
    tracer = np.ones((xsize, ysize, len(Depth)))
    tracer = tracer*CntVal
    

    return tracer


## Main program ##
dt = np.dtype('>f8')  # float 64 big endian

nx = 360
ny = 360
nz = 90

# Depth values
depth = [5.,20.,30.,50.,70.,100.,150.,170.,200.,300.,400.,500.,600.,700.,800.,1000.,1200.] #values form interp nutrient data 
                                                                                            # from Falkor (see NutrientProfilesFalkor.ipynb)
## 90 layers
zi = (5,10,15,20,25,30,	35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,180,190,200,210,220,230,240,250,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680,700,720,740,760,780,800,820,840,860,880,900,920,940,960,980,1000,1020,1040,1060,1080,1100,1120,1140,1160,1180,1200)


#Temperature
Temp = iniTracerCnt(nx,ny,9.0,zi)

# Save binary file
tmpfile = "%dx%dx%d/Cnttmp%dzlev_%dx%d.bin" %(nx,ny,nz,nz,nx,ny)
fileobj = open(tmpfile,mode='wb')
Temp2 = Temp.transpose((2,0,1)) # To keep fortran order when writing as C binary
print(np.shape(Temp2))
Temp2.astype(dt).tofile(fileobj,"")
fileobj.close()


### PLOT
plt.rcParams['contour.negative_linestyle']='solid'

plt.figure(figsize=(8,6))

CS = plt.plot(np.squeeze(Temp[60,45,:]),zi,'bo-')

plt.gca().invert_yaxis()
    
plt.xlabel('T ($^{\circ}C$)')
    
plt.ylabel('Depth (m)')
    
plt.title('Temperature initial profile ')

plt.show()

#Salinity


Sal = iniTracerCnt(nx,ny,33.0,zi)

# Save binary file
tmpfile = "%dx%dx%d/Cntsal%dzlev_%dx%d.bin" %(nx,ny,nz,nz,nx,ny)
fileobj = open(tmpfile,mode='wb')
Sal2 = Sal.transpose((2,0,1)) # To keep fortran order when writing as C binarynp.asfortranarray(Sal)
Sal2.astype(dt).tofile(fileobj,"")
fileobj.close()

### PLOT Contour

plt.rcParams.update({'font.size':14})
plt.rcParams['contour.negative_linestyle']='solid'

plt.figure(figsize=(8,6))

CS = plt.plot(np.squeeze(Sal[60,45,:]),zi,'bo-')

plt.gca().invert_yaxis()
    
plt.xlabel('Salinity')
    
plt.ylabel('Depth (m)')
    
plt.title('Salinity initial profile ')

plt.show()

