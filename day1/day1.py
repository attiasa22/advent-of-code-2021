
def increasing_measurements(sonar_readings_file):
    sonar_readings = open(sonar_readings_file, "r")
    
    increasing_value_counter = 0
    previous_value = float("inf")
    
    for value in sonar_readings:
        
        if int(value) > previous_value: increasing_value_counter += 1
        previous_value = int(value)

    sonar_readings.close()
    
    return increasing_value_counter

if __name__ == "__main__":
    print(increasing_measurements('day1/sonarreadings.txt'))
    


