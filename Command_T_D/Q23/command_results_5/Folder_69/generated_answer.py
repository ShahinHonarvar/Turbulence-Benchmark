def find_divisors_in_range(N):
    l = [x for x in range(658, 868) if N % x == 0]
    if not l:
        return []
    l.sort()
    l.extend([N])
    return l
