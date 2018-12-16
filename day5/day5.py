with open('input.txt', 'r') as f:
    polymer = f.read()[:-1]

def reduceString(string):
    '''Reacts a polymer string by iteratively eliminating adjacent 
    identical letters of opposite cases'''

    n = len(string)
    n_new = 0
    while n-n_new != 0:
        n = len(string)
        i = 0
        del_chars = []
        while i < n-1:
            if string[i].swapcase() == string[i+1]:
                del_chars.append(i)
                del_chars.append(i+1)
                if i == n-2:
                    break
                else:
                    i += 2
            else:
                i += 1

        string = ''.join([c for i, c in enumerate(string) if i not in del_chars])
        n_new = len(string)
    return string

assert(reduceString('DdabAcCaCBAcCcaDAaA') == 'abCBAcaDA')

def eliminateLetter(string):
    letters = set(string.lower())
    return [len(reduceString(string.replace(c, '').replace(c.upper(), ''))) for
            c in letters]

print(len(reduceString(polymer)))
print(min(eliminateLetter(polymer)))
