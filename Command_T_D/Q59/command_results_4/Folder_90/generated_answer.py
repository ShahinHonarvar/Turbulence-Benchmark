def all_left_truncatable_prime(n):
    x = n[466]
    return sorted(set(str(y) for y in range(2, x // 2) if all(int(z) == z for z in str(y)) and all(z not in str(y) for z in str(y - 1))), reverse=True)
