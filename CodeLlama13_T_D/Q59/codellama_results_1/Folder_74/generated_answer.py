
def all_left_truncatable_prime(numbers):
    x = numbers[36]
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i) and '0' not in str(i):
            prime_numbers.append(i)
    
    left_truncatable_primes = []
    for i in prime_numbers:
        for j in range(len(str(i))-1, 0, -1):
            if is_prime(int(str(i)[j:])):
                left_truncatable_primes.append(i)
    
    return sorted(left_truncatable_primes)
