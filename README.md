Some tools to extract and analize information from CUBE files, including coordinates, number of voxels and density (or wavefunction).
cube.py has several methods to load and analyze cube data.
plotters.py has special plotting functions for cube data.
tdd.py is a script to calculate the transition dipole density [see J. Phys. Chem. A 2011 115 (44), 12280-12285], it works with cube files generated by the waveplot utility of DFTB+, it works as follows:
python tdd.py n1 n2
where n1 and n2 are the indeces of the orbitals involved in the transition.
