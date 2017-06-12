#!/usr/bin/python

def crear(executable,universe,log,output):
    str(executable)
    str(universe)
    str(log)
    str(output)
    sub = executable.split(".")
    
    fo = open(sub[0]+".submit", "w")
    fo.write("executable = ")
    fo.write(executable)
    fo.write("\n")
    fo.write("universe = ")
    fo.write(universe)
    fo.write("\n")
    fo.write("log = ")
    fo.write(log)
    fo.write("\n")
    fo.write("output = ")
    fo.write(output)

# Close opend file
    fo.close()
    



