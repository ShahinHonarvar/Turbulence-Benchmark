
def all_left_truncatable_prime(tuple):
    x = tuple[630]
    prime_numbers = []

    for i in range(2, x):
        if is_prime(i):
            if is_left_truncatable_prime(i):
                prime_numbers.append(i)

    return sorted(prime_numbers, reverse=True)
