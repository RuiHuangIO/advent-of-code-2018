from collections import Counter
f = open('inputs.txt', 'r')
r = f.readlines()

# part 1

# twoletters = 0
# threeletters = 0

# for line in r:
#     counter = Counter(line)
#     if 2 in counter.values():
#         twoletters += 1
#     if 3 in counter.values():
#         threeletters += 1
# print(twoletters * threeletters)

# part 2
list = []
for line in r:
    list.append(line.strip())

d = set()
for i in list:
    for j in range(len(i)):
        new_str = ''.join(i[:j] + '_' + i[j+1:])
        if new_str in d:
            print(''.join(n for n in new_str if n != '_'))
        d.add(new_str)
print(d)
