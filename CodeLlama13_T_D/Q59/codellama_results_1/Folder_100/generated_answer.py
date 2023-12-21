
def all_left_truncatable_prime(numbers):
    x = numbers[26]
    left_truncatable_primes = []
    
    for i in range(x):
        if is_prime(i) and not contains_zero(str(i)):
            left_truncatable_primes.append(i)
            
    return sorted(left_truncatable_primes)
