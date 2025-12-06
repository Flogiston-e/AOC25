banks = open("03.txt").read().strip().split()

def maxfinder(start: int, end: int, bank: str):
    max, mi = "0", 0
    for i, battery in enumerate(bank[start:end]):
        if battery > max:
            max, mi = battery, i
    return max, mi+start+1

def maxjolts(turnons: int, ans: int = 0):
    for bank in banks:
        start, jolts = 0, ""
        for b in range(turnons-1, -1, -1):
            max, start = maxfinder(start, len(bank)-b, bank)
            jolts += max
        ans += int(jolts)
    print(ans)

maxjolts(2), maxjolts(12)