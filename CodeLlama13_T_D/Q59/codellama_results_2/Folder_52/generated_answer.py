
def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[52]
    prime_numbers = []
    for i in range(10**x):
        if is_prime(i) and not any(str(i).startswith('0') for i in range(len(str(i)))):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)
