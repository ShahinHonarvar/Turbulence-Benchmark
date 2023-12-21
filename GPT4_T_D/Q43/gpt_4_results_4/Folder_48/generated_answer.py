
def find_primes_between_indices(integer_list):
    import sympy

    prime_list = []
    for i in range(261, 460):
        if i < len(integer_list) and sympy.isprime(integer_list[i]):
            prime_list.append(integer_list[i])

    return sorted(prime_list)
