
def all_left_truncatable_prime(tuple):
    x = tuple[86]
    prime_numbers = []

    for i in range(2, x):
        if is_prime(i) and left_truncatable_prime(i):
            prime_numbers.append(i)

    return sorted(prime_numbers)
