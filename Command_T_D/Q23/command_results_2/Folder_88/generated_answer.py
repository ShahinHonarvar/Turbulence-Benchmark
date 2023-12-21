def find_divisors_in_range(n):
    divs = []
    for i in range(6, n // 2 + 1):
        if n % i == 0:
            divs.append(i)
            if n / i != i:
                divs.append(n // i)
    return sorted(set(divs))
