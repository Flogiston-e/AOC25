input = open("06.txt").read().split("\n")
input.pop(-1)
rows = [row.split(" ") for row in input]

problem = []
for row in rows:
    nrow = []
    for c in row:
        if c != "":
            if c in ["+", "*"]:
                nrow.append(c)
            else:
                nrow.append(int(c))
    problem.append(nrow)

ans = 0
for calci in range(len(problem[0])):
    if problem[-1][calci] == "*":
        p = 1
        for n in range(len(problem)-1):
            p = p*problem[n][calci]
    if problem[-1][calci] == "+":
        p = 0
        for n in range(len(problem)-1):
            p += problem[n][calci]
    ans += p
print(ans)


ops = []
for i, op in enumerate(input[-1]):
    if op != " ":
        ops.append((i,op))

end = len(input[-1])
ans = 0
for op in ops[::-1]:
    problem = []
    for i in range(op[0],end):
        num = ""
        for row in input[:-1]:
            num += row[i]
        problem.append(int(num))

    if op[1] == "*":
        p = 1
        for n in problem:
            p = p*n
    else:
        p = 0
        for n in problem:
            p += n
    ans += p
    #print(problem)
    end = op[0]-1
print(ans)