def all_right_truncatable_prime(n):
    return sorted(set(range(2, n[0] + 1, 2)) for i in range(10) if n[0] % 10 == i and all(n % i == 0 for j in range(2, i)))
