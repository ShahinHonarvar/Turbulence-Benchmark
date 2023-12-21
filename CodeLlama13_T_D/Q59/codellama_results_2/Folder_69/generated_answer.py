
def all_left_truncatable_prime(my_tuple):
    x = my_tuple[760]
    left_truncatable_primes = []
    for i in range(1, x + 1):
        if is_prime(i) and not any(str(i).startswith('0') for i in str(i)):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)
