with open("course.txt", "r") as inputfile:
    commands = [d for d in inputfile.read().strip().split("\n")]
fwd, depth = 0, 0
for command in commands:
    command = command.split(" ")
    direction = command[0]
    value = command[1]
    if direction == "forward":
        fwd += int(value)
    elif direction == "down":
        depth += int(value)
    elif direction == "up":
        depth -= int(value)
print(f"Part 1: forward: {fwd}, down: {depth}, product: {fwd*depth}")


fwd, depth, aim = 0, 0, 0
for command in commands:
    command = command.split(" ")
    direction = command[0]
    value = command[1]
    if direction == "down":
        aim += int(value)
    elif direction == "up":
        aim -= int(value)
    elif direction == "forward":
        fwd += int(value)
        depth += int(value)*aim

print(f"Part 2: forward: {fwd}, down: {depth}, product: {fwd*depth}")
