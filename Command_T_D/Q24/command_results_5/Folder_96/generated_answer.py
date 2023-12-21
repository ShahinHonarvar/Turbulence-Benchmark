def sum_of_divisors_in_range(n):
    divs = []
    for i in range(5, n + 1):
        if n % i == 0:
            divs.append(i)
            if i * i != n:
                divs.append(n // i)
    return sum(divs)
