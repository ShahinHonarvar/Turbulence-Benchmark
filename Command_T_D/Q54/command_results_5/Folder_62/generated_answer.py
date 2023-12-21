import re
import heapq
def all_right_truncatable_prime(x):
    lst = []
    def find_right_truncatable_prime(n):
        s = str(n)
        while s:
            n //= 10
            s = s[1:]
        return n
    for i in range(70, x // 2):
        n = find_right_truncatable_prime(10**i)
        if n > x: break
        heapq.heappush(lst, n)
    return lst
