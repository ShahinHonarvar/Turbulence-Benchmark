
def all_left_truncatable_prime(tuple_of_numbers):
    import sympy

    x = tuple_of_numbers[77]

    all_primes = list(sympy.primerange(10, x))
    left_truncatable_primes = []

    for prime_number in all_primes:
        prime_number_str = str(prime_number)
        if '0' in prime_number_str:
            continue
        else:
            left_truncated_primes = [int(prime_number_str[i:]) for i in range(len(prime_number_str))]
            if all(sympy.isprime(num) for num in left_truncated_primes):
                left_truncatable_primes.append(prime_number)

    return sorted(left_truncatable_primes)
