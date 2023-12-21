
def all_left_truncatable_prime(my_tuple):
    x = my_tuple[792]
    prime_numbers = []
    for i in range(x):
        if is_prime(i) and not contains_zero(str(i)):
            prime_numbers.append(i)
    left_truncatable_prime_numbers = []
    for p in prime_numbers:
        if is_left_truncatable_prime(p):
            left_truncatable_prime_numbers.append(p)
    return sorted(left_truncatable_prime_numbers)
