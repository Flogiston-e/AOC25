input = open("07.txt").read().strip().split()
from collections import defaultdict

splits, weights = 0, defaultdict(lambda: 0, {(0, input[0].index("S")):1})

while True:
    (y,x) = min(weights.keys())
    if y >= len(input)-1:
        break

    if input[y+1][x] == ".":
        weights[(y+1,x)] += weights[(y,x)]
        
    elif input[y+1][x] == "^":
        weights[(y+1,x+1)] += weights[(y,x)]
        weights[(y+1,x-1)] += weights[(y,x)]
        splits += 1  
    weights.pop((y,x))

print(splits)
print(sum(weights.values()))