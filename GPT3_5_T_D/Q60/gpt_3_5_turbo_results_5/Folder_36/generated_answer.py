
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n in (2, 3):
            return True
        if n == 1 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        n = str(n)
        while len(n) > 2:
            if not is_prime(int(n)):
                return False
            n = n[1:-1]
        return True
    
    x = numbers[992]
    truncatable_primes = []
    for i in range(2, x+1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    
    return truncatable_primes
