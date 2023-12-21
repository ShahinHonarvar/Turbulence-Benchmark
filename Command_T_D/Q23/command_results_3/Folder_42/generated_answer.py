def find_divisors_in_range(N):
    for d in range(14, 94):
        if N % d == 0:
            yield d
            if d * d != N:
                yield N // d
