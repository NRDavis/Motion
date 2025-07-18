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

def bounceZ(path, depth, plungeD, rise, moveSpeed):
	#depth = 10
    #plungeD = 0.5
    #rise=0.1
    
    h = depth
    with open(path,'a') as file:
        #print(h)
        #file.write("G21;\nG91;\n")
        while h > plungeD:
            file.write(f"G01 Z-{plungeD} F{moveSpeed};\n")
            file.write(f"G01 Z{rise};\n")
            #print(f"\tG01 Z-{plungeD} F80;\n")
            #print(f"\tG01 Z{rise};\n")
            #print("Hcurrent"+str(h-plungeD+rise))
            h = h - plungeD + rise
        
        file.write(f"G01 Z-{h} F{moveSpeed};\n")
        #file.write(f"G01 Z{rise};\n")
        #print(f"\tG01 Z-{h} F80;")
        h = 0
        #print("Hcurrent"+str(h))
        
        #file.write("M84;\nG02;\n")
        
    return

def liftZ(path, offset, moveSpeed):
    with open(path,'a') as file:
            file.write(f"G01 Z{offset} F{moveSpeed};\n")
    return

def spindleOn(path, spindleSpeed):
    with open(path,'a') as file:
            file.write(f"M03 S{spindleSpeed};\n")
    return

def spindleOff(path):
    with open(path,'a') as file:
            file.write(f"M05;\n")
    return

#def patternRec(path, rows, cols, spacingX, spacingY, depth, moveSpeed):
def drillPatternRec(path,startX, startY, endX, endY, depth, rows, cols, moveSpeed, spindleSpeed=None, action=None):
    # move to relative position first
    xSpacing = (endX-startX)/(rows-1)
    ySpacing = (endY-startY)/(cols-1)
    
    with open(path,'a') as file:
        # Ensure system is set to relative movements
        file.write(f"G21;\n")
        # Turn Spindle On, if not zero
        if spindleSpeed is not None:
            file.write(f"M03 S{spindleSpeed};\n")
        
        r = 0
        while r < rows:
            c = 0
            
            while c < (cols):
                print(f"({r},{c})")
                if r%2 == 1:
                    sign = "-"
                else:
                    sign = ""
                # Drill
                file.write(f"G01 Z-{depth} F{moveSpeed};{r},{c}\n")
                #file.write(f"G01 Z-{depth} F{moveSpeed};\n")
                # Lift Z back to original height
                file.write(f"G01 Z{depth} F{moveSpeed};\n")
                # Move to next Column
                c = c + 1
                if c < cols:
                    file.write(f"G01 X{sign}{xSpacing} F{moveSpeed};{c-1}\n")
                    #file.write(f"G01 X{sign}{xSpacing} F{moveSpeed};\n")
                
            #advance Y, advance to next row
            r = r + 1
            if r < rows:
                file.write(f"G01 Y{ySpacing} F{moveSpeed};\n")
                
        # turn spindle off
        if spindleSpeed is not None:
            file.write(f"M05;\n")
    
    return
    
def actionPatternRec(path,startX, startY, endX, endY, rows, cols, action=None):
    # move to relative position first
    xSpacing = (endX-startX)/(rows-1)
    ySpacing = (endY-startY)/(cols-1)
    
    with open(path,'a') as file:
        # Ensure system is set to relative movements
        file.write(f"G21;\nG91;\n")

        r = 0
        while r < rows:
            c = 0
            
            while c < (cols):
                #print(f"({r},{c})")
                if r%2 == 1:
                    sign = "-"
                else:
                    sign = ""
                # insert Action Code
                if action is not None:
                    file.write(action)
                else:
                    file.write(";\n")
                # Move to next Column
                c = c + 1
                if c < cols:
                    file.write(f"G00 X{sign}{xSpacing};\n")
                
            #advance Y, advance to next row
            r = r + 1
            if r < rows:
                file.write(f"G00 Y{ySpacing};\n")

    return