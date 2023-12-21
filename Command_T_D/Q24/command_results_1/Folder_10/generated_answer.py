import math
def sum_of_divisors_in_range(n):
    for i in range(1, n+1):
        if n%i == 0:
            a = 1
            j = i
            while j <= n:
                a += j
                j += i
            if 60 <= a <= 86:
                return a
    return 0
