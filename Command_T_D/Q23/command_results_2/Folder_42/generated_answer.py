import math
def find_divisors_in_range(n):
    divs = []
    for i in range(14, 93):
        if n % i == 0:
            divs += [i]
            if i * i != n:
                divs += [n // i]
    return divs
