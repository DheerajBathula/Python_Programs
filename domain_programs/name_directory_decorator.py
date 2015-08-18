n = int(raw_input())
l = []
l2 = []
ages = []
for i in range(n):
    l.append(raw_input().split())
for i in l:
    if i.pop() == "M":
        l2.append("Mr. "+i[0]+" "+i[1])
    else:
        l2.append("Ms. "+i[0]+" "+i[1])
for i in l:
    ages.append(i[2])
for i in sorted(ages):
    for j in l:
        if i in j:
            print l2[l.index(j)]
            l[l.index(j)] = []
