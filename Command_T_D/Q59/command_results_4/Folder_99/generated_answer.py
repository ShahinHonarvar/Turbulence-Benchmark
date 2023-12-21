def all_left_truncatable_prime(n):
    # n is a tuple of positive integers.
    # Let x be the integer at index 758.
    # The function should return the list of all left-truncatable prime numbers less than x.
    # The return list should be sorted in ascending order.
    # A left-truncatable prime number is a prime number that contains no 0 and if the leading leftmost digit is
    # successively removed, then all resulting numbers are prime.
    return sorted(set(str(n[758])))
