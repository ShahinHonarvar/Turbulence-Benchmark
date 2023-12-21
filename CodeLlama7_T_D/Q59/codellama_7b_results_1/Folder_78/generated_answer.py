
def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[23]
    list_of_all_left_truncatable_prime_numbers = []
    for i in range(x):
        if is_prime(i) and is_left_truncatable_prime(i, x):
            list_of_all_left_truncatable_prime_numbers.append(i)
    return sorted(list_of_all_left_truncatable_prime_numbers)
