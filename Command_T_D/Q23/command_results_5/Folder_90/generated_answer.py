import sys
def find_divisors_in_range(n):
    if n < 451:
        return []
    elif n > 973:
        return []
    else:
        return [x for x in range(1, int(n ** .5) + 1) if n % x == 0]
