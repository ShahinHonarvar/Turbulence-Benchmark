
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[992]
    primes = []
    
    def is_left_truncatable_prime(number):
        num_str = str(number)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True
    
    for i in range(2, x):
        if '0' not in str(i) and is_left_truncatable_prime(i):
            primes.append(i)
    
    return sorted(primes)
