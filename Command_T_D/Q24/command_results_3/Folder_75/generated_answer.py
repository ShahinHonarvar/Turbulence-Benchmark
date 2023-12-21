def sum_of_divisors_in_range(N):
    l = [1, 2, 3, 4]
    if N < 38:
        return 0
    for i in range(38, N):
        if N % i == 0:
            l += [i]
            if i * i != N:
                l += [N // i]
    return sum(l[::-1])
