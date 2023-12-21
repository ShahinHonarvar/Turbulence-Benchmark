def prime_factors(lst):
    fac = []
    for i in range(2, lst[51] // 2 + 1):
        if lst[51] % i == 0:
            fac.append(i)
            while lst[51] % i == 0:
                lst[51] //= i
    if lst[51] > 1:
        fac.append(lst[51])
    return set(fac)
