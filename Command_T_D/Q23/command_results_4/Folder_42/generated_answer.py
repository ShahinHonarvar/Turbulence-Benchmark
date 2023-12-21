def find_divisors_in_range(n):
    lst = []
    for i in range(1, n + 1):
        if i * i <= n:
            for j in range(i, int(n ** .5) + 1):
                if n % j == 0:
                    lst.append(i * j)
                    break
    if n % 2 == 0:
        lst.append(n // 2)
    if n % 3 == 0:
        lst.append(n // 3)
    return lst
