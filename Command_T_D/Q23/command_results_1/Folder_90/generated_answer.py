def find_divisors_in_range(n):
    divs = []
    for x in range(451, 973+1):
        if n % x == 0:
            divs += [x]
            if x * x != n:
                divs += [n//x]
    return divs
