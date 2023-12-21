
def all_left_truncatable_prime(numbers):
    x = numbers[14]
    left_truncatable_primes = []
    for i in range(2, x+1):
        if is_prime(i) and not any(str(i).startswith('0') for i in range(2, x)):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)
