import os
import sys

def startFile(path):
    with open(path,'w') as file:
        file.write("G21;\nG91;\n")
    return

def endFile(path):
    with open(path,'a') as file:
        file.write("M84;\nG02;\n")
    return

def drillBounce(path, depth, plungeD, rise):
	#depth = 10
    #plungeD = 0.5
    #rise=0.1
    
    h = depth
    with open(path,'a') as file:
        #print(h)
        #file.write("G21;\nG91;\n")
        while h > plungeD:
            file.write(f"G01 Z-{plungeD} F80;\n")
            file.write(f"G01 Z{rise};\n")
            #print(f"\tG01 Z-{plungeD} F80;\n")
            #print(f"\tG01 Z{rise};\n")
            #print("Hcurrent"+str(h-plungeD+rise))
            h = h - plungeD + rise
        
        file.write(f"G01 Z-{h} F80;\n")
        #file.write(f"G01 Z{rise};\n")
        #print(f"\tG01 Z-{h} F80;")
        h = 0
        #print("Hcurrent"+str(h))
        
        #file.write("M84;\nG02;\n")
        
    return