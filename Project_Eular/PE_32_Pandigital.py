def is_pandigital(n, s=9):
    st = ""
    for i in range(1,s+1):
        st = st + str(i)
    return len(n)==s and ''.join(sorted(list(n))) == st

p = set()
n = int(raw_input())
for i in range(1, 999):
    for j in range(2, 999):
        if is_pandigital(str(i) + str(j) + str(i*j),n):
            p.add(i*j)

print sum(p)
