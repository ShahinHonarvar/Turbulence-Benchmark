def find_divisors_in_range(n):
    d = []
    for i in range(46,89+1):
        if n % i == 0:
            d += [i]
            if i*i != n:
                d += [n//i]
    return d
