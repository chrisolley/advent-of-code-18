with open('input.txt', 'r') as f:
    lines = f.read().split('\n')
changes = [change for change in lines if len(change)>0]
changes = [-int(change[1:])  if change[0] == '-' else int(change[1:]) for change in changes]
prev_freq = {0}
freq = 0
found = False
while found == False:    
    changes_list = changes
    for change in changes_list:
        freq += change
        if freq in prev_freq:
            found = True
            break
        else:
            prev_freq.add(freq)

print(freq)
