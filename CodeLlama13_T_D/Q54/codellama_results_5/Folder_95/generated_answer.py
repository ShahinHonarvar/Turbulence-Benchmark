
def all_right_truncatable_prime(numbers):
    x = numbers[77]
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)
