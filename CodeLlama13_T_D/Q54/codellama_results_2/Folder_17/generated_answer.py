
def all_right_truncatable_prime(numbers):
    x = numbers[36]
    prime_numbers = []
    for i in range(2, x + 1):
        if is_prime(i):
            prime_numbers.append(i)
    
    right_truncatable_primes = []
    for p in prime_numbers:
        for i in range(len(str(p)) - 1, 0, -1):
            if is_prime(int(str(p)[:i])):
                right_truncatable_primes.append(int(str(p)[:i]))
    
    return sorted(right_truncatable_primes, reverse=True)
