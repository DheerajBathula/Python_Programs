import math
def differ(x,y):
    result = []
    result.append(float(y[0]) - float(x[0]))
    result.append(float(y[1]) - float(x[1]))
    result.append(float(y[2]) - float(x[2]))
    return result
def cross(a,b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return c

a = raw_input()
b = raw_input()
c = raw_input()
d = raw_input()
ac = a.split()
bc = b.split()
cc = c.split()
dc = d.split()
ab = differ(ac,bc)
bc = differ(bc,cc)
cd = differ(cc,dc)
ab_bc = cross(ab,bc)
bc_cd = cross(bc,cd)
dot = (ab_bc[0]*bc_cd[0]) + (ab_bc[1]*bc_cd[1]) + (ab_bc[2]*bc_cd[2])
modx = math.sqrt((ab_bc[0]*ab_bc[0]) + (ab_bc[1]*ab_bc[1]) + (ab_bc[2]*ab_bc[2]))
mody = math.sqrt((bc_cd[0]*bc_cd[0]) + (bc_cd[1]*bc_cd[1]) + (bc_cd[2]*bc_cd[2]))
result = dot/(modx*mody)
x = math.acos(result)
y = x * 180 / math.pi
print("%.2f" % y)
