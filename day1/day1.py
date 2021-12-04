"""Day 1 of https://adventofcode.com 2021 challenge"""
def increasing_measurements(sonar_readings_file):
    '''Determine if sonar depth readings are increasing relative to the previous reading'''
    with open(sonar_readings_file, "r", encoding="utf-8") as sonar_readings:

        increasing_value_counter = 0
        previous_value = float("inf")

        for value in sonar_readings:

            if int(value) > previous_value:
                increasing_value_counter += 1

            previous_value = int(value)

    return increasing_value_counter

if __name__ == "__main__":
    print(increasing_measurements('day1/sonarreadings.txt'))
