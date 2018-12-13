
def findCoords(claim):
    '''Claim of form: #123 @ 3,2: 5x4 '''
    xl = int(claim.split(' ')[2].split(',')[0])
    yt = int(claim.split(' ')[2].split(',')[1][:-1])
    xr = int(claim.split(' ')[3].split('x')[0]) + xl
    yb = int(claim.split(' ')[3].split('x')[1]) + yt
    return xl, xr, yb, yt

assert(findCoords('#123 @ 3,2: 5x4') == (3,8,6,2))

def findSquares(claim):
    '''Returns set of coords in a claim'''
    squares = set()
    xl, xr, yb, yt = findCoords(claim)
    for x in range(xl+1, xr+1):
        for y in range(yt+1, yb+1):
            squares.add((x,y))
    return squares

assert(findSquares('#666 @ 1,2: 2x2') == {(2,3), (3,3), (2,4), (3,4)})

def main():
    with open('input.txt', 'r') as f:
        lines = f.read().split('\n')[:-1]
    overlap = set()
    overlaps = set()
    for i, line1 in enumerate(lines):
        for j, line2 in enumerate(lines[i+1:]):
            o = findSquares(line1).intersection(findSquares(line2))
            if len(o) != 0:
                overlap.update(o)
                overlaps.add(line1.split(' ')[0])
                overlaps.add(line2.split(' ')[0])

    intact = set([line.split(' ')[0] for line in lines]).difference(overlaps)
             
    return overlap, intact

if __name__ == '__main__':
    overlap, intact = main()
    print(len(overlap))
    print(intact)
