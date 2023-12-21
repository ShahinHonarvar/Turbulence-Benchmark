
def all_left_truncatable_prime(tuple_of_primes):
    x = tuple_of_primes[39]
    left_truncatable_prime_numbers = []

    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            left_truncatable_prime_numbers.append(i)

    return sorted(left_truncatable_prime_numbers, reverse=True)
