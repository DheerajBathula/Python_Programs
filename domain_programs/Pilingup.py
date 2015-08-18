for i in range(0, int(raw_input())):
    n = int(raw_input())
    s = raw_input()
    a = map(int,s.split())
    min_a = min(a)
    indx = a.index(min_a)

    while min_a in a:
        if indx != a.index(min_a):
            print 'No'
            quit()
        a.remove(min_a)

    s1 = a[:indx]
    s2 = a[indx:]

    if s1 == sorted(s1, reverse = True) and s2 == sorted(s2):
        print 'Yes'
    else:
        print 'No'
