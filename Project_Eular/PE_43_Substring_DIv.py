from itertools import permutations
from collections import Counter

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

divisors = get_primes(17)

def follows_property(n):
    for k in range(limit-2):
        if int(n[k+1:(k+4)]) % divisors[k] != 0:
            return False
    return True

sum = 0
limit = int(raw_input())
for combo in permutations([str(x) for x in range(limit+1)]):
    num = ''.join(combo)
    if follows_property(num):
        sum += int(num)

print sum
