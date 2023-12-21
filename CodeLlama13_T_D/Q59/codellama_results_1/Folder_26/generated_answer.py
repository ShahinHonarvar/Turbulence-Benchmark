
def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[81]
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_0(str(i)):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)
