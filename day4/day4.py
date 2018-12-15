from collections import Counter

def getMinutes(array):
    '''Returns an array of minutes slept for a list of start and end times'''
    minutes = []
    for i in range(int(len(array)/2)):
        minutes += range(int(array[2*i]), int(array[2*i+1]))
    return minutes

assert(getMinutes(['01', '04', '23', '31']) == [1, 2, 3, 23, 24, 25, 26, 27,
                                                28, 29, 30])

def pt1(guards):
    guardTimes = [(guard, len(guards[guard])) for guard in guards]
    guardTimes.sort(key=lambda x: x[1], reverse=True)
    sleepyGuard = guardTimes[0][0]
    mostCommonTime = Counter(guards[sleepyGuard]).most_common(1)[0][0]
    return sleepyGuard, mostCommonTime

def pt2(guards):
    mostCommonTimes = []
    for iD, times in guards.items():
        mostCommon = Counter(guards[iD]).most_common(1)[0]
        mostCommonTimes.append((iD, mostCommon[0], mostCommon[1]))
    mostCommonTimes.sort(key=lambda x: x[2], reverse=True)
    sleepyGuard = mostCommonTimes[0][0]
    mostCommonTime = mostCommonTimes[0][1]
    return sleepyGuard, mostCommonTime

def main():
    '''Generates dictionary of minutes asleep for each guard, over all dates'''
    with open('input.txt', 'r') as f:
        lines = f.read().split('\n')[:-1]
    # generate tuple pairs of (date, event)
    events = [(' '.join(line.split(' ')[0:2])[1:-1], ' '.join(line.split(' ')[3:])) for
              line in lines]
    events.sort(key=lambda x: x[0]) # sort by date

    guards = {}
    for date, event in events: # create {guard:array of sleeping/waking times} dictionary
        if event[0] == '#':
            iD = event.split(' ')[0]
        else:
            if iD in guards:
                guards[iD].append(date.split(':')[1])
            else:
                guards[iD] = [date.split(':')[1]]

    for iD, times in guards.items():
        guards[iD] = getMinutes(times)
    return guards

if __name__ == '__main__':
    guards = main()
    sleepyGuard, mostCommonTime = pt1(guards)
    print(f'Most sleepy guard: {sleepyGuard}')
    print(f'Most common time: {mostCommonTime}')
    print(f'{int(sleepyGuard[1:])*int(mostCommonTime)}')
    sleepyGuard, mostCommonTime = pt2(guards)
    print(f'Most sleepy guard: {sleepyGuard}')
    print(f'Most common time: {mostCommonTime}')
    print(f'{int(sleepyGuard[1:])*int(mostCommonTime)}')
