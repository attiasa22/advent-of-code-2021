"""Day 2 of https://adventofcode.com 2021 challenge"""
def increasing_measurements(directions_file):
    horizontal = 0
    vertical = 0
    aim = 0
    with open(directions_file, "r", encoding="utf-8") as directions:
        for line in directions:
            direction = line.split()
            
            if direction[0] == "forward":
                horizontal += int(direction[1])
                vertical += aim * int(direction[1])
            elif direction[0] == "down":
                aim += int(direction[1])
            else: 
                aim -= int(direction[1])
        
    return vertical * horizontal

if __name__ == "__main__":
    print(increasing_measurements('day2/directions.txt'))
