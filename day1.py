import itertools

f = open('inputs.txt', 'r')
r = f.readlines()
sum = 0

# part 1
# for line in r:
#   frequency = int(line.replace("\n", ""))
#   sum += frequency
# print(sum)

# part 2
seen = set()
for line in itertools.cycle(r):
    frequency = int(line.replace("\n", ""))
    sum += frequency
    if sum in seen:
        print(sum)
        break
    seen.add(sum)
f.close()
