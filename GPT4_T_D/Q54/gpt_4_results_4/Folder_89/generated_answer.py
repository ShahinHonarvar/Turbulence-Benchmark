
def all_right_truncatable_prime(tuple_values):
    x = tuple_values[97]
    all_prime = [i for i in range(2, x) if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1))]
    right_truncatable_primes = []
    for prime in all_prime:
        str_prime = str(prime)
        while str_prime:
            if all(int(str_prime) % j != 0 for j in range(2, int(int(str_prime)**0.5) + 1)):
                str_prime = str_prime[:-1]
            else:
                break
        if not str_prime:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)
