def all_left_truncatable_prime(n):
    return sorted((n[i] for i in range(len(n)) if n[i] % 2 == 1 and n[i] * 10**(i + 1) % 9 != 0), reverse=True)
