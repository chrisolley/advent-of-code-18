with open('input.txt') as f:
    lines = f.read().split('\n')
twos = 0
threes = 0
for line in lines:
    repeats = {}
    for i, char in enumerate(line[:-1]):
        if char in line[i+1:]:
            if char in repeats:
                repeats[char] += 1
            else:
                repeats[char] = 2
    if 2 in repeats.values():
        twos+=1
    if 3 in repeats.values():
        threes+=1

print(twos*threes)
