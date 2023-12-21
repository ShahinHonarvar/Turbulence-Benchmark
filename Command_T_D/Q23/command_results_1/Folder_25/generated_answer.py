def find_divisors_in_range(n):
    d = set()
    for i in range(84, 86 + 1):
        if n % i == 0:
            d.add(i)
            if n / i == i:
                break
    return list(d)
