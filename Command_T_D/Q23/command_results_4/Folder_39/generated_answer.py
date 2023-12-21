def find_divisors_in_range(n):
    # your code here
    if n < 11 or n > 56:
        return []
    divs = []
    for d in range(1, int(n ** .5) + 1):
        if n % d == 0:
            divs += [d]
            if d * d != n:
                divs += [n // d]
    return sorted(set(divs))
