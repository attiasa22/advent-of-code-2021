"""Day 3 of https://adventofcode.com 2021 challenge"""

from os import chown


def find_power_consumption(diagnostic_report_file):
    '''Find the power consumption of a submarine given a series of binary numbers'''
    
    with open(diagnostic_report_file, "r", encoding="utf-8") as energy_readings:
        bit_counts = [0] * energy_readings.readline().index('\n')
        beginning0 = []
        beginning1 = []
        for line in energy_readings:
            digits = [int(a) if int(a) else -1 for a in str(line).strip()]
            bit_counts = [a + b for a, b in zip(bit_counts, digits)]
            
            if line[0] == "0":
                beginning0.append(line)
            else:
                 beginning1.append(line)
        
        gamma = ''.join(map(str,[1 if a>=1 else 0 for a in bit_counts]))
        if gamma[0] == "1":
            possibleO2 =  beginning1
            possibleCO2 = beginning0
        else:
            possibleO2 =  beginning0
            possibleCO2 = beginning1
            
        
        o2 = find_measurement(possibleO2, bit_counts, 1)
        co2 = find_measurement(possibleCO2, bit_counts, 0)
        
        o2 = int(o2,2)
        co2 = int(co2,2)
        print(o2*co2)
       
def find_measurement(possible_readings, bit_counts, e_g):       
    counter = 0
    while len((possible_readings)) != 1 and counter< len(bit_counts):
        counter +=1
        beginning0 = []
        beginning1 = [] 
        bit_counts = [0] * len(bit_counts)
        # print((possibleO2))
        #print(counter)
        for reading in possible_readings:
        #    print(reading)
            digits = [int(a) if int(a) else -1 for a in str(reading).strip()]
            bit_counts = [a + b for a, b in zip(bit_counts, digits)]
            if reading[counter] == "0":
                beginning0.append(reading)
            else:
                beginning1.append(reading)
        #print(len(possible_readings))    
        #print(len(beginning0))
        #print(len(beginning1)) 
             
        gamma = ''.join(map(str,[e_g if a>=0 else (e_g-1)*-1 for a in bit_counts]))
        
        #print(bit_counts)
        #print(gamma)
        if gamma[counter] == "1":
            possible_readings =  beginning1
            #possibleCO2 = beginning0
        else:
            possible_readings =  beginning0
    return(possible_readings[0])
            
    
if __name__ == "__main__":
    print(find_power_consumption('day3/readings2.txt'))