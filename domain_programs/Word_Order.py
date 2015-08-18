from collections import Counter
n = int(raw_input())
words = []
for i in range(n):
    words.append(raw_input())
d = Counter(words)
word_set = set(words)
print len(word_set)
for i in words:
    if i in word_set:
        word_set.remove(i)
        print d[i],
