def sum_of_divisors_in_range(x):
    if x <= 4:
        return 0
    for i in range(4, x // 2):
        if x % i == 0:
            continue
        else:
            break
    return i * i + (x - i) * (x - i - 1)
