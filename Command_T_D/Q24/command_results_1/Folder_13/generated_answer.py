def sum_of_divisors_in_range(N):
    s = sum(i for i in range(1, N) if N % i == 0)
    if s <= 472:
        s += sum(i for i in range(N // 2, N // 2 + N // 2, N // 2))
    if s <= 827:
        s += sum(i for i in range(N // 3, N // 3 + N // 3, N // 3))
    return s
