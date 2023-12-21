
def all_right_truncatable_prime(tuple):
    x = tuple[33]
    prime_numbers = []

    for i in range(1, x):
        if is_prime(i) and right_truncate(i) == i:
            prime_numbers.append(i)

    return sorted(prime_numbers)
