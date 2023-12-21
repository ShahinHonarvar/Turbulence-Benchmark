
def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[177]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)
