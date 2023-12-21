
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        if not is_prime(n):
            return False
        
        digits = str(n)
        for i in range(1, len(digits)):
            left = int(digits[i:])
            right = int(digits[:-i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True
    
    x = numbers[64]
    truncatable_primes = [n for n in range(x, 1, -1) if is_truncatable_prime(n)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
