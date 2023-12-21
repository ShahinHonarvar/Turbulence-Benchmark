def all_right_truncatable_prime(n):
    return sorted(list(filter(str_is_right_truncatable_prime, str(n).split()))))
