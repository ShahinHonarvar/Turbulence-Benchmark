def sum_of_divisors_in_range(x):
    return sum(
        i * j
        for i in range(x, x // 2)
        for j in range(x // i + 1, min(x, 9), i)
    )
