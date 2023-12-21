def find_divisors_in_range(n):
    divs = []
    for i in range(20, 51):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
    return divs
