def find_divisors_in_range(n):
    divs = []
    for i in range(4, 8):
        if n % i == 0:
            divs.append(i)
            if i * i != n:
                divs.append(n // i)
    return divs
