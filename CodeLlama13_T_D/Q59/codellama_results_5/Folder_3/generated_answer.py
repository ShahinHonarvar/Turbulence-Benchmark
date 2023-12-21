
def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[100]
    list_of_left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and contains_no_zero(i):
            list_of_left_truncatable_primes.append(i)
    return sorted(list_of_left_truncatable_primes)
