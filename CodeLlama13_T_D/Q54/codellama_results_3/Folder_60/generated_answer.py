
def all_right_truncatable_prime(x):
    prime_numbers = []
    for i in range(10**8, x+1):
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers)
