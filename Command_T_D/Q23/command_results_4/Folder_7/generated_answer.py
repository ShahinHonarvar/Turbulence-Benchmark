def find_divisors_in_range(n):
    divs = []
    for i in range(469, 682):
        if n % i == 0:
            divs.append(i)
            if n / i == i:
                break
    return divs
