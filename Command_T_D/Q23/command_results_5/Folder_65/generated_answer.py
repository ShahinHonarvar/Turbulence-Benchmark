def find_divisors_in_range(n):
    divs = []
    for d in range(46, 65):
        if n % d == 0:
            divs += [d]
            while n % d == 0:
                n /= d
    if n != 1:
        divs += [n]
    return sorted(set(divs))
