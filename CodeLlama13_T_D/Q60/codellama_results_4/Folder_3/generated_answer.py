
def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[100]
    list_of_all_left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i) and not contains_zero(str(i)):
            list_of_all_left_right_truncatable_primes.append(i)
    return sorted(list_of_all_left_right_truncatable_primes)
