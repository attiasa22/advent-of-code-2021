"""Day 3 of https://adventofcode.com 2021 challenge"""

def find_power_consumption(diagnostic_report_file):
    '''Find the power consumption of a submarine given a series of binary numbers'''
    with open(diagnostic_report_file, "r", encoding="utf-8") as energy_readings:
        bit_counts = [0] * energy_readings.readline().index('\n')
        for value in energy_readings:
            digits = [int(a) if int(a) else -1 for a in str(value).strip()]
            bit_counts = [a + b for a, b in zip(bit_counts, digits)]

        gamma = ''.join(map(str,[1 if a>=1 else 0 for a in bit_counts]))
        epsilon = ''.join(map(str,[0 if a>=1 else 1 for a in bit_counts]))

        gamma = int(gamma,2)
        epsilon = int(epsilon,2)

    return gamma * epsilon

if __name__ == "__main__":
    print(find_power_consumption('day3/readings.txt'))
    