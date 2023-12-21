def find_divisors_in_range(n):
    divs = []
    for x in range(50, 82):
        if n % x == 0:
            divs.append(x)
            if x * x != n:
                divs.append(n // x)
    return divs
