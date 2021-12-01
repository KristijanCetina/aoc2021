# samo za debug :-)
# from os import write

with open("depth.txt","r") as inputfile:
    depth = inputfile.read().strip().split("\n")
    steps = 0

    for count, d in enumerate(depth):
        if int(depth[count]) > int(depth[count-1]):
            steps += 1
        # ovo mi je trebalo jer nisam odmah skužio da su u listi stringovi, a ne int
        # with open("log.txt", "a") as logfile:
        #     logfile.writelines(f"dubina je {d}, a promjena {steps}\n")
    print (steps)
