import numpy as np

"""Day 8 of https://adventofcode.com 2021 challenge"""
def increasing_measurements(lines_file):    
    with open(lines_file, "r", encoding="utf-8") as lines:
        for value in lines:
            value = value.split("|")
            digits =  value[0].split()
            numbers = value[1].split()
            unknowns = []
            for digit in digits:
                if len(digit) == 2:
                    one = digit
                elif len(digit) == 4:
                    four = digit
                elif len(digit) == 3:
                    seven = digit
                elif len(digit) == 7:
                    eight =digit
                else:
                    unknowns.append(digit)
            print(one, four, seven, eight)
            print(unknowns)
            
            #
               
if __name__ == "__main__":
    print(increasing_measurements('day8/numbers.txt'))
