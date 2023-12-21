def find_divisors_in_range(n):
    divs = []
    for i in range(57, n // 2 + 1, 2):
        if n % i == 0:
            divs += [i]
    if n % 2 == 0:
        divs += [2]
    for i in range(n // 2, 86, 2):
        if n % i == 0:
            divs += [i]
    return sorted(set(divs))
