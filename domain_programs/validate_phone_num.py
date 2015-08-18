def validate(x):
    if len(x) != 10:
        return False
    if x[0] != "7" and x[0] !="8" and x[0] != "9":
        return False
    for i in x:
        if (not i.isdigit()):
            return False
    return True
n = int(raw_input())
l = []
for i in range(n):
    if validate(raw_input()):
        print "YES"
    else:
        print "NO"
