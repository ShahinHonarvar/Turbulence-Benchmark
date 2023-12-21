import math
import heapq
import itertools
def all_right_truncatable_prime(n):
    # write your code here
    lst = []
    for i in range(2, int(n[0]) + 1):
        isPrime = True
        i += 1
        while i <= int(n[0]):
            if i**0.5 % 1 == 0:
                break
            if i**0.5 == int(i**0.5):
                i += 1
            else:
                isPrime = False
                break
        if isPrime:
            lst.append(i)
    return sorted(lst)
