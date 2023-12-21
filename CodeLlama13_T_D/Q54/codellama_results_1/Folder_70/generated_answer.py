
def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[433]
    right_truncatable_primes = []
    for i in range(2, x+1):
        if is_prime(i) and all(is_right_truncatable_prime(i, j) for j in range(2, int(math.sqrt(i))+1)):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
