def all_right_truncatable_prime(n):
    return sorted([i for i in range(2, n[0] // 2) if all(i % j == 0 or i % j == 1 for j in range(2, int(str(i)[-1])))])
