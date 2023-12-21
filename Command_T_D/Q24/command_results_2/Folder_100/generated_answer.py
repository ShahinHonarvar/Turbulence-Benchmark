def sum_of_divisors_in_range(n):
    divs = []
    for x in range(11, n // 2):
        if n % x == 0:
            divs.append(x)
            if x * x != n:
                divs.append(n // x)
    if n % 2 == 0:
        divs.append(n // 2)
    return sum(divs)
