def find_divisors_in_range(n):
    divs = []
    for i in range(35, 55):
        if n % i == 0:
            divs.append(i)
            if n / i != i:
                divs.append(n // i)
    return divs
