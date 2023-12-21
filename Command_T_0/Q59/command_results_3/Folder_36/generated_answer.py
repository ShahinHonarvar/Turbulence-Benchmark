def all_left_truncatable_prime(n):
    return sorted(set(str(n)[0] for n in range(2, int(str(n)[0]) + 1) if all(str(n)[i] for i in range(1, len(str(n)) + 1) if str(n)[i] not in '0')))
