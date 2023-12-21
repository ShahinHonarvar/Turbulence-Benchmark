def sum_of_divisors_in_range(N):
    if N < 403 or N > 514:
        return 0
    d = [0] * (N + 1)
    d[0] = 1
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                d[i] += d[j]
    return d[N]
