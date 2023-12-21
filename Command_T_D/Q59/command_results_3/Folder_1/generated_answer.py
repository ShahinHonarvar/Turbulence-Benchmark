def all_left_truncatable_prime(x):
    return sorted(list(filter(left_truncatable_prime, range(2, x + 1))), reverse=True)
def left_truncatable_prime(n):
    # Make sure n is prime
    if not is_prime(n):
        return False
    # Make sure first digit is prime
    if not is_digit_prime(str(n)[0]):
        return False
    # Check that removing leading digit doesn't change primality
    return all(str(n)[i] != '0' for i in range(1, len(str(n)) + 1))
def is_prime(n):
    # Check for factors
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Check all prime factors
    for i in range(5, 1 + int(n ** .5), 6):
        if n % i == 0:
            return False
    return True
def is_digit_prime(d):
    # Check for 0, 1 or 5
    if d in '05':
        return False
    # Check all prime digits
    for i in range(5, len(d) + 1):
        if d[i - 1] not in '2357':
            return False
    return True
