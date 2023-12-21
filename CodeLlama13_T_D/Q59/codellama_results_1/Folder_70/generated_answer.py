
def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[433]
    left_truncatable_primes = []
    for i in range(x):
        if is_prime(i) and '0' not in str(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)
