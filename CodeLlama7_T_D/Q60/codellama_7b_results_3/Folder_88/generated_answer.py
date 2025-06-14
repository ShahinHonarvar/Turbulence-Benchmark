
def all_left_right_truncatable_prime(x):
    # Find all prime numbers less than or equal to x
    primes = [p for p in range(2, x + 1) if all(p % i != 0 for i in range(2, int(p ** 0.5) + 1))]
    # Filter out non-left-and-right-truncatable prime numbers
    result = []
    for p in primes:
        is_left_right_truncatable = True
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0 and (p - i * (p // i)) % i != 0:
                is_left_right_truncatable = False
                break

        if is_left_right_truncatable:
            result.append(p)

    return sorted(result)
