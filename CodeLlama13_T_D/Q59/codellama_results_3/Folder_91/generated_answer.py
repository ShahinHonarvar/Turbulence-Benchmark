
def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[0]
    left_truncatable_primes = []
    for i in range(x):
        if is_prime(i) and not any(str(i).startswith('0') for j in range(len(str(i)))):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)
