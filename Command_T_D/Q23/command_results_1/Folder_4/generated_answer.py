def find_divisors_in_range(n):
    l = [a for a in range(48, 60) if n % a == 0]
    return [x for x in range(1, n // 48) if all(x % d == 0 for d in l)]
