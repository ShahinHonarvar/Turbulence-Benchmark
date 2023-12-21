def find_divisors_in_range(n):
    if n < 10 or n > 55:
        return []
    divs = []
    for i in range(10, n // 2):
        if n % i == 0:
            divs.append(i)
    for i in range(1, n // 2):
        if n % i == 0:
            divs.append(i)
    return divs
