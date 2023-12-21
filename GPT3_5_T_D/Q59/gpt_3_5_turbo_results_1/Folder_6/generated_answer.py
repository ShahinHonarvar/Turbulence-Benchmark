
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    x = numbers[74]
    left_truncatable_primes = []
    
    def check_left_truncatable_prime(n):
        if '0' in str(n):  # Check if number contains 0
            return False
        
        while n > 0:
            if not is_prime(n):
                return False
            n = int(str(n)[1:])  # Remove leftmost digit
        
        return True
    
    for i in range(2, x):
        if check_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    
    return sorted(left_truncatable_primes)
