
def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[74]
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i) and '0' not in str(i):
            prime_numbers.append(i)
    return sorted(prime_numbers)
