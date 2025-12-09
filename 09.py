input = open("test.txt").read().strip().split()

tiles = []
for tile in input:
    tile = tile.split(",")
    tiles.append((int(tile[0]),int(tile[1])))

turns = []
for i in range(-1, len(tiles)-1):
    x0 = tiles[i][0] - tiles[i-1][0]
    x1 = tiles[i+1][0] - tiles[i][0]
    y0 = tiles[i][1] - tiles[i-1][1]
    y1 = tiles[i+1][1] - tiles[i][1]
    if ((x0 < 0) and (y1 < 0)) or ((y0 < 0) and (x1 > 0)) or ((x0 > 0) and (y1 > 0)) or ((y0 > 0) and (x1 < 0)):
        turns.append(("r", (x0 > 0 or y0 > 0, x0 == 0))) # (True,True) == y0 > 0, (True, False) == x0 > 0, (False, True) == y0 < 0, (False,False) == x0 < 0
    else: 
        turns.append(("l", (x0 > 0 or y0 > 0, x0 == 0))) # (True,True) == y0 > 0, (True, False) == x0 > 0, (False, True) == y0 < 0, (False,False) == x0 < 0


turns.append(turns[0])
turns.pop(0)

print(turns)
    
maxarea = 0
for i,t1 in enumerate(tiles):
    for j,t2 in enumerate(tiles):
        if i > j:
            if turns[i] == "r" and t1[0]-t2[0]:
                1
            area = (abs(t1[0]-t2[0])+1)*(abs(t1[1]-t2[1])+1)
            if maxarea < area:
                maxarea = area
print(maxarea)

