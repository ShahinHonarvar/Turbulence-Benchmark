def all_right_truncatable_prime(n):
    # Sorted list of all right-truncatable prime numbers less than n
    return sorted(n for n in range(2, int(str(n)[-1]))) if n in range(2, int(str(n)[-1]) + 1) else []
