import re
def find_divisors_in_range(n):
    if n < 50 or n > 81:
        return []
    else:
        res = []
        for i in range(1, int(n ** .5) + 1):
            if n % i == 0:
                res += [[i, n // i]]
        return res
