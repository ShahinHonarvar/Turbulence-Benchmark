
def all_left_right_truncatable_prime(x_range):
    # your code here
    left_right_truncatable_primes = []
    for prime in range(2, x_range[1] + 1):
        # Check if prime is even
        if prime % 2 == 0:
            continue
        # Check if prime is odd
        if prime % 2 == 1:
            # Check if prime is left-truncatable
            if prime % 10 == 1 or prime % 10 == 5 or prime % 10 == 3:
                # Check if prime is right-truncatable
                if prime % 100 == 1 or prime % 100 == 5 or prime % 100 == 3:
                    # Add prime to list
                    left_right_truncatable_primes.append(prime)
    return left_right_truncatable_primes
