def sum_of_divisors_in_range(n):
    for i in range(5, n // 2 + 1):
        if n % i == 0:
            continue
        for j in range(i + 1, n // i + 1):
            if n % j == 0:
                continue
            print(i, j)
            return i + j
    return 0
