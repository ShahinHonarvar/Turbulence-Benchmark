
def all_left_truncatable_prime(tuple_of_positive_integers):
    prime_numbers = []
    for num in tuple_of_positive_integers:
        if is_prime(num) and not any(str(num)[1:] == '0'):
            prime_numbers.append(num)
    return sorted(prime_numbers)
