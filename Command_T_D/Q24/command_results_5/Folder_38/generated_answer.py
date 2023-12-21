def sum_of_divisors_in_range(n):
    if n < 16 or n > 68:
        return 0
    a = [1, 2, 3, 4, 6, 8, 9, 10, 12, 16, 18, 20, 24, 28, 30, 32, 36, 40, 44, 48, 54, 56, 60, 64, 66]
    s = 0
    for i in range(1, len(a)):
        for j in range(i + 1, len(a)):
            if a[i] * a[j] <= n:
                s += a[i] * a[j]
    return s
