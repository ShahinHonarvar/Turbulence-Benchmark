def find_divisors_in_range(n):
    if n < 120 or n > 349:
        return []
    a = []
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            a.append(i)
            if n / i == i:
                break
    if n % 2 == 0 and n / 2 == 2:
        a.append(2)
    if n % 3 == 0 and n / 3 == 3:
        a.append(3)
    return a
