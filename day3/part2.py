"""Day 3 of https://adventofcode.com 2021 challenge"""

from os import chown


def find_power_consumption(diagnostic_report_file):
    '''Find the power consumption of a submarine given a series of binary numbers'''
    root = dict()
    _end = '_end_'
    with open(diagnostic_report_file, "r", encoding="utf-8") as energy_readings:
        bit_counts = [0] * (energy_readings.readline().index('\n')+1)
        for value in energy_readings:

            digits = [int(a) if int(a) else -1 for a in str(value).strip()]
            bit_counts = [a + b for a, b in zip(bit_counts, digits)]
            current_dict = root
            for letter in value:
                current_dict = current_dict.setdefault(letter, {})
                current_dict[_end] = _end
        gamma = ''.join(map(str,[1 if a>0 else 0 for a in bit_counts]))
        epsilon = ''.join(map(str,[0 if a>0 else 1 for a in bit_counts]))
   
        o2_level = determine_value(gamma, root, bit_counts)
        co2_level = determine_value(epsilon, root, bit_counts)
        print("bit counts ")
        print(bit_counts)     
        print("--")     
        print(len(o2_level))    
        print(o2_level)  
        print(co2_level)  
        print("--")   
        o2_level = int(o2_level.strip(),2)
        co2_level = int(co2_level.strip(),2)

    return o2_level * co2_level
def determine_value(phrase, root, bit_counts):
    print("Phrase")
    print(phrase)
    answer=""
    for i in range(len(phrase)+2):
            is_trie, current_dict = in_trie(root, phrase[0:i+1])
            answer = phrase[0:i+1]
            if len(current_dict.keys()) ==2 :
                while len(answer) != len(bit_counts):
                    answer += list(current_dict.keys())[1]
                    current_dict = current_dict[answer[-1]]
                return answer
            
                
                
def in_trie(trie, word):
    current_dict = trie
    for letter in word:
        if letter not in current_dict:
           return False, current_dict
        current_dict = current_dict[letter]
    return True, current_dict

if __name__ == "__main__":
    print(find_power_consumption('day3/readings2.txt'))
    