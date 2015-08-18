def check(i,n):
    s = 0
    for j in str(i):
        s = s + int(j)**n
    return s==i

n = int(raw_input())
s = 0
for i in range(2,1000000):
    if check(i,n):
        s = s + i
print s
