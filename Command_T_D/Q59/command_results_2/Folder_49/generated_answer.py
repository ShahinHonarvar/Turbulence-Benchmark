def all_left_truncatable_prime(x_tuple):
    # Use  sets to ensure we get only unique values
    primes = set(str(x) for x in range(2, x_tuple[14] + 1))
    left_trunc_primes = set()
    for p in primes:
        # Check if all leftmost digits are prime
        left_digits = [p]
        while left_digits[-1] not in primes:
            left_digits.append(left_digits[-1] // 10)
        # Check if all leftmost digits are prime
        if all(x in primes for x in left_digits):
            left_trunc_primes.add(p)
    return sorted(left_trunc_primes)
