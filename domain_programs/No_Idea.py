from collections import Counter
a1 = raw_input()
a2 = raw_input()
list2 = a2.split()
a3 = raw_input()
list3 = a3.split()
a4 = raw_input()
list4 = a4.split()
score = 0
b = Counter(list2)
inter_a = list(set(b.keys()).intersection(set(list3)))
inter_b = list(set(b.keys()).intersection(set(list4)))
count_plus = 0
count_minus = 0
for i in inter_a:
    count_plus = count_plus + b[i]
for i in inter_b:
    count_minus = count_minus + b[i]
print count_plus-count_minus
