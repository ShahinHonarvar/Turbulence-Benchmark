
def all_left_truncatable_prime(x):
    prime_numbers = []
    for num in range(2, x + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return sorted(prime_numbers)
