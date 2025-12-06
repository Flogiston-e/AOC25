input = open("01.txt").read().replace("R","+").replace("L","-").split()
dial, p1, passes = 50, 0, 0
for turn in input:
    dial += int(turn)
    passes += abs(dial//100) - ((dial > 0 and dial%100 == 0) or (dial < 0 and dial-int(turn) == 0))
    dial = dial%100
    if dial == 0: p1 += 1
print(p1)
print(p1+passes)