with open('input.txt') as f:
    lines = f.read().split('\n')[:-1]
done = False 
for i, line1 in enumerate(lines):
    for j, line2 in enumerate(lines):
        s = 0
        for char1, char2 in zip(line1, line2):
            if char1 != char2:
                s+=1
        if s==1:
            done = True
            break
    if done:
        break
print(''.join([char for char, _ in zip(lines[i], lines[j]) if char==_]))
