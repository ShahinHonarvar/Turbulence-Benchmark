
def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[126]
    right_truncatable_primes = []
    for i in range(x, 0, -1):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
