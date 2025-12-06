input = open("02.txt").read().split(",")

ans1, ans2 = 0, 0
for codes in input:
    codes = codes.split("-")
    for x in range(int(codes[0]), int(codes[1])+1):
        mid = len(str(x))//2
        for y in range(1, mid+1):
            if len(str(x))/y == len(str(x))//y:
                yes = True
                s = str(x)[0:y]
                for z in range(2, len(str(x))//y + 1):
                    if str(x)[z*y-y:z*y] != s:
                        yes = False
                        break

                if yes:
                    ans2 += x
                    break

        if str(x)[:mid] == str(x)[mid:]:
            ans1 += x

print(ans1)
print(ans2)