import numpy as np

"""Day 6 of https://adventofcode.com 2021 challenge"""
def increasing_measurements(lines_file):    
    with open(lines_file, "r", encoding="utf-8") as lines:
        days = [0]*9
        for value in lines:
            value = list(map(int, value.split(",")))
        
        for day in value:
            days[day] += 1
        for i in range(256):
            zero_fish_count = days.pop(0)
            days[6]+= zero_fish_count
            days.append(zero_fish_count)
            print(np.asarray(days).sum())
           
           
               
if __name__ == "__main__":
    #np.set_printoptions(threshold=300)
    print(increasing_measurements('day6/lanternfish.txt'))
