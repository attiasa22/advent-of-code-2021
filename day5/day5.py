import numpy as np
import sys
import re
"""Day 5 of https://adventofcode.com 2021 challenge"""
def increasing_measurements(lines_file):
    '''Determine if sonar depth readings are increasing relative to the previous reading'''
    seabed = np.zeros((1000, 1000))
    
    with open(lines_file, "r", encoding="utf-8") as lines:
        for value in lines:
            value = re.split("-> |,|\n", value)
            x1, y1 = int(value[0]), int(value[1])
            x2, y2 = int(value[2]), int(value[3])
            
            
            if x1 == x2:
                y1, y2 = min(y1,y2), max(y1,y2)
                #print(x1,y1,x2,y2)
                seabed[y1 :y2+1,x2] = seabed[y1 :y2+1,x2]+1
                #print(seabed[y1 :y2+1,x2])
            elif y1 == y2:
                x1, x2 = min(x1,x2), max(x1,x2)
                #print(value)
                seabed[y1, x1:x2+1] = seabed[y1, x1:x2+1]+1
            
            elif abs(x2-x1) ==abs(y2-y1):
                if x1<x2:
                    current_pos_y = y1
                    current_pos_x = x1
                    if y1<y2:
                        
                        while current_pos_y <=y2:
                            seabed[current_pos_y,current_pos_x]=seabed[current_pos_y,current_pos_x]+1
                            current_pos_y += 1
                            current_pos_x += 1
                    else:
                         while current_pos_y >=y2:
                            seabed[current_pos_y,current_pos_x]=seabed[current_pos_y,current_pos_x]+1
                            current_pos_y -= 1
                            current_pos_x += 1
                else: #x1>x2
                    current_pos_y = y1
                    current_pos_x = x1
                    if y1<y2:
                        
                        while current_pos_y <=y2:
                            seabed[current_pos_y,current_pos_x]=seabed[current_pos_y,current_pos_x]+1
                            current_pos_y += 1
                            current_pos_x -= 1
                    else:
                        print(value)
                        while current_pos_y >=y2:
                            seabed[current_pos_y,current_pos_x]=seabed[current_pos_y,current_pos_x]+1
                            current_pos_y -= 1
                            current_pos_x -= 1
           
        print((np.asarray(seabed) >= 2).sum())

if __name__ == "__main__":
    #np.set_printoptions(threshold=300)
    print(increasing_measurements('day5/lines.txt'))

