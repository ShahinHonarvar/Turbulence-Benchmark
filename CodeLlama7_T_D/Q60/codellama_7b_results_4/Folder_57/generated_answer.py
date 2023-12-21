
def all_left_right_truncatable_prime(x):
    # List of all prime numbers less than or equal to x
    primes = []
    for i in range(2, x + 1):
        # Check if i is a prime number
        if i > 1:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                primes.append(i)
    # List of all left-and-right-truncatable prime numbers less than or equal to x
    lrtprimes = []
    for prime in primes:
        num_digits = len(str(prime))

        if num_digits == 1 or num_digits == 2:
            # Check if prime is left-and-right-truncatable
            left_truncated = prime
            right_truncated = prime

            for i in range(num_digits - 1):
                left_truncated = int(str(left_truncated)[:-1])

                if left_truncated < 2 or (left_truncated % 2 == 0 and left_truncated != 2)):
                    break
            else:
                for i in range(num_digits - 1):
                    right_truncated = int(str(right_truncated)[1:]))

                    if right_truncated < 2 or (right_truncated % 2 == 0 and right_truncated != 2)):
                        break
                else:
                    lrtprimes.append(prime)
    return sorted(lrtprimes, reverse=True)
