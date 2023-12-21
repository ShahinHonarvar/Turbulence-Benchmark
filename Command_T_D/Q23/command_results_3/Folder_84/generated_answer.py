def find_divisors_in_range(n):
    if n <= 224 or n >= 584:
        return []
    l = [x for x in range(1, int(n ** .5) + 1)]
    l.extend([x * x for x in l])
    l.extend([x * (n - x) for x in l])
    return [i for i in range(1, int(n ** .5) + 1) if any(i % j == 0 for j in l)]
