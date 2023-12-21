def all_right_truncatable_prime(n):
    return [n[i] for i in range(1, len(n)) if all(n[i] % d == 0 or n[i] == d for d in range(3, int(n[i]) + 1, 2)) and n[i] != '']
