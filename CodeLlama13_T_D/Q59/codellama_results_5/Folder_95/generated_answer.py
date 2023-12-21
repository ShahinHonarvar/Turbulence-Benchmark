
def all_left_truncatable_prime(numbers):
    x = numbers[77]
    prime_numbers = []
    for num in range(2, x+1):
        if is_prime(num) and '0' not in str(num):
            prime_numbers.append(num)
    
    left_truncatable_primes = []
    for prime in prime_numbers:
        for i in range(len(str(prime))):
            if is_prime(int(str(prime)[:i])):
                left_truncatable_primes.append(prime)
    
    return sorted(left_truncatable_primes)

def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
