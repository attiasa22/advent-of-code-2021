import numpy as np

"""Day 6 of https://adventofcode.com 2021 challenge"""
def increasing_measurements(lines_file):    
    with open(lines_file, "r", encoding="utf-8") as lines:
        
        for value in lines:
            value = sorted(list(map(int, value.split(","))))
        mean = np.mean(np.asarray(value))
        fuel = 0
        print(mean)

        for position in value:
            fuel += sum(range(1,1+abs(position-int(mean))))
           
        print(fuel)
            
            
           
               
if __name__ == "__main__":
    print(increasing_measurements('day7/crabs.txt'))
