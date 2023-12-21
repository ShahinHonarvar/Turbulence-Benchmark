def sum_of_divisors_in_range(n):
    divs = []
    for i in range(32, 90 + 1):
        if n % i == 0:
            divs += [i]
            if i * i != n:
                divs += [n // i]
    return sum(divs) if len(divs) > 0 else 0
