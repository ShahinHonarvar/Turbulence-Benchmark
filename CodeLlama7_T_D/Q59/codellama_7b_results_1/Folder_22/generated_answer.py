
def all_left_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[85]
    list_of_left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i, x):
            list_of_left_truncatable_primes.append(i)
    return sorted(list_of_left_truncatable_primes)
