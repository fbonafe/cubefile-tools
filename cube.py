"""
These functions extract all the useful information from the Gaussian CUBE file
and analize it.
"""

import sys

def readCube(filename):
    
    class CubeFile:
        def __init__(self,coordsx,coordsy,coordsz,x0,y0,z0,pointsx,pointsy,pointsz,voldx,voldy,voldz,isovals):
            self.x0=x0
            self.y0=y0
            self.z0=z0
            self.coords_x=coordsx
            self.coords_y=coordsy
            self.coords_z=coordsz
            self.nx=pointsx
            self.ny=pointsy
            self.nz=pointsz
            self.dx=voldx
            self.dy=voldy
            self.dz=voldz
            self.dv=voldx*voldy*voldz
            self.isovals=isovals
    
    f = open(filename, "r")
    bohr_to_angst = 0.529177
    #skipping comment lines
    f.readline()
    f.readline()
    
    #reading the number of atoms and the origin of the cube
    l = f.readline().split()
    n_atoms = int(l[0])
    x_origin = float(l[1])
    y_origin = float(l[2])
    z_origin = float(l[3])
    
    #reading number of volume elements and their volume
    cubic_box = True
    l = f.readline().split()
    points_x = int(l[0])
    vol_dx = float(l[1])
    if float(l[2])!=0.0 or float(l[3])!= 0.0:
        cubic_box = False
    l = f.readline().split()
    points_y = int(l[0])
    vol_dy = float(l[2])
    if float(l[1])!=0.0 or float(l[3])!= 0.0:
        cubic_box = False
    l = f.readline().split()
    points_z = int(l[0])
    vol_dz = float(l[3])
    if float(l[1])!=0.0 or float(l[2])!= 0.0:
        cubic_box = False
    if cubic_box == False:
        print "Non-cubic box, cannot continue!"
        sys.exit()
#    volume_element = vol_dx * vol_dy * vol_dz
    
    #reading atomic coordinates
    coords_x = []
    coords_y = []
    coords_z = []
    for i in range(n_atoms):
        co = f.readline().split()
        coords_x.append(bohr_to_angst * float(co[2]))
        coords_y.append(bohr_to_angst * float(co[3]))
        coords_z.append(bohr_to_angst * float(co[4]))
    
    #memory consuming but easy
    isovalues = [] 
    for line in f:
        spl = line.split()
        for v in spl:
            isovalues.append(float(v))
            
    return CubeFile(coords_x,coords_y,coords_z,x_origin,y_origin,z_origin,points_x,points_y,points_z,vol_dx,vol_dy,vol_dz,isovalues)
    
def genGrid(CubeFile):
    class Grid:
        def __init__(self,x,y,z,isoval):    
            self.x=x
            self.y=y
            self.z=z
            self.isoval=isoval
            
    bohr_to_angst = 0.529177
    xs = []
    ys = []
    zs = []
    for ix in range(CubeFile.nx):
        for iy in range(CubeFile.ny):
            for iz in range(CubeFile.nz):
               x = bohr_to_angst * (CubeFile.x0 + ix * CubeFile.dx)
               y = bohr_to_angst * (CubeFile.y0 + iy * CubeFile.dy)
               z = bohr_to_angst * (CubeFile.z0 + iz * CubeFile.dz)
               xs.append(x)
               ys.append(y)
               zs.append(z)
    return Grid(xs,ys,zs,CubeFile.isovals)
    
def plotXY(CubeFile,isovalues):
    class Grid:
        def __init__(self,x,y,isoval):    
            self.x=x
            self.y=y
            self.isoval=isoval
            
    bohr_to_angst = 0.529177
#    isovalues=CubeFile.isovals
#    aux = list(isovalues)
    isovalues.reverse()
    xs = []
    ys = []
    dens = []    
    for ix in range(CubeFile.nx):
        for iy in range(CubeFile.ny):
            x = bohr_to_angst * (CubeFile.x0 + ix * CubeFile.dx)
            y = bohr_to_angst * (CubeFile.y0 + iy * CubeFile.dy)
            intdens=0.
            for iz in range(CubeFile.nz):
               val = isovalues.pop()
               intdens += val
            intdens=intdens*CubeFile.dz
            xs.append(x)
            ys.append(y)
            dens.append(intdens)
#    CubeFile.isovals = aux
    return Grid(xs,ys,dens)