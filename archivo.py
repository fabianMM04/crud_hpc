#!/usr/bin/python

def crear(executable,universe,inputt,output):
    str(executable)
    str(universe)
    str(inputt)
    str(output)
    
    fo = open("foot.submit", "w")
    fo.write("executable = ")
    fo.write(executable)
    fo.write("\n")
    fo.write("universe = ")
    fo.write(universe)
    fo.write("\n")
    fo.write("input = ")
    fo.write(inputt)
    fo.write("\n")
    fo.write("output = ")
    fo.write(output)

# Close opend file
    fo.close()

