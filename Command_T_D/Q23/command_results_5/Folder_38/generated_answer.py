import sys
def find_divisors_in_range(n):
    if n < 16 or n > 68:
        return []
    d = [(x, n // x) for x in range(1, int(n ** .5) + 1) if n % x == 0]
    d = sorted(set(d))
    divs = []
    for x, y in d:
        for i in range(x, y + 1):
            if i not in divs:
                divs.append(i)
    return divs
