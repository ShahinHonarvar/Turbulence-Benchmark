import itertools
import heapq
def all_right_truncatable_prime(tup):
    return sorted(list(filter(right_truncatable_prime, (x for x in range(tup[0], tup[1])))), key=lambda x: x)
def right_truncatable_prime(x):
    x += 1
    while True:
        if x % 2 == 0 or x % 5 == 0 or x % 10 == 0:
            return False
        x //= 5
        x //= 10
        x //= 5
