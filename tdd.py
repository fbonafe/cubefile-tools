from cube import *
import sys

path = './'
orb1 = str(sys.argv[1])
orb2 = str(sys.argv[2])
wfc0 = readCube(path+'wp-1-1-'+orb1+'-real.cube')
wfc1 = readCube(path+'wp-1-1-'+orb2+'-real.cube')
transDip = transDipole(wfc0,wfc1)
writeDens(transDip,path+'wp-1-1-'+orb1+'-real.cube','tdd-'+orb1+'-'+orb2+'.cube')
