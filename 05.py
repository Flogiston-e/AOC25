ranges, ingredients = open("05.txt").read().strip().split("\n\n")

ranges= [[int(s) for s in r.split("-")] for r in ranges.split()]
ingredients = [int(v) for v in ingredients.splitlines()]

ans = 0
for ingredient in ingredients:
    for r in ranges:
        if r[0] <= ingredient <= r[1]:
            ans += 1
            break
print(ans)

change = True
while True:
    overlap = False
    for i, r1 in enumerate(ranges):
        for j, r2 in enumerate(ranges):
            if j == i:
                continue
            overlap = False
            if r2[0] <= r1[1]+1 and r2[1] >= r1[0]+1:
                ranges.append([min(r1[0], r2[0]), max(r1[1], r2[1])])
                ranges.pop(max(i,j))
                ranges.pop(min(i,j))
                overlap = True
                break
        if overlap:
            break
    if not overlap:
        break
    
print(sum([r[1]-r[0]+1 for r in ranges]))

