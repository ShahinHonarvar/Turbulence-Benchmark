def sum_of_divisors_in_range(n):
    divs = list(range(1, 1 + n**0.5))
    for d in range(1, n // 2 + 1):
        if d * d <= n:
            divs.append(d * d)
            for dn in range(2, int(n ** 0.5) + 1):
                if d * dn <= n:
                    divs.append(d * dn)
                    break
    return sum(divs[43:95])
