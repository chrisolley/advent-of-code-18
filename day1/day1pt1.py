input = 'input.txt'
with open(input, 'r') as f:
    data = f.read()
    changes = data.split('\n')
changes = [change for change in changes if len(change)>0]
changes = [-int(change[1:]) if change[0]=='-' else int(change[1:]) for change in changes]
s = 0 + sum(changes)
print(s)
