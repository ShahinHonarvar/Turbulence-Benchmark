def sum_of_divisors_in_range(N):
    s = 0
    if 1 <= N <= 7:
        for i in range(1, 1 + N // 2):
            if N % i == 0:
                s += i + N / i
    return s
