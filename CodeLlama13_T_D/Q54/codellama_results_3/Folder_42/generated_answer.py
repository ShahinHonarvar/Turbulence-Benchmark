
def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[64]
    right_truncatable_primes = []
    for i in range(x-1, 0, -1):
        if is_prime(i) and all(is_right_truncatable_prime(str(i)) for j in range(len(str(i)))):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
