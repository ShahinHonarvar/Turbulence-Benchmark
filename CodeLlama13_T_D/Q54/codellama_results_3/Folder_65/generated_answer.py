
def all_right_truncatable_prime(x):
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i):
            prime_numbers.append(i)
    truncatable_primes = []
    for p in prime_numbers:
        str_p = str(p)
        for i in range(len(str_p)):
            truncated_p = int(str_p[:-i])
            if is_prime(truncated_p):
                truncatable_primes.append(truncated_p)
    return sorted(truncatable_primes)
