
def increasing_measurements(sonar_readings_file):
    sonar_readings = open(sonar_readings_file, "r")
    
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

    sonar_readings.close()
    
    return increasing_value_counter

if __name__ == "__main__":
    print(increasing_measurements('./day1/sonarreadings.txt'))
    
