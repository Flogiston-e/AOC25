input = open("08.txt").read().strip().split()

boxes = []
for row in input:
    box = []
    for c in row.split(","):
        box.append(int(c))
    boxes.append(box)

clusters = []
connections = set()
done = len(boxes)

for iteration in range(1000000):

    if iteration == 1001:
        largests = [0,0,0]
        for cluster in clusters:
            if len(cluster) > min(largests):
                largests[largests.index(min(largests))] = len(cluster)

        print(largests[0]*largests[1]*largests[2])

    shortest = 10**15
    cluster = 0
    closeboxes = ()

    for i, b in enumerate(boxes):
        for j, c in enumerate(boxes):
            if j > i:
                if (i,j) not in connections:
                    distance = (b[0]-c[0])**2 + (b[1]-c[1])**2 + (b[2]-c[2])**2
                    if distance < shortest:
                        closeboxes = (i,j)
                        shortest = distance
    connections.add(closeboxes)

    c0 = None
    c1 = None
    for ci, cluster in enumerate(clusters):
        if closeboxes[0] in cluster:
            c0 = ci
        if closeboxes[1] in cluster:
            c1 = ci

    if c0 == None and c1 == None:
        clusters.append(set(closeboxes))
    elif c0 == c1:
        continue
    elif c0 != None and c1 != None:
        clusters[min(c0,c1)].update(clusters.pop(max(c0,c1)))
    elif c0 == None:
        clusters[c1].add(closeboxes[0])
    elif c1 == None:
        clusters[c0].add(closeboxes[1])        
    
    if len(clusters[0]) == done:
        print(boxes[closeboxes[0]][0]*boxes[closeboxes[1]][0])
        break