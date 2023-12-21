
def all_left_right_truncatable_prime(x):
    # Find all prime numbers less than or equal to x
    primes = [p for p in range(2, x + 1) if all(p % i != 0 for i in range(2, int(p ** 0.5) + 1))]
    # Filter the list of prime numbers to include only those that are left-and-right-truncatable prime numbers
    return [p for p in primes if len(str(p)) > 1 and p % int(str(p)[1:]) == 0 and p % int(str(p)[:-1]))]
