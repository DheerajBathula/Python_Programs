f = raw_input()
spl = f.split()
list1 = []
list2 = []
k = 0
s = []
for i in range(int(spl[0])):
    list1.append(raw_input())
for i in range(int(spl[1])):
    list2.append(raw_input())
for i in range(0,len(list2)):
    s.append("")
    for j in range(0,len(list1)):
        if list1[j] == list2[i]:
            s[i] = s[i] + str(j+1) + " "
for i in s:
    if i:
        print i
    else:
        print "-1"
