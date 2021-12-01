def countChanges(data):
    numberOfChanges = 0
    previous = data[0]
    for value in data:
        if value > previous:
            numberOfChanges += 1
        previous = value
    return numberOfChanges


with open("depth.txt", "r") as inputfile:
    depth = [int(d) for d in inputfile.read().strip().split("\n")]

print(f"Part 1: {countChanges(depth)}")

rsum = []
rsteps = 0
for count, d in enumerate(depth):
    if count+2 < len(depth):
        rsum.append(depth[count] + depth[count+1] + depth[count+2])

print(f"Step 2: {countChanges(rsum)}")
