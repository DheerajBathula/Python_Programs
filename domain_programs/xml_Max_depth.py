import xml.etree.ElementTree as etree
def deapth(x,sum):
    sum_l = []
    if len(x) == 0:
        return sum
    else:
        sum = sum + 1
    for i in x:
        sum_l.append(deapth(i,sum))
    return max(sum_l)
n = int(raw_input())
s = ""
l = []
for i in range(n):
    s = s + raw_input()
tree = etree.ElementTree(etree.fromstring(s))
root = tree.getroot()
if len(root) == 0:
    print int("0")
    quit()
for child in root:
    l.append(deapth(child,0))
print int(max(l)) + 1
