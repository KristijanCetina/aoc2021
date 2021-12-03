with open("input.txt", "r") as inputfile:
    commands = [d for d in inputfile.read().strip().split("\n")]
commandSize = len(commands[0])
digit_list = []
for command in commands:
    digit_list.append(list(map(int, str(command))))

zeros, ones = [], []
for i in range(commandSize):
    zeros.append(0)
    ones.append(0)
    for bit in digit_list:
        if bit[i] == 0:
            zeros[i] += 1
        elif bit[i] == 1:
            ones[i] += 1
# print(ones, zeros)

gamma = [0]*commandSize
for i in range(commandSize):
    if zeros[i] > ones[i]:
        gamma[i] = 0
    else:
        gamma[i] = 1
e = [e ^ 0b1 for e in gamma]
print(gamma)
print(e)

string_ints = [str(int) for int in gamma]
str_of_ints = ",".join(string_ints)
g = int(str_of_ints.replace(",", ""), 2)

string_ints = [str(int) for int in e]
str_of_ints = ",".join(string_ints)
ee = int(str_of_ints.replace(",", ""), 2)

print(g*ee)
