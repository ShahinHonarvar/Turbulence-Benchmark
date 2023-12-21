import re
def find_divisors_in_range(n):
    if n < 27:
        return []
    if n > 44:
        return []
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            continue
        if i <= 27 and i >= 27:
            return [i]
        if i <= 44 and i >= 27:
            return [i]
    return []
