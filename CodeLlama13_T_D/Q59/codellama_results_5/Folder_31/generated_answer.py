
def all_left_truncatable_prime(tuple):
    x = tuple[50]
    prime_numbers = []
    for i in range(x + 1):
        if is_prime(i) and not "0" in str(i):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)
