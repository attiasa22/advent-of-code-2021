"""Day 2 of https://adventofcode.com 2021 challenge"""
def increasing_measurements(sonar_readings_file):
    '''Determine if a rolling window of 3 sonar readings is increasing'''
    with open(sonar_readings_file, "r", encoding="utf-8") as sonar_readings:

        increasing_value_counter = 0

        triplet_counter=0

        value_tracker = []

        current_value = 0

        for value in sonar_readings:
            value_tracker.append(int(value))
            print(value_tracker)
            if triplet_counter<3:
                current_value += int(value)
                triplet_counter += 1
            else:
                previous_value = current_value
                current_value = current_value - value_tracker.pop(0) + int(value)

                if current_value > previous_value:
                    increasing_value_counter += 1

    return increasing_value_counter

if __name__ == "__main__":
    print(increasing_measurements('./day1/sonarreadings.txt'))
    