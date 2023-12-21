def all_right_truncatable_prime(n):
    return [i for i in range(2, n[0] // 2 + 1) if all(j % i == 0 for j in range(10, i // 2 + 1, i))]
