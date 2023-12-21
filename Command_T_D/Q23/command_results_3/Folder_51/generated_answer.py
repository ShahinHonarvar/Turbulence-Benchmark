def find_divisors_in_range(n):
    divs = []
    for d in range(2, n // 2 + 1):
        if n % d == 0:
            divs.append(d)
            if d * d != n:
                divs.append(n // d)
    return sorted(set(divs))
