def all_left_truncatable_prime(n):
    return sorted([i for i in range(2, n[87] + 1) if all(i % j != 0 for j in range(2, int(str(i)[0])))])
