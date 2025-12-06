input = open("04.txt").read().strip().split()

pmap = [list(row) for row in input]
width, height = len(pmap[0]), len(pmap)
adjecents = [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]

def counter(p1):
    ans = 0
    removing = True
    while removing:
        removing = False
        for x in range(width):
            for y in range(height):
                if pmap[y][x] == "@":
                    rolls = 0
                    for a in adjecents:
                        if 0 <= x+a[0] < width and 0 <= y+a[1] < height:
                            if pmap[y+a[1]][x+a[0]] == "@":
                                rolls += 1
                    if rolls < 4:
                        ans += 1
                        if p1:
                            continue
                        pmap[y][x] = "."
                        removing = True
    print(ans)

counter(True), counter(False)

