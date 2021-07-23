#!/usr/bin/env python3
"""
This program prints the GDSII 2D layout file Cell References

The program takes one argument, a path to a GDSII file.
"""
import sys # read command-line arguments
import gdspy # open gds file

# get the input file name
if len(sys.argv) < 2: # sys.argv[0] is the name of the program
    print("Error: need exactly one file as a command line argument.")
    sys.exit(0)
GDS_FILE = sys.argv[1]

print(f"Reading = {GDS_FILE}")
gds = gdspy.GdsLibrary(infile=GDS_FILE)
top_cell = gds.top_level()[0]
print("Parsed GDS")

bbox = list(top_cell.get_bounding_box().flatten())
print(f"Top-cell bounding box = {bbox}")
assert set().union(*[x.properties.keys() for x in top_cell.references]) == {98}

cells = [(x.ref_cell.name, x.properties[98]) for x in top_cell.references]
cells.sort();
for x in cells:
    print(f"%s\t%s" % (x[0], x[1]));

