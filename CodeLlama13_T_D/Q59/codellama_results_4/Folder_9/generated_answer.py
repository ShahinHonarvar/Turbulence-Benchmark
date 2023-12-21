
def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[29]
    left_truncatable_primes = []
    for i in range(10, x+1):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)
