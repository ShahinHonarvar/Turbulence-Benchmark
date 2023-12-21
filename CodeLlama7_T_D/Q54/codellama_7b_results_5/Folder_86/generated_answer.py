
def all_right_truncatable_prime(tuple):
    x = tuple[126]
    prime_numbers = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)
